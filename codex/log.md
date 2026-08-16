---
type: Change Log
title: Registro de Mudanças
description: Registro cronológico das mudanças significativas no codex da Mansão Valmorian.
visibility: secret
status: stable
lang: pt-BR
generated: { by: gpt-5/codex, at: 2026-08-16T03:55:46Z }
---

# Registro de Mudanças

Mais recente primeiro. Os agentes registram aqui quando fazem uma mudança estrutural — um
arco novo, um fio resolvido, um retcon, uma importação em lote. Edições rotineiras de
conceito não precisam de entrada; o git já tem essas. Este log é para as mudanças que você
gostaria de *narrar* para si mesmo daqui a seis meses.

Formato: `## AAAA-MM-DD — resumo`, depois bullets, cada um linkando os conceitos tocados.

---

## 2026-08-15 — Primeiro lote estrutural do manifesto aprovado

- Conceitos de origem de Líria: [Lagoa Nymrath](/locations/lagoa-nymrath.md),
  [Marea](/npcs/marea.md), [M. Valmorian](/npcs/m-valmorian.md) e
  [Selo da Lua Refletida](/world/selo-da-lua-refletida.md).
- Lacunas ligadas à mansão: [Chef Espectral](/npcs/chef-espectral.md) e
  [Valthar](/npcs/valthar.md), sem resolver suas identidades ou destinos.
- Princípio de preparação [O que não se revela cedo demais](/sessions/o-que-nao-se-revela.md)
  registrado a partir do handover.

## 2026-08-15 — Idioma definido como pt-BR; exemplos retematizados

- Prosa do codex passa a ser em português. Identificadores estruturais seguem em inglês —
  ver [docs/IDIOMA.md](../docs/IDIOMA.md) para o porquê.
- Glossário D&D 2024 pt-BR em [docs/GLOSSARIO-DND-2024.md](../docs/GLOSSARIO-DND-2024.md),
  separando termos confirmados dos que ainda preciso confirmar.
- Exemplos de scaffold retematizados de uma cidade portuária para uma mansão, já que a
  campanha se chama Mansão Valmorian. Continuam sendo material inventado e descartável.

## 2026-08-15 — `inbox/` substituído por `sources/`

- `inbox/` era gitignored, o que impedia qualquer material de chegar ao companheiro.
- `sources/` é versionado de propósito: é o canal de entrega e o alvo permanente dos links
  `sources[].resource`.

## 2026-08-15 — Codex inicializado

- Scaffold criado sobre [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).
- Nenhum material real da campanha importado ainda.
