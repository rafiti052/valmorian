---
description: Forge a table-ready NPC and wire them into the codex
argument-hint: "<name, role, or brief — e.g. 'harbourmaster who fears the Choir'>"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, Task
---

Create an NPC: **$ARGUMENTS**

First, search the codex — `qmd query` — for an existing character who fits. If one does,
say so and ask whether to use them instead. Reusing an NPC the party already knows is
almost always the stronger choice.

Otherwise delegate to the **npc-smith** subagent. It produces voice, want, and lever
first; truth, relationships, read-aloud line, and stat block after.

Relay the result and state plainly which parts were invented. Everything created is
`status: draft` until the GM says otherwise.
