---
description: Turn raw session notes into a Session Recap and propagate the consequences
argument-hint: "[notes, a file path, or nothing to be prompted]"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, Task
---

Write up the session that was just played.

Raw material: **$ARGUMENTS**

If nothing was provided, ask the GM for his notes — or offer to take a verbal account and
write from that. Do not proceed on guesses.

Delegate to the **session-scribe** subagent, which owns this workflow: it writes the
recap concept, then propagates consequences to NPCs (`last_seen`, `disposition`), threads
(`pressure`, clock ticks), faction clocks, the party hooks ledger, and the session index.

When it reports back, relay to the GM:

- The recap, in brief
- What changed elsewhere in the codex
- Anything a player established that is now recorded as canon
- Any contradiction the session created
- Who is overdue a personal beat

Then run `python3 scripts/okf_validate.py` and `qmd update`.
