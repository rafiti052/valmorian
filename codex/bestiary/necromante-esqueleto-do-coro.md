---
type: Stat Block
title: Necromante-Esqueleto do Coro
description: Morto-vivo cantor da cripta sob a igreja; desmonta ao cair e se remonta no turno seguinte, e só para de verdade com dano radiante ou com a fenda estabilizada.
visibility: secret
status: draft
lang: pt-BR
tags: [bestiário, morto-vivo, cripta, dnd-5e-2024, inventado]
sources:
  - resource: "/sources/sessao_3_estrutura_narrativa.md"
    title: "Sessão 3 — Estrutura Narrativa (§7 Cripta)"
    author: "human:rafael"
    sha256: 64ec6159703e2ed63b139fef35603fccfe208e2c6fac74aee8d279e049bb73e8
    coverage: partial
    locator: "§7 Cripta"
generated: { by: gpt-5/codex, at: 2026-08-16T04:18:13Z }
---

# Necromante-Esqueleto do Coro

> [!warning]
> **Bloco inventado por mim.** A sua fonte enuncia três coisas — *"desmontam ao cair, se
> remontam depois de um turno"*, *"se 3 ou mais estiverem ativos, o coro remonta um dos seis
> por ação bônus conjunta"* e *"são seis"* — e nada mais. Números, ataques e a regra do
> radiante são meus. Nada aqui é canon até você usar na mesa.

Seis deles. Não são guardas da cripta: são o que sobrou de quem cantava nela. Continuam
cantando. É por isso que a igreja soa errada antes de qualquer um entender o porquê.

| | |
|---|---|
| **Tamanho/Tipo** | Médio morto-vivo |
| **CA** | 13 (ossos e paramentos endurecidos) |
| **PV** | 22 (5d8) |
| **Deslocamento** | 30 pés |
| **ND** | 1 (200 XP) |
| **Bônus de proficiência** | +2 |

**FOR** 12 (+1) · **DES** 14 (+2) · **CON** 14 (+2) · **INT** 10 (+0) · **SAB** 12 (+1) · **CAR** 8 (−1)

- **Testes de resistência:** **sem proficiência em nenhum** — use os modificadores acima direto.
  É o que você vai consultar toda vez que alguém conjurar alguma coisa.
- **Vulnerabilidade a dano:** concussão
- **Imunidade a dano:** veneno
- **Imunidade a condição:** envenenado, exausto
- **Sentidos:** visão no escuro 60 pés, Percepção passiva 11 · **Iniciativa:** +2
- **Idiomas:** entende Comum e a língua litúrgica da cripta, mas só canta

> [!note]
> **Iniciativa:** role **uma** para os quatro da nave e **outra** para os dois da escada, que
> entram na rodada 3. Seis iniciativas separadas transformam o combate numa fila.

## Traços

**Desmontar.** Quando cai a 0 pontos de vida, ele **não é destruído**. Desaba numa pilha de
ossos e paramentos no espaço dele. No **início do próximo turno dele**, remonta em pé, no
mesmo espaço, com **11 pontos de vida** — e perde aquele turno inteiro.

**O Coro.** Na contagem de iniciativa do primeiro esqueleto ainda ativo, se **3 ou mais**
estiverem de pé, o coro gasta a **ação bônus coletiva** e **uma pilha remonta imediatamente
com 11 PV**. Uma vez por rodada. Com dois ou menos de pé, o canto se desfaz e isso deixa de
funcionar. Não alcança pilha já destruída de vez.

**Fim verdadeiro.** Uma pilha para de remontar de vez se sofrer **dano radiante** — ou se a
fenda na [cripta](/locations/cripta.md) for estabilizada, o que derruba os seis de uma vez,
sem teste de resistência.

### A pilha, em regras

Isto é o que a mesa mais vai perguntar no meio da luta:

- Ocupa o espaço dela e conta como **terreno difícil** (+5 pés para atravessar).
- É **alvo inerte**: ataques contra ela **acertam automaticamente** e ela não faz
  testes de resistência.
- **Qualquer quantidade de dano radiante** destrói a pilha de vez. Não há limiar, não há
  teste de resistência. **1 ponto basta** — é por isso que a Rapieira de Prata da Yara resolve.
- Nada mais destrói uma pilha. Bater nela com dano físico não adianta, e a mesa precisa
  sentir isso uma vez.

### Segredo de condução

Essa é a regra que a mesa precisa descobrir, não que você precisa anunciar. Deixe as duas
primeiras rodadas serem só frustração. Detalhes de quando entregar estão no
[plano da sessão](/sessions/sessao-04-plano.md).

## Ações

