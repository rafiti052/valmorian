# Valmorian OKF Profile

This repository is an **Open Knowledge Format (OKF) v0.2** bundle. This document is the
normative profile: it says which concept `type` values Valmorian uses, which frontmatter
fields are required beyond the base spec, and how secrecy is modelled.

Upstream spec: <https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>

The base spec is deliberately minimal — `type` is the *only* required field, there is no
schema registry, and cross-file markdown links form the knowledge graph. This profile adds
constraints on top. Everything here is additive; a Valmorian concept is always a valid OKF
concept, so any OKF-aware agent can read this bundle without knowing this profile exists.

---

## 1. Bundle layout

The bundle root is `codex/`. Absolute links are resolved **relative to the bundle root**,
not the repo root: `/npcs/aurelio-bastos.md` means `codex/npcs/aurelio-bastos.md`.

```
codex/
  index.md              # RESERVED - bundle manifest, declares okf_version
  log.md                # RESERVED - chronological change history
  world/                # cosmology, calendar, history, themes
  npcs/                 # individual characters
  factions/             # organisations, cults, houses, guilds
  locations/            # regions, settlements, sites
  arcs/                 # long-term narrative arcs (the campaign skeleton)
  threads/              # live plot threads, seeded and dangling
  sessions/             # session plans and recaps
  party/                # player characters and party-level state
  items/                # artifacts, boons, notable loot
  rules/                # house rules and rulings made at the table
  bestiary/             # homebrew and reskinned stat blocks
```

`index.md` and `log.md` are the only reserved filenames, per spec. Subdirectories may
contain their own `index.md` as a directory listing.

Filenames are `kebab-case.md`, derived from the concept title, and **ASCII only** — strip
accents and cedillas: `mansao-valmorian.md`, not `mansão-valmorian.md`; `sessao-01.md`, not
`sessão-01.md`.

Two reasons. Paths appear in absolute links across the whole bundle, and an accented path is
a portability hazard across filesystems. More practically: QMD indexes filenames, so an
ASCII filename is what lets `qmd search mansao` find the concept when you type without
accents — which you will, mid-session, in a hurry. Titles in the frontmatter keep their
accents; only the path is stripped.

Never rename a file without updating inbound links — `scripts/okf_validate.py` will catch
orphans.

---

## 2. Frontmatter

### 2.1 Required by the spec

| Field | Notes |
|-------|-------|
| `type` | Short descriptive string. Must be one of the values in §3. |

### 2.2 Required by this profile

| Field | Notes |
|-------|-------|
| `title` | Human-readable display name. |
| `description` | One sentence. This is what search returns and what an agent reads first — write it as a *summary*, not a teaser. |
| `visibility` | Secrecy tier. One of `public`, `rumored`, `secret`. See §4. |
| `status` | Lifecycle: `draft`, `stable`, `deprecated`. Spec-defined values. |

### 2.3 Language

Concept prose is **pt-BR**; frontmatter field names, enum values, `type` values, and
directory names stay English. Full rationale in [IDIOMA.md](IDIOMA.md).

Optional `lang` field, defaulting to the bundle value in `codex/index.md`. Only worth
setting on a concept that departs from the default.

### 2.4 Recommended

| Field | Notes |
|-------|-------|
| `tags` | YAML list. Lowercase kebab-case. |
| `generated` | `{ by: <actor>, at: <ISO 8601> }`. Set by agents on every meaningful write. |
| `sources` | Provenance for imported material. See §5. |
| `verified` | List of `{ by, at }` review events. Use when you confirm canon at the table. |
| `stale_after` | `YYYY-MM-DD`. Useful on session plans and volatile faction state. |
| `resource` | URI for the underlying asset — the Google Doc, the Notion page, the map image. |

### 2.5 Profile extensions

These are Valmorian-specific and carry no meaning to a generic OKF reader. That is fine and
expected; the spec explicitly allows producer-defined fields.

| Field | Applies to | Notes |
|-------|-----------|-------|
| `visibility` | all | See §4. |
| `arc` | threads, sessions, npcs | Link to the owning arc, e.g. `/arcs/o-inventario.md`. |
| `threads` | sessions, npcs, factions | List of links to live plot threads. |
| `first_appeared` | npcs, factions, locations, items | Link to the session concept where the party first encountered this. |
| `last_seen` | npcs | Link to the most recent session concept. |
| `disposition` | npcs, factions | Attitude toward the party: `hostile`, `wary`, `neutral`, `friendly`, `devoted`. |
| `session_number` | sessions | Integer. |
| `played_on` | sessions | `YYYY-MM-DD`. |
| `pcs` | sessions | List of links to party members present. |
| `pressure` | threads | `dormant`, `simmering`, `urgent`, `resolved`. How close this is to forcing itself onto the table. |
| `stat_block` | npcs, bestiary | Free-form 5e-2024 block, or a link to a bestiary concept. |
| `lang` | all | BCP-47 tag. Defaults to the bundle's `lang` in `codex/index.md`. |

---

## 3. Concept types

