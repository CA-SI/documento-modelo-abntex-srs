# Plano de implementação

## Arquitetura e contratos

`srs.tex` declara a classe abnTeX2 e a ordem dos elementos. `config/pacotes.tex`
contém tipografia, tabelas, links e o comando de requisito; `config/metadados.tex`
centraliza projeto, autoria, instituição, local, data e versão. `conteudo/`
contém uma unidade por capítulo ou apêndice. `referencias.bib` reúne as fontes.
O texto usa espaçamento simples para leitura de uma especificação técnica;
blocos de requisitos permanecem inteiros na página e o sumário lista até seções.

O documento é um guia-modelo: instruções didáticas e um exemplo fictício de
inscrição em eventos. Os exemplos são explicitamente didáticos e coerentes
entre requisitos, regras e testes. Não há campos de rascunho no PDF.

O comando `\requisito` recebe ID, título, prioridade, origem, enunciado e
critério de aceite. Ele cria `req:<ID>` para `\ref`; IDs nunca dependem do
contador das seções. A matriz referencia esses rótulos.

Usar pdfLaTeX e BibTeX com `abntex2cite` para manter dependências pequenas.
Documentar a edição legada das normas bibliográficas implementada pelo pacote,
sem prometer a seleção de edições oferecida pelo projeto de modelos UFV.

`latexmk` gerencia as passagens e grava somente em `build/`. O Makefile executa
a compilação sempre que invocado (o próprio latexmk decide o que recompilar),
evitando dependências incompletas em arquivos incluídos. `make check` chama um
verificador Python para IDs duplicados, marcadores editoriais e problemas do
log. `clean` preserva o PDF; `mrproper` remove somente `build/srs.pdf` após limpar.

## Decisões

- Reimplementar as ideias úteis dos forks, preservando créditos e sem importar
  exemplos específicos, pacotes externos ou arquivos de compilação.
- Adotar do artigo CA-SI a separação entre conteúdo, configuração e build,
  documentação em português e compilação por latexmk.
- Não copiar o pacote `abntex2-UFV`: sua fonte canônica é outro repositório e
  sua API trata trabalhos acadêmicos, não o conteúdo de uma SRS.

## Validação

Compilar do zero, verificar log e PDF, renderizar e inspecionar todas as páginas.
Confirmar que alterações em conteúdo incluído e metadados recompilam o PDF.
Exercitar a rejeição de marcadores e IDs duplicados com entradas temporárias.
Verificar que `clean` preserva o PDF e que `mrproper` preserva PDFs alheios.
