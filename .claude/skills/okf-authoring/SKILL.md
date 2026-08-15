---
name: okf-authoring
description: Author or edit concepts in the Valmorian codex using Open Knowledge Format v0.2. Use whenever creating, editing, or restructuring any file under codex/ — NPCs, factions, locations, arcs, threads, sessions, items, rules, stat blocks — or when asked about frontmatter, concept types, secrecy tiers, or cross-linking in this repo.
allowed-tools: Bash(qmd:*), Bash(python3 scripts/*), Read, Write, Edit, Glob, Grep
---

# Authoring OKF concepts in the Valmorian codex

The normative spec is [docs/OKF-PROFILE.md](../../../docs/OKF-PROFILE.md). Read it if you
have not this session. This skill is the working procedure.

## Language

Prose in **pt-BR**. Field names, enum values, `type` values, directory names and callout
tags in English — the validator compares against fixed English lists. See
[docs/IDIOMA.md](../../../docs/IDIOMA.md) and the pt-BR D&D 2024 glossary in
[docs/GLOSSARIO-DND-2024.md](../../../docs/GLOSSARIO-DND-2024.md).

`description` is prose, so it is Portuguese too, even though it sits in the frontmatter.

## Before writing anything

1. **Search for an existing concept.** `qmd query "<subject>"`. Duplicates are the main
   failure mode of a growing codex.
2. **Check the arc.** Read [codex/arcs/index.md](../../../codex/arcs/index.md). New
   material should press one of the three questions, or you should say why it does not.
3. **Decide the type** from the table in the profile, §3. The type determines the
   directory.

## Frontmatter

Every concept, minimum:

```yaml
---
type: NPC                    # required by spec, from the profile's type table
title: Aurélio Bastos        # required here — pt-BR, accents kept
description: Uma frase.      # required here — a summary, not a teaser
visibility: public           # required here — public | rumored | secret
status: draft                # required here — draft | stable | deprecated
lang: pt-BR                  # optional; defaults to the bundle value
tags: [npc, mansão]
generated: { by: claude-opus-5/gm-companion, at: 2026-08-15T21:48:00Z }
---
```

Add the type-specific extensions from profile §2.5 — `disposition` and `last_seen` on an
NPC, `pressure` and `arc` on a thread, `session_number` and `pcs` on a session, and so on.

Use a real current UTC timestamp in `generated.at`. Do not copy one from another file.

## Secrecy

- Set `visibility` to what the **party** knows, not what is dramatic.
- `public` — they know it or could trivially learn it.
- `rumored` — they have heard a version. Record the *distortion* in the body; a rumour
  that is merely an incomplete truth is a wasted opportunity.
- `secret` — they do not know.
- For a public concept hiding one twist, keep it `public` and wrap the twist:

```markdown
> [!secret]
> The thing the players must not read.
```

Visibility is a ceiling; an inline secret block lowers it locally.

## Linking

Absolute from the bundle root: `[Aurélio Bastos](/npcs/aurelio-bastos.md)` →
`codex/npcs/aurelio-bastos.md`. Filenames are ASCII (no accents); titles keep theirs.

Link on first mention, once. Link to concepts that do not exist yet — the validator
reports them as stubs to write, which is a useful to-do list.

## Body structure by type

Lead with the usable thing. Concretely:

| Type | Opens with | Never opens with |
|------|-----------|------------------|
| NPC | Voice, tell, want, lever | Ancestry, childhood |
| Faction | What the party thinks, then what is true | Founding history |
| Settlement | Read-aloud first impression, three noticed things | Population figures |
| Story Arc | What it is about, the turn, the default outcome | A scene list |
| Plot Thread | The question, who wants which answer, the clock | Backstory |
| Session Plan | "The one thing", then beats with cut markers | A rigid scene sequence |
| Session Recap | What happened, what players latched onto | Your own performance notes |
| Stat Block | Basis block + deltas, then how to play it | A full re-typed statblock |

Callouts in use: `> [!read-aloud]`, `> [!secret]`, `> [!note]`, `> [!warning]`.

## Every faction, thread, and arc states its default

What happens if the party does nothing? If you cannot answer, the concept is not
finished. This is the single highest-value field in the whole codex.

## After writing

1. Add a row to the directory's `index.md`. Always.
2. If it is structurally significant — new arc, resolved thread, retcon, bulk import —
   append to [codex/log.md](../../../codex/log.md).
3. `python3 scripts/okf_validate.py`
4. `qmd update` to re-index, then `qmd embed` if you added a lot.

## What not to do

- Do not invent canon and present it as established. Mark new material `status: draft`
  and say out loud that you made it up.
- Do not write a `verified` entry. Only Rafael verifies.
- Do not rewrite existing prose into your own voice while making an unrelated edit.
- Do not create a concept for something with no story consequence. A generic tavern does
  not need a file.
