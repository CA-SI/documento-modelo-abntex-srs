# Modelo SRS modular em português

## Objetivo

Adaptar o modelo herdado de `jpeisenbarth/SRS-Tex` para a comunidade de
Sistemas de Informação da UFV-CRP, com apresentação abnTeX2, conteúdo didático
em português e requisitos rastreáveis. O nome do repositório deve corresponder
à classe efetivamente usada.

## Requisitos e critérios de aceite

- Manter `srs.tex` como entrada, separando metadados, configuração e conteúdo.
- Incluir introdução, descrição geral, interfaces, funcionalidades, requisitos
  não funcionais, regras de negócio, glossário e rastreabilidade.
- Demonstrar requisitos com identificadores estáveis, prioridade, origem,
  enunciado e critério de aceite; ligar exemplos a casos de teste.
- Usar abnTeX2, português brasileiro, capa, folha de rosto, sumário,
  referências e apêndices com referências internas resolvidas.
- Não incluir pendências editoriais ou afirmações de aprovação no PDF.
- Gerar `build/srs.pdf` com `make`, verificar o documento com `make check`
  e limitar a limpeza aos artefatos deste modelo.
- Documentar instalação, edição, estrutura, limites normativos, licença,
  créditos, comparação dos forks e links para artigo e perfil da CA-SI.
- Compilar e verificar em CI, disponibilizando o PDF como artefato.
- Preservar a GPL-3.0-or-later e a atribuição do modelo original.

## Fora de escopo

Certificação de conformidade ABNT/IEEE/ISO; implementação de um software real;
alterações no artigo e no pacote de estilo UFV; escolha entre edições de normas
bibliográficas; mudanças no perfil da organização (domínio de `CA-SI/.github`).
