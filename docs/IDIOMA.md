# Idioma do codex

**A prosa do codex é escrita em português (pt-BR).** É o idioma em que Rafael mestra, e
este material é lido durante a preparação e na mesa.

## O que fica em inglês, e por quê

Identificadores estruturais permanecem em inglês:

| Fica em inglês | Exemplo | Motivo |
|----------------|---------|--------|
| Nomes de campos do frontmatter | `title`, `visibility`, `status` | O validador e a spec OKF indexam por esses nomes. |
| Valores de enum | `secret`, `draft`, `urgent`, `friendly` | Mesmos motivos — `scripts/okf_validate.py` compara com listas fixas. |
| Valores de `type` | `NPC`, `Faction`, `Story Arc` | Fazem parte do perfil OKF e definem o diretório válido. |
| Nomes de diretórios | `npcs/`, `factions/` | Fazem parte dos links absolutos do bundle. Renomear quebra o grafo inteiro. |
| Callouts | `> [!secret]`, `> [!read-aloud]` | Reconhecidos pelo validador e por qualquer renderizador de markdown. |

Este é o padrão normal de internacionalização: **código em inglês, conteúdo no idioma do
usuário**. Um schema bilíngue é uma fonte inesgotável de bugs — `visibilidade: secreto`
não seria validado, e o erro só apareceria quando alguém exportasse um material para os
jogadores com um segredo dentro.

## O que fica em português

Tudo que é lido por um humano: títulos, descrições, corpo dos conceitos, tabelas,
blocos de leitura em voz alta, nomes próprios, e as entradas do `codex/log.md`.

O campo `description` é português, mesmo sendo tecnicamente metadado — é o que a busca
retorna e o que você lê primeiro.

## Nomes de arquivo sem acento

Nomes de arquivo são ASCII: `mansao-valmorian.md`, `sessao-01.md`,
`quem-deu-a-ultima-ordem.md`. O `title` no frontmatter mantém os acentos — só o caminho é
despido.

Além da portabilidade entre sistemas de arquivos, isso é o que faz `qmd search mansao`
encontrar o conceito quando você digita sem acento no meio da sessão. Testado: a busca
acentuada funciona normalmente, e a versão sem acento só acha o documento porque o nome do
arquivo é ASCII.

## Campo `lang`

Conceitos podem declarar `lang: pt-BR`. O padrão do bundle está em `codex/index.md`, então
só vale a pena declarar em um conceito específico quando ele foge do padrão — por exemplo,
uma transcrição de sessão que ficou em inglês, ou um bloco de regras copiado do livro
original.

## Material importado

O idioma da fonte manda. Se as notas em `sources/` estão em português, o conceito sai em
português; se um trecho está em inglês e é uma citação (uma regra do livro, o nome de uma
magia), mantenha o original e traduza ao redor.

**Não traduza a voz do Rafael.** Importação não é passe de edição. Se uma frase dele está
em português coloquial, ela continua em português coloquial.
