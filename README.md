# Valmorian

A GM companion for the Valmorian D&D campaign — a knowledge base for the world, the NPCs,
the factions and the sessions, plus a planning companion for the long-term narrative.

Built as an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
v0.2 bundle, searched with [QMD](https://github.com/tobi/qmd), and driven by Claude Code.

> **This repository is GM-only.** It contains the answers. Do not share it, or a rendered
> view of it, with players. See [the secrecy model](docs/OKF-PROFILE.md#4-secrecy-model).

**System:** D&D 5e, 2024 rules.

## Setup

```bash
npm install -g @tobilu/qmd     # requires Node >= 22 (or Bun >= 1.0)
qmd update                     # index the codex
qmd embed                      # optional: vector search (downloads ~1.9GB of models)
```

The `.qmd/index.yml` config is committed; the SQLite index is not — it rebuilds from the
markdown with `qmd update`.

Claude Code picks up `.mcp.json` automatically, exposing QMD search as MCP tools.

## Layout

| Path | What it is |
|------|-----------|
| `codex/` | The OKF bundle. All campaign canon. Bundle root for absolute links. |
| `docs/OKF-PROFILE.md` | The normative format spec for this repo — read before authoring. |
| `sources/` | Raw material as Rafael wrote it. Tracked, searchable, **not canon** — the provenance target for `sources:` links. |
| `scripts/okf_validate.py` | Conformance and link-graph validator. |
| `.claude/` | Skills, subagents, and slash commands. |

Inside `codex/`: `world/`, `arcs/`, `threads/`, `factions/`, `npcs/`, `locations/`,
`sessions/`, `party/`, `items/`, `rules/`, `bestiary/`.

Start at [`codex/arcs/index.md`](codex/arcs/index.md) — the narrative spine, and the
document to open when you have lost the plot.

## Commands

| Command | Does |
|---------|------|
| `/session-prep` | Plans the next session from live threads, faction clocks, and party hooks. |
| `/recap` | Turns raw session notes into a recap, then propagates the consequences. |
| `/npc` | Forges a table-ready NPC and wires them into the graph. |
| `/canon-check` | Audits for contradictions, secrecy leaks, forgotten threads, broken links. |
| `/thread` | Opens, advances, or resolves a plot thread. Also handles "I'm lost". |
| `/import` | Converts raw material in `sources/` into OKF concepts. |

Backed by four subagents: `lore-keeper` (continuity, read-only), `session-scribe`
(recaps), `npc-smith` (characters), `plot-weaver` (arcs and long-term shape).

## Searching

```bash
qmd search "Drowned Choir" -n 10        # fast BM25 keyword search
qmd query "who knows about the surfacings"   # hybrid + rerank (needs `qmd embed`)
qmd get codex/npcs/serath-vane.md       # read a full document
```

## Validating

```bash
python3 scripts/import_status.py          # what in sources/ is not yet ingested
python3 scripts/okf_validate.py           # 0 = clean, 1 = errors
python3 scripts/okf_validate.py --strict  # warnings count as failures
python3 scripts/okf_validate.py --json    # machine-readable
```

Checks required frontmatter, enum values, type/directory agreement, the cross-link graph,
directory indexes, provenance honesty (agents cannot self-`verify`), and secrecy leaks
where a `public` concept links a `secret` one outside a `> [!secret]` block.

## Scaffold status

The codex currently holds **worked examples**, tagged `scaffold-example` and marked
`status: draft`. They exist to show the shape of each concept type and to exercise the
cross-linking. Replace them as real material is imported:

```bash
grep -rl "scaffold-example" codex/
```
