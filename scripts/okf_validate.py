#!/usr/bin/env python3
"""Validate the Valmorian codex against the OKF v0.2 profile in docs/OKF-PROFILE.md.

Checks conformance of frontmatter, the integrity of the cross-link graph, and the
profile-specific rules (secrecy tiers, provenance honesty, type/directory agreement).

Exit codes:
    0  no errors (warnings may still be present)
    1  one or more errors
    2  could not run (missing dependency, bad bundle root)

Usage:
    python3 scripts/okf_validate.py [--strict] [--json] [--bundle codex]

    --strict  treat warnings as errors
    --json    machine-readable output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("error: PyYAML is required. Install with: pip install pyyaml\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent

# --- profile constants (keep in sync with docs/OKF-PROFILE.md) ---------------

REQUIRED_FIELDS = ("type", "title", "description", "visibility", "status")
VISIBILITY = {"public", "rumored", "secret"}
STATUS = {"draft", "stable", "deprecated"}
PRESSURE = {"dormant", "simmering", "urgent", "resolved"}
DISPOSITION = {"hostile", "wary", "neutral", "friendly", "devoted"}
SOURCE_COVERAGE = {"full", "partial", "catalog-only", "deferred"}

# type -> directories the type is allowed to live in (relative to bundle root)
TYPE_DIRS = {
    "Campaign": {""},
    "Change Log": {""},
    "World Concept": {"world", "arcs", "threads", "factions", "npcs", "locations",
                      "sessions", "party", "items", "rules", "bestiary", "rulebooks",
                      "homebrew"},
    "NPC": {"npcs"},
    "Faction": {"factions"},
    "Region": {"locations"},
    "Settlement": {"locations"},
    "Site": {"locations"},
    "Story Arc": {"arcs"},
    "Plot Thread": {"threads"},
    "Session Plan": {"sessions"},
    "Session Recap": {"sessions"},
    "Player Character": {"party"},
    "Item": {"items"},
    "House Rule": {"rules"},
    "Stat Block": {"bestiary"},
    "Rulebook": {"rulebooks"},
    "Homebrew": {"homebrew"},
}

# frontmatter fields whose values are links into the bundle
LINK_FIELDS_SINGLE = ("arc", "first_appeared", "last_seen", "stat_block")
LINK_FIELDS_LIST = ("threads", "pcs")

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")
SECRET_BLOCK_RE = re.compile(r"^>\s*\[!secret\]", re.MULTILINE | re.IGNORECASE)
AGENT_ACTOR_RE = re.compile(r"^(claude|gpt|gemini|process:|[a-z0-9_.-]+/)", re.IGNORECASE)
LANG_RE = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]{2,8})*$")


@dataclass
class Finding:
    level: str          # "error" | "warning"
    path: str
    message: str

    def render(self) -> str:
        return f"{self.path}: {self.message}"


@dataclass
class Concept:
    path: Path                    # absolute
    rel: str                      # relative to bundle root, e.g. "npcs/serath-vane.md"
    meta: dict
    body: str
    links: list = field(default_factory=list)


def parse_file(path: Path, bundle: Path) -> tuple[Concept | None, list[Finding]]:
    rel = path.relative_to(bundle).as_posix()
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")

    match = FRONTMATTER_RE.match(text)
    if not match:
        findings.append(Finding("error", rel, "no YAML frontmatter block"))
        return None, findings

    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        detail = str(exc).replace("\n", " ")[:160]
        findings.append(Finding("error", rel, f"invalid YAML frontmatter: {detail}"))
        return None, findings

    if not isinstance(meta, dict):
        findings.append(Finding("error", rel, "frontmatter is not a mapping"))
        return None, findings

    body = text[match.end():]
    concept = Concept(path=path, rel=rel, meta=meta, body=body,
                      links=MD_LINK_RE.findall(body))
    return concept, findings


def check_fields(c: Concept) -> list[Finding]:
    out: list[Finding] = []
    m = c.meta

    for fname in REQUIRED_FIELDS:
        if fname not in m or m[fname] in (None, ""):
            out.append(Finding("error", c.rel, f"missing required field '{fname}'"))

    vis = m.get("visibility")
    if vis is not None and vis not in VISIBILITY:
        out.append(Finding("error", c.rel,
                           f"visibility '{vis}' not one of {sorted(VISIBILITY)}"))

    status = m.get("status")
    if status is not None and status not in STATUS:
        out.append(Finding("error", c.rel,
                           f"status '{status}' not one of {sorted(STATUS)}"))

    desc = m.get("description")
    if isinstance(desc, str) and len(desc) > 300:
        out.append(Finding("warning", c.rel,
                           f"description is {len(desc)} chars; aim for one sentence"))

    ctype = m.get("type")
    if ctype is not None:
        if ctype not in TYPE_DIRS:
            out.append(Finding("warning", c.rel,
                               f"type '{ctype}' is not in the profile's type table"))
        else:
            parent = str(Path(c.rel).parent)
            parent = "" if parent == "." else parent.split("/")[0]
            allowed = TYPE_DIRS[ctype]
            if parent not in allowed:
                out.append(Finding("error", c.rel,
                                   f"type '{ctype}' should live in {sorted(allowed)}, "
                                   f"found in '{parent or '<bundle root>'}'"))

    if "timestamp" in m:
        out.append(Finding("warning", c.rel,
                           "'timestamp' is OKF v0.1; use generated.at instead"))

    gen = m.get("generated")
    if gen is not None:
        if not isinstance(gen, dict) or "by" not in gen:
            out.append(Finding("error", c.rel,
                               "generated must be a mapping with at least a 'by' field"))
        elif "at" not in gen:
            out.append(Finding("warning", c.rel, "generated has no 'at' timestamp"))

    ver = m.get("verified")
    if ver is not None:
        if not isinstance(ver, list):
            out.append(Finding("error", c.rel, "verified must be a list"))
        else:
            for entry in ver:
                if not isinstance(entry, dict) or "by" not in entry:
                    out.append(Finding("error", c.rel,
                                       "each verified entry needs a 'by' field"))
                    continue
                by = str(entry["by"])
                if not by.startswith("human:"):
                    out.append(Finding("error", c.rel,
                                       f"verified.by '{by}' is not a human actor — "
                                       "only a human can verify (profile §5)"))

    for fname in ("pressure", "disposition"):
        val = m.get(fname)
        valid = PRESSURE if fname == "pressure" else DISPOSITION
        if val is not None and val not in valid:
            out.append(Finding("error", c.rel,
                               f"{fname} '{val}' not one of {sorted(valid)}"))

    stale = m.get("stale_after")
    if stale is not None:
        parsed = stale if isinstance(stale, date) else None
        if parsed is None:
            try:
                parsed = datetime.strptime(str(stale), "%Y-%m-%d").date()
            except ValueError:
                out.append(Finding("error", c.rel,
                                   f"stale_after '{stale}' is not YYYY-MM-DD"))
        if parsed is not None and parsed < date.today():
            out.append(Finding("warning", c.rel,
                               f"stale since {parsed.isoformat()}"))

    srcs = m.get("sources")
    if srcs is not None:
        if not isinstance(srcs, list):
            out.append(Finding("error", c.rel, "sources must be a list"))
        else:
            for entry in srcs:
                if not isinstance(entry, dict) or not isinstance(entry.get("resource"), str) \
                        or not entry["resource"].strip():
                    out.append(Finding("error", c.rel,
                                       "each sources entry needs a non-empty string "
                                       "'resource' field"))
                    continue
                local_source = entry["resource"].startswith("/sources/")
                coverage = entry.get("coverage")
                if local_source and coverage is None:
                    out.append(Finding(
                        "error", c.rel,
                        "local /sources/ entry needs a 'coverage' field",
                    ))
                if coverage is not None and coverage not in SOURCE_COVERAGE:
                    out.append(Finding(
                        "error", c.rel,
                        f"sources coverage '{coverage}' not one of "
                        f"{sorted(SOURCE_COVERAGE)}",
                    ))
                digest = entry.get("sha256")
                if local_source and digest is None:
                    out.append(Finding(
                        "error", c.rel,
                        "local /sources/ entry needs a 'sha256' field",
                    ))
                if digest is not None and not re.fullmatch(r"[0-9a-fA-F]{64}", str(digest)):
                    out.append(Finding(
                        "error", c.rel,
                        "sources sha256 must be a 64-character hexadecimal digest",
                    ))
                locator = entry.get("locator")
                if local_source and (not isinstance(locator, str) or not locator.strip()):
                    out.append(Finding(
                        "error", c.rel,
                        "local /sources/ entry needs a non-empty string 'locator' field",
                    ))
                elif locator is not None and not isinstance(locator, str):
                    out.append(Finding(
                        "error", c.rel, "sources locator must be a string",
                    ))

    tags = m.get("tags")
    if tags is not None and not isinstance(tags, list):
        out.append(Finding("error", c.rel, "tags must be a YAML list"))

    lang = m.get("lang")
    if lang is not None and not LANG_RE.match(str(lang)):
        out.append(Finding("error", c.rel,
                           f"lang '{lang}' is not a BCP-47 tag (e.g. pt-BR, en)"))

    return out


def resolve_link(target: str, c: Concept) -> str | None:
    """Return a bundle-relative path for an internal link, or None if external."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
        return None                      # http:, mailto:, etc.
    target = target.split("#", 1)[0]
    if not target:
        return None                      # pure anchor
    if target.startswith("/"):
        return target.lstrip("/")
    resolved = (Path(c.rel).parent / target).as_posix()
    return str(Path(resolved)).replace("\\", "/")


