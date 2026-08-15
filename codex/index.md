---
okf_version: "0.2"
type: Campaign
title: Mansão Valmorian
description: Base de conhecimento e companheiro de planejamento do mestre para a campanha Mansão Valmorian, em D&D 5e (regras de 2024).
visibility: secret
status: draft
lang: pt-BR
tags: [campanha, dnd-5e-2024, apenas-mestre]
generated: { by: claude-opus-5/gm-companion, at: 2026-08-15T21:40:00Z }
---

# Mansão Valmorian

Raiz do bundle do codex da campanha. Tudo aqui é **apenas para o mestre**.

> [!warning]
> Este bundle inteiro é escrito do lado do mestre da tela. Não compartilhe o repositório,
> uma listagem de diretórios, nem uma visualização renderizada dele com os jogadores.
> Material para jogadores é gerado sob demanda filtrando por `visibility` — veja
> [o perfil OKF](../docs/OKF-PROFILE.md#4-secrecy-model).

## Sistema e idioma

D&D 5e, **regras de 2024**. A prosa do codex é em **pt-BR**; nomes de campos, valores de
enum e nomes de diretórios ficam em inglês porque o validador compara com listas fixas —
veja [docs/IDIOMA.md](../docs/IDIOMA.md).

Terminologia em [docs/GLOSSARIO-DND-2024.md](../docs/GLOSSARIO-DND-2024.md): *espécie*,
*antecedente*, *maestria*. Regras da casa em [/rules](/rules/index.md) têm precedência
sobre o livro.

## Como o bundle está organizado

| Diretório | O que vive lá |
|-----------|---------------|
| [world/](/world/index.md) | Cosmologia, calendário, história, os temas de que a campanha *trata*. |
| [arcs/](/arcs/index.md) | O esqueleto narrativo de longo prazo. Comece aqui quando se sentir perdido. |
| [threads/](/threads/index.md) | Fios de trama vivos e sua pressão. O que está prestes a acontecer *com* o grupo. |
| [factions/](/factions/index.md) | Organizações com objetivos, relógios e opinião sobre o grupo. |
| [npcs/](/npcs/index.md) | Personagens nomeados. |
| [locations/](/locations/index.md) | Regiões, assentamentos, locais. |
| [sessions/](/sessions/index.md) | Planos do que vem e resumos do que aconteceu. |
| [party/](/party/index.md) | Os PJs, seus laços, e os ganchos que você deve a cada um. |
| [items/](/items/index.md) | Artefatos e tesouro notável. |
| [rules/](/rules/index.md) | Regras da casa e decisões de mesa. |
| [bestiary/](/bestiary/index.md) | Blocos de estatísticas caseiros e reskins. |

## Trabalhando aqui

Peça ao companheiro o que você precisa em vez de abrir arquivos na mão:

```
/session-prep          planeja a próxima sessão a partir dos fios vivos e ganchos do grupo
/recap                 transforma notas cruas de sessão em um conceito Session Recap
/npc <nome ou resumo>  forja um NPC e o conecta ao grafo
/canon-check           acha contradições, links quebrados e fios esquecidos
/thread                abre, avança ou resolve um fio de trama
/import <caminho>      converte material cru de sources/ em conceitos OKF
```

## Status

Isto é um **scaffold**. Os conceitos abaixo são exemplos de trabalho que mostram o formato
de cada tipo — coerentes o bastante para demonstrar os links cruzados, mas **não são a sua
campanha**. Eu inventei todos eles. Substitua conforme importar material real.

Todo exemplo tem `status: draft` e a tag `scaffold-example`:

```bash
grep -rl "scaffold-example" codex/
```
