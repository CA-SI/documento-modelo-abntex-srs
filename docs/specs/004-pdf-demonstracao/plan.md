# Plano de implementação

Manter `build/` ignorado. Adicionar uma exceção específica à regra `*.pdf`
para o PDF demonstrativo em `exemplos/`. Acrescentar `make demo`, dependente
de `check`, que copia `build/srs.pdf` após a validação. Documentar o link,
a finalidade e o comando no README.

Conferir a igualdade entre o PDF compilado e a demonstração, os arquivos
incluídos no commit e o avanço da branch remota. Usar a configuração GPG
canônica, sem sobrescrever autor, committer ou desativar assinatura.
Após o push, confirmar o hash remoto e acompanhar o workflow de compilação.
