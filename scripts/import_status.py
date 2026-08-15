#!/usr/bin/env python3
"""Report which files under sources/ have not yet been converted into codex concepts.

Compares every file in sources/ against the `sources[].resource` values recorded in
codex/ frontmatter. Anything unreferenced is un-ingested.

Usage:
    python3 scripts/import_status.py [--json]

Exit codes:
    0  everything under sources/ is referenced by at least one concept
    1  un-ingested material found
    2  could not run
"""

from __future__ import annotations

import argparse
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
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)

# files that are scaffolding, not campaign material
IGNORED_NAMES = {"README.md", ".gitkeep"}


def referenced_resources() -> dict[str, list[str]]:
    """Map normalised resource string -> concepts that cite it."""
    refs: dict[str, list[str]] = {}
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
            refs.setdefault(normalise(res), []).append(rel_concept)
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


def main() -> int:
    ap = argparse.ArgumentParser(description="Report un-ingested source material.")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    if not SOURCES.is_dir():
        sys.stderr.write("error: sources/ not found\n")
        return 2

    refs = referenced_resources()

    ingested: list[tuple[str, list[str]]] = []
    pending: list[str] = []

    for path in sorted(SOURCES.rglob("*")):
        if not path.is_file():
            continue
        if path.name in IGNORED_NAMES:
            continue
        rel = path.relative_to(SOURCES).as_posix()
        key = normalise(rel)
        if key in refs:
            ingested.append((rel, refs[key]))
        else:
            pending.append(rel)

    # resources cited by concepts that no longer exist on disk
    on_disk = {normalise(p.relative_to(SOURCES).as_posix())
               for p in SOURCES.rglob("*") if p.is_file()}
    dangling = sorted(
        res for res in refs
        if is_file_reference(res) and res not in on_disk
    )
    citations = sorted(
        res for res in refs if not is_file_reference(res) and not is_url(res)
    )

    if args.as_json:
        print(json.dumps({
            "pending": pending,
            "ingested": [{"source": s, "concepts": c} for s, c in ingested],
            "dangling": dangling,
            "citations": citations,
        }, indent=2))
    else:
        if pending:
            print(f"Un-ingested ({len(pending)}):")
            for rel in pending:
                print(f"  ! {rel}")
        if ingested:
            print(f"\nIngested ({len(ingested)}):")
            for rel, concepts in ingested:
                print(f"  ok {rel}  ->  {', '.join(concepts)}")
        if dangling:
            print(f"\nCited but missing from sources/ ({len(dangling)}):")
            for res in dangling:
                print(f"  ? {res}")
        if citations:
            print(f"\nExternal citations, no file expected ({len(citations)}):")
            for res in citations:
                print(f"  - {res}")
        if not pending and not ingested and not dangling:
            print("sources/ is empty — nothing to ingest yet.")
        elif not pending:
            print("\nAll source material has been ingested.")

    return 1 if pending else 0


if __name__ == "__main__":
    sys.exit(main())
