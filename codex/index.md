---
okf_version: "0.2"
type: Campaign
title: Valmorian
description: GM knowledge base and planning companion for the Valmorian campaign, running D&D 5e (2024 rules).
visibility: secret
status: draft
tags: [campaign, dnd-5e-2024, gm-only]
generated: { by: claude-opus-5/gm-companion, at: 2026-08-15T19:20:00Z }
---

# Valmorian

The bundle root for the Valmorian campaign codex. Everything here is **GM-only**.

> [!warning]
> This whole bundle is written from the GM's side of the screen. Do not share the repo,
> a directory listing, or a rendered view of it with players. Player-facing material is
> generated on demand by filtering on `visibility` — see
> [the OKF profile](../docs/OKF-PROFILE.md#4-secrecy-model).

## System

D&D 5e, **2024 rules**. Species not race; backgrounds grant feats; weapon mastery is in
play. House rulings that diverge from RAW live in [/rules](/rules/index.md) and are the
final word when they conflict with the books.

## How this bundle is organised

| Directory | What lives there |
|-----------|------------------|
| [world/](/world/index.md) | Cosmology, calendar, history, the themes the campaign is *about*. |
| [arcs/](/arcs/index.md) | The long-term narrative skeleton. Start here when you feel lost. |
| [threads/](/threads/index.md) | Live plot threads and their pressure. What is about to happen *to* the party. |
| [factions/](/factions/index.md) | Organisations with goals, clocks, and opinions about the party. |
| [npcs/](/npcs/index.md) | Named characters. |
| [locations/](/locations/index.md) | Regions, settlements, sites. |
| [sessions/](/sessions/index.md) | Plans for what is next, recaps of what happened. |
| [party/](/party/index.md) | The PCs, their bonds, and the hooks you owe each of them. |
| [items/](/items/index.md) | Artifacts and notable loot. |
| [rules/](/rules/index.md) | House rules and table rulings. |
| [bestiary/](/bestiary/index.md) | Homebrew and reskinned stat blocks. |

## Working here

Ask the companion for what you need rather than opening files by hand:

```
/session-prep          plan the next session from live threads and party hooks
/recap                 turn raw session notes into a Session Recap concept
/npc <name or brief>   forge an NPC and wire them into the graph
/canon-check           find contradictions, dangling links, and forgotten threads
/thread                open, advance, or resolve a plot thread
/import <path>         convert raw notes in inbox/ into OKF concepts
```

## Status

This is a **scaffold**. The concepts below are worked examples showing the shape of each
type — coherent enough to demonstrate cross-linking, but not your campaign. Replace them
as you import real material. Every example carries `status: draft` and the tag
`scaffold-example`, so `/canon-check` can list what is still placeholder.
