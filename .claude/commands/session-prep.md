---
description: Plan the next session from live threads, faction clocks, and party hooks
argument-hint: "[optional focus, e.g. 'lean on the archive' or 'short session']"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, Task
---

Prep the next Valmorian session. Focus from the GM, if any: **$ARGUMENTS**

Work through this in order. Do not skip to writing the plan.

1. **Orient.** Read the most recent session recap in `codex/sessions/` (just the latest).
   Read `codex/arcs/index.md`.
2. **Find the pressure.** Read `codex/threads/index.md`. Anything `urgent` is the session
   spine; `simmering` is B-plot material.
3. **Check the debts.** Read the hooks ledger in `codex/party/index.md`. Whoever has gone
   longest without a personal beat gets one this session. Say who and why.
4. **Advance the world.** Check faction clocks in `codex/factions/`. Decide what moved
   off-screen since last session.
5. **Search for reincorporation.** `qmd query` the recaps for something the party has
   already seen that could pay off now. Reusing beats the party remembers is always
   stronger than new material.

Then write `codex/sessions/session-NN-plan.md` following the **okf-authoring** skill,
with:

- **The one thing** — if only one thing happens tonight, what is it?
- **Opening** — a specific scene, starting *after* the boring part.
- **Beats** — a table with a purpose column and a "cut if short on time" column.
- **Personal beat owed** — to the PC identified in step 3.
- **Prepared, not planned** — stat blocks, a name list, anything to have at hand.
- **If the party goes sideways** — the two facts that must land by any route.

Set `stale_after` about a month out.

Finally: tell the GM what you decided and why, flag anything you invented, and list what
he still needs to decide before play. Do not present the plan as finished if it rests on
an open question.