def check_links(concepts: list[Concept], bundle: Path) -> list[Finding]:
    out: list[Finding] = []
    known = {c.rel for c in concepts}

    for c in concepts:
        seen: set[str] = set()

        frontmatter_links: list[str] = []
        for fname in LINK_FIELDS_SINGLE:
            val = c.meta.get(fname)
            if isinstance(val, str):
                frontmatter_links.append(val)
        for fname in LINK_FIELDS_LIST:
            val = c.meta.get(fname)
            if isinstance(val, list):
                frontmatter_links.extend(x for x in val if isinstance(x, str))

        for target in frontmatter_links:
            rel = resolve_link(target, c)
            if rel is None:
                continue
            if rel not in known:
                out.append(Finding("error", c.rel,
                                   f"frontmatter link -> '{target}' does not exist"))

        for target in c.links:
            rel = resolve_link(target, c)
            if rel is None:
                continue
            if rel in seen:
                continue
            seen.add(rel)
            if rel in known:
                continue
            # a link outside the bundle (e.g. ../docs/) is fine if the file exists
            outside = (bundle / rel).resolve()
            if outside.exists():
                continue
            if not rel.endswith(".md"):
                out.append(Finding("warning", c.rel,
                                   f"link -> '{target}' not found"))
            else:
                out.append(Finding("warning", c.rel,
                                   f"stub to write: '{target}' has no concept file"))

    return out


