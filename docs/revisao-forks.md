# Revisão da origem, forks e modelo CA-SI

Consulta realizada em 11 de outubro de 2026, tomando o commit local
`423aa94` como base. A API do GitHub informa que este repositório é um fork de
`jpeisenbarth/SRS-Tex` e não possui forks diretos. Por isso, a comparação usa
a rede do projeto original.

## Método e limites

Foi consultada a lista paginada de forks da origem. Foram inspecionados os
comparativos da branch padrão da origem e de seis forks selecionados por
diferenças de tamanho ou datas de atualização: `FuhrmannMartin`, `capric98`,
`ddewaleffe`, `sebmaldo`, `jhlink` e `casch-at`. Esses sinais orientam a seleção;
não comprovam melhoria. A avaliação abaixo descreve somente os arquivos e
diferenças efetivamente consultados, sem afirmar revisão exaustiva de todas
as branches da rede.

Os links de comparação usam a base fixa e o nome da branch consultada; a branch
pode mudar após esta revisão.

## O que os comparativos mostram

| Fonte | Diferença observada | Decisão para este modelo |
|---|---|---|
| [Origem](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...master) | A branch padrão é idêntica à base local. | Não há atualização da origem a incorporar nessa comparação. |
| [FuhrmannMartin/SRS-FH-](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...FuhrmannMartin:master) | Seis commits adicionais; aplicação estudantil, diagramas de casos de uso, requisitos e tabelas; arquivos gerados versionados. | Adotar exemplos concretos e casos de uso; escrever um exemplo próprio e manter auxiliares fora do Git. |
| [capric98/SRS-Tex](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...capric98:master) | Onze commits adicionais; correções de formatação e bookmarks, histórico no sumário, paginação e suporte CJK. | Corrigir apresentação, metadados e links; não acrescentar dependências CJK ao modelo em português. |
| [ddewaleffe/SRS-Tex](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...ddewaleffe:master) | Ambientes de requisitos, rótulos, lista de requisitos e exemplos de controle de acesso; pacotes adicionais e auxiliares versionados. | Usar IDs estáveis, links e matriz de rastreabilidade com um comando local simples; não importar pacotes ou dados específicos dessa aplicação. |
| [sebmaldo/SRS-Tex](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...sebmaldo:master) | Sete commits adicionais; tradução para espanhol e ampliação do `.gitignore`. | Localizar integralmente para português e ignorar artefatos LaTeX. |
| [jhlink/SRS-Tex](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...jhlink:master) | Branch atrás da base, sem mudanças de arquivos no comparativo. | Nenhuma mudança de conteúdo a incorporar. |
| [casch-at/SRS-Tex](https://github.com/jpeisenbarth/SRS-Tex/compare/423aa94...casch-at:master) | Branch atrás da base, sem mudanças de arquivos no comparativo. | Nenhuma mudança de conteúdo a incorporar. |

## Relação com o artigo da CA-SI

O [artigo-modelo-abntex-ufv](https://github.com/CA-SI/artigo-modelo-abntex-ufv)
apresenta o pacote e os modelos de trabalhos acadêmicos mantidos em outro
repositório. Foram consultados seu README, Makefile, fonte do artigo e árvore
de arquivos. São práticas aproveitáveis: documentação em português, uso real
da classe abnTeX2, compilação por latexmk, saída em `build/`, especificações
em `docs/specs/` e separação entre texto e configuração.

Este SRS não copia o artigo nem o pacote `abntex2-UFV`, e não oferece sua escolha
de edições bibliográficas. O vínculo é documentado por links no README.

## Melhorias resultantes

- Classe abnTeX2 efetivamente usada, substituindo a classe `scrreprt` herdada.
- Metadados e apresentação separados de capítulos e apêndices em português.
- Exemplo fictício consistente, com sete requisitos, duas regras, casos de uso,
  critérios de aceite, modelo de estados e sete cenários de teste rastreáveis.
- Remoção da declaração automática de aprovação e da lista de pendências do PDF.
- Compilação gerenciada por latexmk, limpeza restrita ao modelo e verificação
  de marcadores, identificadores, rastreabilidade e problemas do log.
- Licença GPL e atribuições preservadas, sem inferir a licença de outros projetos.

As ideias foram reimplementadas neste repositório; os forks não foram mesclados.