`type` values are not registered centrally, so these are ours. Keep them stable — search and
the validator both key off them.

| `type` | Directory | Purpose |
|--------|-----------|---------|
| `Campaign` | `/index.md` | The bundle manifest. Exactly one. |
| `World Concept` | `world/` | Cosmology, pantheon, calendar, magic laws, historical eras. |
| `NPC` | `npcs/` | A named character. |
| `Faction` | `factions/` | Any organisation with goals and a clock. |
| `Region` | `locations/` | Large geography. |
| `Settlement` | `locations/` | Cities, towns, villages. |
| `Site` | `locations/` | Dungeons, ruins, single buildings, encounter locations. |
| `Story Arc` | `arcs/` | A multi-session narrative movement. The long-term skeleton. |
| `Plot Thread` | `threads/` | A single live question or pressure. Shorter-lived than an arc. |
| `Session Plan` | `sessions/` | Prep for an upcoming session. |
| `Session Recap` | `sessions/` | What actually happened. |
| `Player Character` | `party/` | A PC, including their personal hooks and bonds. |
| `Item` | `items/` | Artifacts, boons, notable loot. |
| `House Rule` | `rules/` | A ruling made at or before the table. |
| `Stat Block` | `bestiary/` | Homebrew or reskinned creature. |

### 5e 2024 terminology

This campaign runs **D&D 5e (2024 rules)**, and the codex is written in pt-BR. Use the
2024 Portuguese vocabulary: *espécie* (não raça), *antecedente* como pacote mecânico que
concede talento, *maestria* de armas, e as definições de condição e exaustão de 2024.

The vetted term list is [GLOSSARIO-DND-2024.md](GLOSSARIO-DND-2024.md). Terms in its
"a confirmar" section are unverified translations — flag them, do not assert them. When a
stat block is adapted from a 2014 source, say so in `sources`.

---

## 4. Secrecy model

This is a **GM-only repository**. Nothing here is safe to screen-share as-is. The
`visibility` field exists so that a future export can filter, and so an agent knows what it
may put in a player-facing handout.

| Tier | Meaning |
|------|---------|
| `public` | The party knows this, or would learn it by asking any tavern keeper. Safe to export to a player wiki. |
| `rumored` | The party has heard a version of this. Possibly a *wrong* version — record the distortion in the body. |
| `secret` | The party does not know this. Never export. |

Concept-level `visibility` is coarse. For a mostly-public concept that hides one twist, keep
`visibility: public` and mark the twist inline:

```markdown
> [!secret]
> Aurélio já morreu no incêndio. O que serve o chá responde
> [à Criadagem](/factions/a-criadagem.md).
```

Any agent generating player-facing material MUST strip `> [!secret]` blocks and MUST skip
concepts with `visibility: secret` entirely. The rule is: **a concept's visibility is a
ceiling, and an inline secret block lowers it locally.**

---

## 5. Provenance

Every concept records where it came from. This matters most for imported material, where
"did I write this or did the agent?" becomes unanswerable within a month.

Actor strings follow the spec convention:

- `human:rafael` — you, at the keyboard
- `claude-opus-5/gm-companion` — an agent in this repo
- `process:okf-import` — the import pipeline

```yaml
generated: { by: claude-opus-5/gm-companion, at: 2026-08-15T19:30:00Z }
sources:
  - resource: "https://docs.google.com/document/d/abc123"
    title: "Valmorian session zero notes"
    author: "human:rafael"
    last_modified: 2026-03-02
verified:
  - { by: "human:rafael", at: 2026-08-15T20:00:00Z }
```

`generated` supersedes any `timestamp` field from OKF v0.1. Do not use `timestamp`.

**Agents must not add a `verified` entry on their own behalf.** Verification means a human
confirmed it. An agent writing `verified: [{by: claude..., ...}]` is laundering its own
output into canon.

---

## 6. Linking

Cross-links are the graph. Two forms, per spec:

- **Absolute (preferred):** `[Aurélio Bastos](/npcs/aurelio-bastos.md)` — resolved from `codex/`.
- **Relative:** `[A Criadagem](../factions/a-criadagem.md)` — only within a tight cluster.

Link on first mention of any concept that has its own file. Do not link the same concept
five times in one document; once, at the top, is enough.

If you mention something that *should* have a file and does not, link it anyway and let the
validator flag it as a stub to write. A broken link is a to-do, not an error.

---

## 7. Writing style for concepts

The body is for a GM at the table under time pressure. That shapes everything:

- **Lead with the usable thing.** An NPC concept opens with how they talk and what they
  want, not with their grandfather's mercantile career.
- **Bullets over paragraphs** for anything you would scan mid-session.
- **Prose for the parts you would read aloud**, marked with `> [!read-aloud]`.
- **State the pressure.** Every faction and thread answers: what happens if the party does
  nothing? A campaign world that only moves when poked is not a world.
- **No stat block padding.** If it is a standard 2024 monster, name it and link the bestiary.
  Only write a block out when it is genuinely custom.