**Cajado de Ossos.** *Ataque corpo a corpo:* **+4** para acertar, alcance 5 pés, um alvo.
*Acerto:* **5 (1d6+2) de concussão** mais **2 (1d4) de necrótico**.

**Verso Necrótico.** *Ataque mágico à distância:* **+3** para acertar, alcance 60 pés, um
alvo. *Acerto:* **5 (2d4) de necrótico**, e o alvo **não recupera pontos de vida** até o fim
do próximo turno dele.

## A brasa consagrada — a segunda via, com números

O braseiro tombado é o caminho de vitória que **não depende da Bri**, e é o que abre o
encontro. Ele precisava de mecânica; esta é invenção minha:

- **Tombar um braseiro:** ação de Usar um Objeto. Se estiver disputado, **Força (Atletismo)
  CD 10**. A [Enna](/party/enna.md) faz com **ação bônus** por Mãos Rápidas; a Língua do
  [Bob](/party/bob.md) derruba um a 15 pés.
- Cria um **quadrado de 5 pés de brasa consagrada**, que dura o resto do combate.
- Criatura que **entra** no quadrado pela primeira vez no turno, ou **termina o turno** nele:
  **1d6 de fogo**. Morto-vivo sofre **mais 1d6 radiante**.
- **Pilha que cai dentro de um quadrado de brasa é destruída de vez.** A brasa é radiante e
  não para de queimar.
- **Quantos braseiros:** quatro na nave, dois de cada lado do corredor central. *Número
  inventado agora* — a [igreja](/locations/igreja-de-lathander.md) não dizia quantos.

## As interações que a mesa vai forçar

Modificadores e CDs prontos, para você não parar a luta procurando:

| O que a mesa faz | Como resolve |
|---|---|
| **Empurrar um para a brasa** | Teste de resistência de **FOR +1** ou **DES +2** contra a CD de Empurrar de quem empurra (8 + FOR + PB, na ficha) |
| **Agarrar com a Língua do Bob** | Escapar: **Atletismo +1** ou **Acrobacia +2** contra a CD de agarrar do Bob |
| **Aquecer Metal** (Bob, CD 15) | Turíbulo e gola de metal. 2d8 de fogo, e teste de resistência de **CON +2** — na falha, desvantagem em ataques e testes. **Ele não consegue largar a gola**, então come o dano toda rodada |
| **Esconjurar Inimigo** (Bri, CD 13) | Teste de resistência de **SAB +1**. Amedrontado: deslocamento 0 e desvantagem. Um fugindo quebra o coro de 3 — é a jogada mais subestimada da mesa |
| **Sussurros Dissonantes** (Bob, CD 15) | Teste de resistência de **SAB +1** |
| **Divine Smite** (Bri) | +2d8 radiante **+1d8 contra morto-vivo**. Se sobrar radiante quando a pilha cair, ela não remonta |
| **Rapieira de Prata +1** (Yara) | +1 radiante. Um ponto é suficiente para matar uma pilha de vez |
| **Talhar** (maestria da Bri) | No acerto, um segundo ataque contra outro alvo a 5 pés do primeiro, 1×/turno. Contra seis em fileira, é muito — *confira o texto exato na ficha dela* |
| **Segurar Pessoa** (Líria) | **Não funciona.** Morto-vivo não é humanoide. Avise antes de ela gastar o espaço de 2º |
| **Orbe Cromático** (Líria) | Funciona, mas **ela não tem opção radiante** — derruba, não resolve |

## Notas de mesa

- **Vulnerabilidade a concussão** é do esqueleto padrão de 2024 e vale a pena lembrar: um
  banco arremessado, o desarmado do Aurélio, a **Língua do Bob** puxando um para a parede.
- **Vantagem da Yara** vale aqui: Inimigo Favorito (mortos-vivos) dá vantagem em testes de
  rastrear e conhecer. Uma pergunta dela sobre por que eles se levantam é resposta grátis.
- **Economia de ações:** seis contra cinco já é pesado. Por isso os PV são baixos. Não
  aumente — a pressão tem que vir da remontagem, não do saco de PV.

## Calibragem

Cinco PJs de nível 4. Orçamento de 2024: moderado 2.500 XP, alto 4.375 XP.

Seis criaturas de ND 1 = **1.200 XP** no papel. A remontagem quase dobra o custo efetivo,
o que põe o encontro perto do **moderado** — de propósito. Este combate não é para ser
vencido por atrito; é para ensinar que atrito não resolve.

## Os seis

Nomes rápidos, inventados agora, para quando a mesa perguntar quem eles eram: Dom Nesteu,
Irmã Valquina, o Cantor Sem Nome, Dom Ferrez, Irmã Odila, o Menino do Turíbulo.