def secret_line_flags(body: str) -> list[bool]:
    """For each line of the body, whether it sits inside a > [!secret] blockquote.

    A blockquote continues while lines keep starting with '>'; the first
    non-quoted, non-blank line closes it.
    """
    flags: list[bool] = []
    inside = False
    for line in body.splitlines():
        stripped = line.lstrip()
        if SECRET_BLOCK_RE.match(stripped):
            inside = True
            flags.append(True)
            continue
        if inside:
            if stripped.startswith(">"):
                flags.append(True)
                continue
            if not stripped:
                # blank line inside a quote is ambiguous; keep the block open but
                # do not claim the blank line itself is secret
                flags.append(False)
                continue
            inside = False
        flags.append(False)
    return flags


def check_secrecy(concepts: list[Concept]) -> list[Finding]:
    """Heuristics for the secrecy model. Deliberately conservative."""
    out: list[Finding] = []
    by_rel = {c.rel: c for c in concepts}
    # Session concepts are secret by definition; NPCs and locations linking their
    # first/last appearance is bookkeeping, not a leak, and an export drops those links.
    exempt_types = {"Session Recap", "Session Plan"}

    for c in concepts:
        vis = c.meta.get("visibility")
        body_lines = c.body.splitlines()
        flags = secret_line_flags(c.body)

        if vis == "secret" and SECRET_BLOCK_RE.search(c.body):
            out.append(Finding("warning", c.rel,
                               "concept is already 'secret'; the inline [!secret] block "
                               "is redundant and may hide that the whole file is hidden"))

        if vis != "public":
            continue

        reported: set[str] = set()
        for lineno, line in enumerate(body_lines):
            if flags[lineno]:
                continue
            for target in MD_LINK_RE.findall(line):
                rel = resolve_link(target, c)
                if rel is None or rel in reported:
                    continue
                other = by_rel.get(rel)
                if other is None:
                    continue
                if other.meta.get("visibility") != "secret":
                    continue
                if other.meta.get("type") in exempt_types:
                    continue
                reported.add(rel)
                out.append(Finding("warning", c.rel,
                                   f"line {lineno + 1}: public concept links secret "
                                   f"concept '{rel}' outside a [!secret] block "
                                   "— possible leak"))

    return out


