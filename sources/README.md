# sources/

Raw campaign material, as Rafael wrote it. **This is provenance, not canon.**

Canon lives in [`codex/`](../codex/index.md). Everything here is the *input* that canon
was derived from, kept permanently so that any concept can point back at where it came
from and that link still resolves a year later.

## The workflow

1. Drop material in here — any structure you like, subfolders welcome.
2. Commit and push.
3. Run `/import`, or just say "ingest the new sources".
4. The companion surveys **everything** first, shows you a manifest, and waits for your
   go before writing a single concept.
5. Converted concepts land in `codex/` with a `sources:` frontmatter entry pointing back
   at the file here.

## What to put here

Anything. Session notes in whatever state they are in, world bible drafts, name lists,
half-finished NPC sketches, maps, a wall of text you dictated in the car. The messier it
is the more useful the survey step is.

Formats that work directly: `.md`, `.txt`, `.json`, `.csv`, `.pdf`, images.
For Google Docs or Notion pages you do not need to export — the companion can read those
connectors directly; just paste the link.

## Why this is committed and `inbox/` was not

The original scaffold had a gitignored `inbox/`. That was wrong for this setup: the repo
is the only channel between your machine and the companion's, so a staging directory that
git ignores is a staging directory the companion can never see.

Keeping `sources/` tracked also means `sources[].resource` links in the codex point at a
real file that stays put, which is the whole reason the OKF provenance fields exist.

## The one rule

**Never edit `sources/` to fix canon.** If a concept is wrong, fix the concept in
`codex/`. These files are a record of what you originally wrote; rewriting them destroys
the audit trail that makes "did I decide this or did the agent?" answerable.

Superseded material is fine to leave here. It is not competing with canon — the validator
only reads `codex/`, and search results from this collection are labelled `sources`.
