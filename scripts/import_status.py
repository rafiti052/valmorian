#!/usr/bin/env python3
"""Report ingestion coverage for every file under sources/.

Uses `docs/source-ingestion-manifest.md` as the source-level registry and reports codex
citations separately. A citation without an explicit `coverage` is conservatively
`partial`: being referenced is not proof that the source was fully ingested.

Usage:
    python3 scripts/import_status.py [--json]

Exit codes:
    0  every source is full, catalog-only, or intentionally deferred
    1  pending or partially ingested material found
    2  manifest/hash integrity error or could not run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("error: PyYAML is required. Install with: pip install pyyaml\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES = REPO_ROOT / "sources"
CODEX = REPO_ROOT / "codex"
MANIFEST = REPO_ROOT / "docs" / "source-ingestion-manifest.md"
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)

# files that are scaffolding, not campaign material
IGNORED_NAMES = {"README.md", ".gitkeep", ".DS_Store"}
COVERAGE = ("full", "partial", "catalog-only", "deferred")
DISPOSITIONS = ("pending",) + COVERAGE
AVAILABILITY = ("tracked", "local-only")


def referenced_resources() -> dict[str, list[dict[str, str]]]:
    """Map normalised resource string -> concepts and declared coverage."""
    refs: dict[str, list[dict[str, str]]] = {}
    for path in CODEX.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(meta, dict):
            continue
        entries = meta.get("sources")
        if not isinstance(entries, list):
            continue
        rel_concept = path.relative_to(CODEX).as_posix()
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            res = entry.get("resource")
            if not isinstance(res, str):
                continue
            coverage = entry.get("coverage", "partial")
            if coverage not in COVERAGE:
                coverage = "partial"
            refs.setdefault(normalise(res), []).append({
                "concept": rel_concept,
                "coverage": coverage,
            })
    return refs


FILE_EXT_RE = re.compile(
    r"\.(md|markdown|txt|text|json|csv|tsv|pdf|docx?|rtf|png|jpe?g|webp|heic)$",
    re.IGNORECASE,
)


def is_url(resource: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*://", resource.strip(), re.IGNORECASE))


def is_file_reference(resource: str) -> bool:
    """True when a resource string points at a file in sources/.

    A citation like 'D&D 2024 Monster Manual — Doppelganger' is a legitimate
    provenance record with no file behind it, and must not be reported as missing.
    """
    r = resource.strip()
    if is_url(r):
        return False
    if not FILE_EXT_RE.search(r):
        return False
    return True


def normalise(resource: str) -> str:
    """Reduce a resource string to a comparable form.

    Accepts '/sources/x.md', 'sources/x.md', './sources/x.md', or a bare 'x.md'.
    URLs and free-text citations pass through lowercased and unchanged in shape.
    """
    r = resource.strip()
    if is_url(r):
        return r.lower()
    r = r.lstrip("./").lstrip("/")
    if r.startswith("sources/"):
        r = r[len("sources/"):]
    return r.lower()


def normalise_target(target: str) -> str | None:
    """Return a canonical codex-relative Markdown target, or None.

    Manifest targets use OKF bundle-root paths (for example ``/party/bob.md``).
    Non-codex destinations such as ``qmd://rulebooks-local/`` are useful notes,
    but cannot establish that a source has been ingested into a codex concept.
    """
    value = target.strip()
    if is_url(value) or not value.lower().endswith(".md"):
        return None
    value = value.lstrip("./").lstrip("/")
    if value.startswith("codex/"):
        value = value[len("codex/"):]
    if not value or any(part in ("", ".", "..") for part in Path(value).parts):
        return None
    return value


def validate_terminal_disposition(
    resource: str,
    disposition: str,
    manifest_entry: dict,
    source_refs: list[dict[str, str]],
) -> list[str]:
    """Prove a terminal disposition with real targets and source citations."""
    errors: list[str] = []
    raw_targets = manifest_entry.get("targets")
    if not isinstance(raw_targets, list) or not raw_targets:
        return [f"terminal resource {resource} needs a non-empty targets list"]

    codex_targets: list[str] = []
    for target in raw_targets:
        if not isinstance(target, str):
            errors.append(f"terminal resource {resource} has a non-string target")
            continue
        normalised = normalise_target(target)
        if normalised is not None:
            codex_targets.append(normalised)
        elif not target.strip().lower().startswith("qmd://"):
            errors.append(
                f"terminal resource {resource} has an invalid codex target: {target}"
            )

    if not codex_targets:
        errors.append(f"terminal resource {resource} needs a codex Markdown target")
        return errors

    refs_by_concept: dict[str, set[str]] = {}
    for source_ref in source_refs:
        refs_by_concept.setdefault(source_ref["concept"], set()).add(
            source_ref["coverage"]
        )
    for target in codex_targets:
        target_path = CODEX / target
        if not target_path.is_file():
            errors.append(
                f"terminal resource {resource} target does not exist: /{target}"
            )
            continue
        target_coverages = refs_by_concept.get(target, set())
        if not target_coverages:
            errors.append(
                f"terminal resource {resource} target does not cite the source: /{target}"
            )
        elif disposition == "full" and not target_coverages.intersection(
            {"partial", "full"}
        ):
            declared = ", ".join(sorted(target_coverages))
            errors.append(
                f"full resource {resource} target /{target} has incompatible "
                f"coverage: {declared}"
            )
        elif (
            disposition in ("catalog-only", "deferred")
            and disposition not in target_coverages
        ):
            declared = ", ".join(sorted(target_coverages))
            errors.append(
                f"terminal resource {resource} target /{target} needs coverage "
                f"{disposition}, found: {declared}"
            )

    if not source_refs:
        errors.append(f"terminal resource {resource} has no codex source reference")
    return errors


def effective_coverage(
    disposition: str,
    source_refs: list[dict[str, str]],
    terminal_errors: list[str],
) -> str:
    """Derive coverage conservatively from evidence, bounded by the manifest.

    Pending entries stay non-terminal even when a concept already cites them.
    Partial entries without a citation fall back to pending. Terminal entries are
    only accepted after their declared targets and citation coverage validate.
    """
    if disposition in ("full", "catalog-only", "deferred"):
        if not terminal_errors:
            return disposition
        return "partial" if source_refs else "pending"
    if disposition == "partial" or source_refs:
        return "partial" if source_refs else "pending"
    return "pending"


def load_manifest() -> tuple[dict[str, dict], list[str]]:
    """Load the source-level registry embedded in the Markdown manifest."""
    if not MANIFEST.is_file():
        return {}, [f"manifest not found: {MANIFEST.relative_to(REPO_ROOT)}"]
    text = MANIFEST.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, ["manifest has no YAML frontmatter"]
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {}, [f"manifest YAML is invalid: {exc}"]
    raw_entries = meta.get("sources") if isinstance(meta, dict) else None
    if not isinstance(raw_entries, list):
        return {}, ["manifest frontmatter needs a sources list"]

    entries: dict[str, dict] = {}
    errors: list[str] = []
    for index, entry in enumerate(raw_entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"manifest source #{index} is not a mapping")
            continue
        resource = entry.get("resource")
        if not isinstance(resource, str):
            errors.append(f"manifest source #{index} has no resource")
            continue
        key = normalise(resource)
        if key in entries:
            errors.append(f"manifest repeats resource: {resource}")
            continue
        disposition = entry.get("disposition")
        if disposition not in DISPOSITIONS:
            errors.append(
                f"manifest resource {resource} has invalid disposition {disposition!r}"
            )
        digest = entry.get("sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"manifest resource {resource} has invalid sha256")
        availability = entry.get("availability")
        if availability not in AVAILABILITY:
            errors.append(
                f"manifest resource {resource} has invalid availability {availability!r}"
            )
        entries[key] = entry
    return entries, errors


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="Report un-ingested source material.")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    if not SOURCES.is_dir():
        sys.stderr.write("error: sources/ not found\n")
        return 2

    refs = referenced_resources()
    manifest, manifest_errors = load_manifest()

    groups: dict[str, list[dict[str, object]]] = {name: [] for name in COVERAGE}
    referenced: list[dict[str, object]] = []
    pending: list[dict[str, object]] = []
    hash_mismatches: list[dict[str, str]] = []
    unavailable_local: list[dict[str, object]] = []
    on_disk_paths = {
        normalise(path.relative_to(SOURCES).as_posix()): path
        for path in SOURCES.rglob("*")
        if path.is_file() and path.name not in IGNORED_NAMES
    }
    all_keys = sorted(set(on_disk_paths) | set(manifest))

    for key in all_keys:
        path = on_disk_paths.get(key)
        source_refs = refs.get(key, [])
        manifest_entry = manifest.get(key)
        if manifest_entry is not None:
            resource = str(manifest_entry.get("resource"))
            rel = resource.lstrip("/")
            if rel.startswith("sources/"):
                rel = rel[len("sources/"):]
            disposition = manifest_entry.get("disposition", "pending")
            availability = manifest_entry.get("availability")
            terminal_errors: list[str] = []
            if disposition in ("full", "catalog-only", "deferred"):
                terminal_errors = validate_terminal_disposition(
                    resource, disposition, manifest_entry, source_refs
                )
                manifest_errors.extend(terminal_errors)
            coverage = effective_coverage(disposition, source_refs, terminal_errors)
            if path is not None:
                expected_hash = manifest_entry.get("sha256")
                actual_hash = sha256_file(path)
                if expected_hash != actual_hash:
                    hash_mismatches.append({
                        "source": rel,
                        "expected": str(expected_hash),
                        "actual": actual_hash,
                    })
            elif availability == "tracked":
                manifest_errors.append(f"tracked manifest resource is missing: {resource}")
            record = {
                "source": rel,
                "coverage": coverage,
                "disposition": disposition,
                "proposed_coverage": manifest_entry.get("proposed_disposition"),
                "concepts": sorted({entry["concept"] for entry in source_refs}),
                "availability": availability,
                "available": path is not None,
            }
            if path is None and availability == "local-only":
                unavailable_local.append(record)
        elif source_refs:
            assert path is not None
            rel = path.relative_to(SOURCES).as_posix()
            coverage = "pending"
            manifest_errors.append(f"source is missing from the manifest: /sources/{rel}")
            record = {
                "source": rel,
                "coverage": coverage,
                "disposition": None,
                "proposed_coverage": None,
                "concepts": sorted({entry["concept"] for entry in source_refs}),
                "availability": None,
                "available": True,
            }
        else:
            assert path is not None
            rel = path.relative_to(SOURCES).as_posix()
            coverage = "pending"
            manifest_errors.append(f"source is missing from the manifest: /sources/{rel}")
            record = {
                "source": rel,
                "coverage": coverage,
                "disposition": None,
                "proposed_coverage": None,
                "concepts": [],
                "availability": None,
                "available": True,
            }

        if source_refs:
            referenced.append(record)
        if coverage == "pending":
            pending.append(record)
        else:
            groups[coverage].append(record)

    # resources cited by concepts that no longer exist on disk
    local_only = {
        key for key, entry in manifest.items()
        if entry.get("availability") == "local-only"
    }
    dangling = sorted(
        res for res in refs
        if is_file_reference(res) and res not in on_disk_paths and res not in local_only
    )
    citations = sorted(
        res for res in refs if not is_file_reference(res) and not is_url(res)
    )

    if args.as_json:
        print(json.dumps({
            "pending": pending,
            "full": groups["full"],
            "partial": groups["partial"],
            "catalog_only": groups["catalog-only"],
            "deferred": groups["deferred"],
            "referenced": referenced,
            "dangling": dangling,
            "citations": citations,
            "unavailable_local": unavailable_local,
            "manifest_errors": manifest_errors,
            "hash_mismatches": hash_mismatches,
        }, indent=2))
    else:
        if pending:
            print(f"Un-ingested ({len(pending)}):")
            for record in pending:
                proposed = record.get("proposed_coverage")
                suffix = f" (proposed: {proposed})" if proposed else ""
                print(f"  ! {record['source']}{suffix}")
        labels = {
            "full": "Fully ingested",
            "partial": "Partially ingested",
            "catalog-only": "Catalog only",
            "deferred": "Deferred",
        }
        for coverage in COVERAGE:
            records = groups[coverage]
            if not records:
                continue
            print(f"\n{labels[coverage]} ({len(records)}):")
            for record in records:
                concepts = ", ".join(record["concepts"])
                print(f"  {coverage:12} {record['source']}  ->  {concepts}")
        if dangling:
            print(f"\nCited but missing from sources/ ({len(dangling)}):")
            for res in dangling:
                print(f"  ? {res}")
        if citations:
            print(f"\nExternal citations, no file expected ({len(citations)}):")
            for res in citations:
                print(f"  - {res}")
        if unavailable_local:
            print(f"\nLocal-only sources not present ({len(unavailable_local)}):")
            for record in unavailable_local:
                print(f"  - {record['source']}")
        if manifest_errors:
            print(f"\nManifest errors ({len(manifest_errors)}):")
            for error in manifest_errors:
                print(f"  x {error}")
        if hash_mismatches:
            print(f"\nHash mismatches ({len(hash_mismatches)}):")
            for item in hash_mismatches:
                print(f"  x {item['source']}: expected {item['expected']}, got {item['actual']}")
        if not pending and not referenced and not dangling:
            print("sources/ is empty — nothing to ingest yet.")
        elif not pending and not groups["partial"]:
            print("\nAll source material has a terminal ingestion disposition.")

    if manifest_errors or hash_mismatches:
        return 2
    return 1 if pending or groups["partial"] else 0


if __name__ == "__main__":
    sys.exit(main())
