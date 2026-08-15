---
name: notes-import
description: Convert raw campaign notes into OKF concepts in the Valmorian codex. Use when importing existing material from Obsidian vaults, Google Docs, Notion pages, World Anvil exports, plain markdown, or scanned session notes — or whenever the user says import, migrate, ingest, bring in my notes, or points at anything in sources/.
allowed-tools: Bash(qmd:*), Bash(python3 scripts/*), Read, Write, Edit, Glob, Grep, WebFetch
---

# Importing existing notes into the codex

Rafael has campaign material that predates this repo. The job is to turn it into OKF
concepts without losing information and without silently inventing the gaps.

## Sources and how to reach them

| Source | Approach |
|--------|----------|
| Loose markdown / Obsidian vault | Already in `sources/`. Obsidian `[[wikilinks]]` become OKF absolute links. |
| Google Docs | The Google Drive connector is available — `search_files`, then `read_file_content`. Record the doc URL in `sources[].resource`. |
| Notion | The Notion connector is available — `notion-search`, then `notion-fetch`. Record the page URL. |
| World Anvil / Kanka / other exports | Ask for a markdown or JSON export committed to `sources/`. |
| Handwritten / scanned | Ask Rafael to transcribe or photograph; read images directly. |

`sources/` is **tracked on purpose**: it is the channel by which material reaches this
repo, and the provenance target for `sources[].resource` links. Never delete or edit a
file there to fix canon — fix the concept in `codex/` instead. Superseded material stays;
it is not competing with canon, because the validator reads only `codex/` and search
labels these results `sources`.

## Procedure

### 1. Survey before converting

Read everything first. Do not convert file-by-file as you go — you will create six NPC
concepts for the same character under different spellings.

Produce a manifest and **show it to Rafael before writing any concept**:

- What concepts you propose to create, with proposed type and path
- Which source material maps to which concept
- Duplicates and name variants you detected
- Contradictions between sources
- Material you could not classify

### 2. Ask about contradictions, do not resolve them

Old notes disagree with each other. That is normal and it is not yours to adjudicate.
Collect the conflicts and ask. If Rafael is unavailable, write both versions into the
concept under a `> [!warning] Conflicting sources` block rather than picking one.

### 3. Convert

For each concept:

- Follow the **okf-authoring** skill for structure.
- Set provenance honestly:

```yaml
generated: { by: process:okf-import, at: <now> }
sources:
  - resource: "https://docs.google.com/document/d/abc123"
    title: "Valmorian world bible v3"
    author: "human:rafael"
    last_modified: 2026-03-02
```

- Set `status: draft` on everything imported. Rafael promotes to `stable` after review.
- **Keep the source language.** Notes in Portuguese produce concepts in Portuguese.
  Quotations that are in English — a spell name, a rule from the book — stay in English
  with Portuguese around them.
- **Preserve his wording.** Import is not an editing pass, and it is not a translation
  pass either. Restructure into the codex's
  headings, but keep his sentences. If a passage is genuinely unusable, keep it verbatim
  in a `> [!note] From the original notes` block rather than paraphrasing it away.

### 4. Assign visibility carefully

Old notes rarely mark secrets. Defaulting everything to `secret` is safe but makes the
field useless; defaulting to `public` risks a spoiler in a handout. So:

- If the source clearly indicates player knowledge, use it.
- Otherwise set `visibility: secret` and **flag it in the manifest** as needing a pass.
- Never guess `public`.

### 5. Reconcile the graph

After conversion:

- Convert every internal reference to an absolute OKF link.
- Update every directory `index.md`.
- Append an import entry to `codex/log.md` naming the source and date.
- `python3 scripts/okf_validate.py`
- `qmd update && qmd embed`

### 6. Report

Tell Rafael: what was created, what was skipped and why, what conflicts need his ruling,
and which concepts need a visibility pass. Be specific about what you could not do — a
silent gap in an import is a fact he will discover mid-session.
