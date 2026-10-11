# Plano de implementação

## Estrutura e contratos

O documento segue: introdução → contexto → regras e dados → interfaces → RF →
RNF → casos de uso → verificação. Glossário e estados permanecem em apêndice.
A verificação passa de `apendice-b-rastreabilidade.tex` a `08-verificacao.tex`,
com rótulo `cap:verificacao`; a ordem é definida somente em `srs.tex`.

As fichas usam `longtable`, duas colunas (campo e conteúdo), fonte de 11 pt,
espaçamento simples, cabeçalho cinza com texto preto e linhas discretas.
Uma ficha pode continuar em outra página entre campos; o título se repete.
Não colocar fichas extensas em minipages que impeçam paginação. Tabelas compactas
usam `tabularx`; registros extensos e dicionário usam `longtable`.
Quadros e figuras compactos usam caixas no fluxo do texto, com legenda e fonte,
para evitar que um quadro apareça depois da seção seguinte. A reserva de espaço
antes das fichas reduz quebras quando o registro cabe inteiro na página.

`\requisito[campos]{ID}{Título}{Prioridade}{Origem}{Enunciado}{Aceite}` mantém os
seis argumentos obrigatórios existentes e acrescenta campos opcionais por
`keyval`: `categoria`, `precondicoes`, `gatilho`, `entradas`, `saidas`,
`excecoes`, `relacoes`, `metrica`, `meta`, `verificacao`. Valores com vírgulas
usam chaves. Campos não fornecidos são omitidos, sem texto de pendência.
`req:<ID>` e `\reqref{ID}` continuam estáveis.

RF-005 registra consulta de inscrições pessoais e RNF-004 registra conservação
das inscrições confirmadas após reinício normal do serviço. UC-001 e UC-002
permanecem inscrição e cancelamento; UC-003 e UC-004 são consulta de catálogo
e de inscrições pessoais. CT-008 e CT-009 verificam os requisitos novos.
Objetivos OBJ-001/002/003 são descoberta, inscrição válida e cancelamento.

Detalhar contratos HTTP/JSON didáticos, sem impor framework ou banco de dados;
definir códigos e respostas para criação, repetição, falta de vaga, prazo,
autenticação e acesso a recurso de outra pessoa. A matriz inclui objetivos,
requisitos, origem e testes. Uma regra do domínio fica em seu catálogo e é
referenciada pelas fichas, evitando cópias divergentes.

## Aproveitamento das referências

- EnergyOS: campos explícitos de requisito, qualidade mensurável, critérios
  Dado/Quando/Então, dicionário de dados e relação com testes.
- Trabalho interdisciplinar: ficha por funcionalidade, vínculo RF/RNF,
  passos separados entre ação do ator e resposta do sistema.
- DOCX: necessidades/responsabilidades dos stakeholders, condições de casos
  de uso e catalogação de requisitos por categoria.

As referências são fontes de inspiração, não cópias para distribuição.
Registrar nomes, hashes e decisões em `docs/revisao-referencias.md`.

## Validação

Compilar do zero e inspecionar cada página do PDF, especialmente continuação
de fichas, largura das tabelas, cabeçalhos e blocos de fluxo. Exercitar o
verificador com campos opcionais, requisito simples, duplicidade, ID inválido,
ausência na matriz, referência inexistente e marcador editorial. Confirmar
recompilação de arquivos incluídos e limpeza restrita aos artefatos do SRS.
