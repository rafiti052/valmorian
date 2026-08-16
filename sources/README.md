# sources/

Raw campaign material, as Rafael wrote it. **This is provenance, not canon.**

Canon lives in [`codex/`](../codex/index.md). Everything here is the *input* that canon
was derived from. Campaign-authored material cleared for this public repository is kept
in Git. Private player files, commercial books, licensed art, and material without
confirmed publication rights stay at the same local paths but are ignored by Git.

## The workflow

1. Drop material in here — any structure you like, subfolders welcome.
2. Run `/import`, or just say "ingest the new sources".
3. The companion surveys **everything** first and records each file's publication rights
   in the ingestion manifest.
4. For a campaign-authored file explicitly cleared for publication, stage only that path
   (`git add -- sources/nome-exato.md`) and then commit and push. **Never run
   `git add sources/` or `git add .` to publish source material.** Local-only files remain
   untracked and must not be pushed.
5. The companion shows you the manifest and waits for your
   go before writing a single concept.
6. Converted concepts land in `codex/` with a `sources:` frontmatter entry pointing back
   at the file here.

## What to put here

Anything can be used locally: session notes in whatever state they are in, world bible
drafts, name lists, half-finished NPC sketches, maps, a wall of text you dictated in the
car. The messier it is the more useful the survey step is. Putting a file here does not
authorize publishing it.

Formats that work directly: `.md`, `.txt`, `.json`, `.csv`, `.pdf`, images.
For Google Docs or Notion pages you do not need to export — the companion can read those
connectors directly; just paste the link.

## Why some of this is committed and `inbox/` was not

The original scaffold had a gitignored `inbox/`. That was wrong for this setup: the repo
is the durable channel for campaign-authored sources that Rafael has explicitly cleared
for publication.

Keeping cleared files tracked means their `sources[].resource` links resolve in every
clone. A local-only link resolves only on a machine that holds the private asset; its
manifest entry, exact path, hash, and coverage preserve the audit trail without publishing
the asset.

Before committing, run `git status --short` and `git check-ignore -v -- <source-path>`.
An asset classified as local-only must be ignored. If it is not, update `.gitignore`
before staging anything.

## The one rule

**Never edit `sources/` to fix canon.** If a concept is wrong, fix the concept in
`codex/`. These files are a record of what you originally wrote; rewriting them destroys
the audit trail that makes "did I decide this or did the agent?" answerable.

Superseded material is fine to leave here. It is not competing with canon — the validator
only reads `codex/`, and search results from this collection are labelled `sources`.
