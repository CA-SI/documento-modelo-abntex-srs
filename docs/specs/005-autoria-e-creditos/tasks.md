# Passos de implementação e validação

1. Definir escopo e plano da atribuição antes da edição.
2. Atualizar autoria, agradecimentos e descrição do hard fork.
3. Executar `make demo` e conferir capa, folha de rosto e metadados.
4. Comparar os arquivos técnicos e diagramas com o commit anterior.
5. Renderizar e inspecionar o PDF, incluindo créditos e paginação.
6. Publicar commit GPG assinado, conferir o PDF remoto e acompanhar o CI.

## Evidências locais

- `make demo`, incluindo `make check`, aprovado.
- PDF com 55 páginas e metadado Author igual a `Matheus Breguêz`.
- Capa, folha de rosto e página de créditos conferidas por extração de texto.
- As 55 páginas foram renderizadas e inspecionadas; créditos e sumário estão
  em páginas separadas, sem cortes ou sobreposição.
- Todos os capítulos técnicos e diagramas idênticos em bytes ao commit anterior.
- PDF demonstrativo idêntico a `build/srs.pdf`.
