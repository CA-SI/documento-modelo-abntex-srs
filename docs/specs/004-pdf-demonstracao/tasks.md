# Tarefas

- [x] Definir escopo e contrato de publicação antes da alteração.
- [x] Versionar PDF demonstrativo e documentar atualização e acesso.
- [x] Validar compilação, igualdade do PDF e arquivos do commit.
- [x] Criar commit assinado e publicar sem sobrescrever histórico remoto.
- [x] Corrigir dependência Linux identificada pelo primeiro workflow remoto.
- [x] Confirmar publicação e verificar resultado do workflow.

## Evidências locais

- `make demo` aprovado, incluindo `make check`.
- PDF demonstrativo idêntico a `build/srs.pdf`, com 54 páginas e 449.679 bytes.
- SHA-256: `6df369046fc184b9dbd5ea457e0e35d55d75c83d44e80306326faca1b87bc154`.
- `build/` continua ignorado; somente o PDF nomeado em `exemplos/` tem exceção.
- `git diff --check` sem problemas; remoto em `423aa94` antes da publicação.

## Evidências remotas

- Commit inicial `4796bf466a5091ae196ba4a206e52d743ba581a5` publicado em
  `origin/master`; assinatura GPG confirmada pelo GitHub como `valid`.
- Workflow inicial `38164444002` identificou ausência de `abntex2.cls`;
  `texlive-publishers` acrescentado ao CI e ao README, com checagem da classe.
- Correção publicada no commit assinado `74cd805b15b72bbbe9a25d055771f607fb27144d`.
- [Workflow corrigido](https://github.com/CA-SI/documento-modelo-abntex-srs/actions/runs/38165006800)
  concluído com `success`, incluindo compilação, verificação e publicação do artefato PDF.
- [PDF de demonstração](https://github.com/CA-SI/documento-modelo-abntex-srs/blob/master/exemplos/srs-demonstracao.pdf)
  publicado no repositório e acessível pelo README.
