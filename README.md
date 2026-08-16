# Valmorian

A GM companion for the **Mansão Valmorian** D&D campaign — a knowledge base for the world,
the NPCs, the factions and the sessions, plus a planning companion for the long-term
narrative.

O codex é escrito em **português (pt-BR)**. Identificadores estruturais (campos do
frontmatter, valores de enum, nomes de diretório) ficam em inglês — ver
[docs/IDIOMA.md](docs/IDIOMA.md).

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

## Battlemap hexagonal

O gerador da grade hexagonal requer Node 20.9 ou superior. Instale as dependências do
repositório e informe os caminhos de entrada e saída:

```bash
npm ci
npm run battlemap:hex -- caminho/entrada.png caminho/saida.png
```

## Layout

| Path | What it is |
|------|-----------|
| `codex/` | The OKF bundle. All campaign canon. Bundle root for absolute links. |
| `docs/OKF-PROFILE.md` | The normative format spec for this repo — read before authoring. |
| `docs/IDIOMA.md` | Language policy: pt-BR prose, English identifiers, ASCII filenames. |
| `docs/GLOSSARIO-DND-2024.md` | pt-BR D&D 2024 terminology, confirmed vs. unverified. |
| `sources/` | Raw material as Rafael wrote it. Tracked, searchable, **not canon** — the provenance target for `sources:` links. |
| `local-corpus/rulebooks/` | Gitignored full-text rulebook extraction for local QMD search; tracked metadata remains in `codex/rulebooks/`. |
| `scripts/okf_validate.py` | Conformance and link-graph validator. |
| `.claude/` | Skills, subagents, and slash commands. |

Inside `codex/`: `world/`, `arcs/`, `threads/`, `factions/`, `npcs/`, `locations/`,
`sessions/`, `party/`, `items/`, `rules/`, `bestiary/`, `rulebooks/`, `homebrew/`.

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
qmd search "criadagem última ordem" -n 10       # fast BM25 keyword search
qmd query "quem sabe do incêndio de 1897"       # hybrid + rerank (needs `qmd embed`)
qmd get codex/npcs/aurelio-bastos.md            # read a full document
```

Accented queries work. Unaccented ones match via the ASCII filename, which is why
filenames are stripped of accents.

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

## Import status

The fictional scaffold concepts have been removed. Real imported material remains
`status: draft` until Rafael reviews it. `scripts/import_status.py` reads the source-level
manifest and distinguishes full, partial, catalog-only, deferred, and pending sources.
