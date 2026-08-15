---
description: Audit the codex for contradictions, secrecy leaks, forgotten threads, and broken links
argument-hint: "[optional scope, e.g. 'the Choir' or 'sessions 1-4']"
allowed-tools: Bash, Read, Glob, Grep, Task
---

Audit the Valmorian codex. Scope, if given: **$ARGUMENTS**

Delegate to the **lore-keeper** subagent. It is read-only by design — it reports, the GM
decides.

It will run `python3 scripts/okf_validate.py`, search for name variants and near-spellings,
retrieve full documents rather than concluding from snippets, and check frontmatter state
against prose.

Relay its findings ranked by table impact: hard contradictions first, then secrecy leaks,
then broken state, then forgotten threads, then dangling links (which are usually stubs to
write, not errors), then stale concepts.

For each finding, offer the cheapest fix. Apply fixes only if the GM asks.

If the codex is clean, say so in one sentence. Do not pad an audit with manufactured
findings.