def check_indexes(concepts: list[Concept], bundle: Path) -> list[Finding]:
    out: list[Finding] = []
    dirs = {str(Path(c.rel).parent) for c in concepts if str(Path(c.rel).parent) != "."}
    index_rels = {c.rel for c in concepts if Path(c.rel).name == "index.md"}

    for d in sorted(dirs):
        expected = f"{d}/index.md"
        if expected not in index_rels:
            out.append(Finding("warning", expected,
                               f"directory '{d}' has no index.md"))
            continue
        idx = next(c for c in concepts if c.rel == expected)
        idx_targets = set()
        for t in idx.links:
            rel = resolve_link(t, idx)
            if rel:
                idx_targets.add(rel)
        for c in concepts:
            if str(Path(c.rel).parent) != d or c.rel == expected:
                continue
            if c.rel not in idx_targets:
                out.append(Finding("warning", expected,
                                   f"does not list '{Path(c.rel).name}'"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate the Valmorian OKF bundle.")
    ap.add_argument("--bundle", default="codex", help="bundle root (default: codex)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    bundle = (REPO_ROOT / args.bundle).resolve()
    if not bundle.is_dir():
        sys.stderr.write(f"error: bundle root '{bundle}' not found\n")
        return 2

    findings: list[Finding] = []
    concepts: list[Concept] = []

    for path in sorted(bundle.rglob("*.md")):
        concept, parse_findings = parse_file(path, bundle)
        findings.extend(parse_findings)
        if concept is not None:
            concepts.append(concept)

    if not concepts:
        sys.stderr.write(f"error: no markdown concepts under '{bundle}'\n")
        return 2

    root_index = next((c for c in concepts if c.rel == "index.md"), None)
    if root_index is None:
        findings.append(Finding("error", "index.md",
                                "bundle root has no index.md manifest"))
    elif str(root_index.meta.get("okf_version", "")) != "0.2":
        findings.append(Finding("warning", "index.md",
                                "root index.md should declare okf_version: \"0.2\""))

    campaigns = [c for c in concepts if c.meta.get("type") == "Campaign"]
    if len(campaigns) > 1:
        findings.append(Finding("error", "index.md",
                                f"expected exactly one Campaign concept, found {len(campaigns)}"))

    for c in concepts:
        findings.extend(check_fields(c))
    findings.extend(check_links(concepts, bundle))
    findings.extend(check_secrecy(concepts))
    findings.extend(check_indexes(concepts, bundle))

    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]

    if args.as_json:
        print(json.dumps({
            "concepts": len(concepts),
            "errors": [f.__dict__ for f in errors],
            "warnings": [f.__dict__ for f in warnings],
        }, indent=2))
    else:
        for f in errors:
            print(f"ERROR   {f.render()}")
        for f in warnings:
            print(f"warning {f.render()}")
        print()
        print(f"{len(concepts)} concepts · {len(errors)} errors · {len(warnings)} warnings")
        if not errors and not warnings:
            print("codex is clean.")

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
