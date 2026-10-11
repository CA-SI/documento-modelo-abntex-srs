# Tarefas

- [x] Definir escopo e contrato de publicação antes da alteração.
- [x] Versionar PDF demonstrativo e documentar atualização e acesso.
- [x] Validar compilação, igualdade do PDF e arquivos do commit.
- [ ] Criar commit assinado e publicar sem sobrescrever histórico remoto.
- [ ] Confirmar publicação e verificar resultado do workflow.

## Evidências locais

- `make demo` aprovado, incluindo `make check`.
- PDF demonstrativo idêntico a `build/srs.pdf`, com 54 páginas e 449.679 bytes.
- SHA-256: `6df369046fc184b9dbd5ea457e0e35d55d75c83d44e80306326faca1b87bc154`.
- `build/` continua ignorado; somente o PDF nomeado em `exemplos/` tem exceção.
- `git diff --check` sem problemas; remoto em `423aa94` antes da publicação.
