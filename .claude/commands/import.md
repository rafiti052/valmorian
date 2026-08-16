---
description: Convert raw notes into OKF concepts in the codex
argument-hint: "[path in sources/, a Google Doc or Notion link, or nothing to sweep all of sources/]"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, Task
---

Import campaign material into the codex. Source: **$ARGUMENTS**

If no argument was given, sweep everything not yet ingested. Start with:

```bash
python3 scripts/import_status.py
```

It lists source files no concept cites yet (`!`), what is already converted, and any
`sources[].resource` pointing at a file that has since vanished.

Follow the **notes-import** skill. The order matters:

1. **Survey everything first.** Read all of it before converting anything, or you will
   create several concepts for the same character under different spellings.
2. **Show the GM a manifest before writing a single concept** — proposed concepts with
   types and paths, source-to-concept mapping, detected duplicates and name variants,
   contradictions between sources, and anything you could not classify. Wait for his go.
3. **Convert**, preserving his wording. Import is not an editing pass.
4. **Set provenance honestly** — `generated: { by: process:okf-import, ... }` and a
   `sources` entry with the real URL or path, SHA-256 for local files, coverage, and a
   page/field/section locator when available. Everything lands as `status: draft`.
5. **Never guess `visibility: public`.** Default unmarked material to `secret` and list
   it in the report as needing a visibility pass.
6. **Reconcile** — absolute links, directory indexes, a `codex/log.md` entry, then
   `python3 scripts/okf_validate.py` and `qmd update && qmd embed`.

Report what was created, what was skipped and why, which conflicts need his ruling, and
which concepts need a visibility pass. Be explicit about gaps — a silent one is a fact he
discovers mid-session.

If the notes are in Google Drive or Notion, those connectors are available; use them
rather than asking him to copy and paste.
