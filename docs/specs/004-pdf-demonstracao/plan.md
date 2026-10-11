# Plano de implementação

Manter `build/` ignorado. Adicionar uma exceção específica à regra `*.pdf`
para o PDF demonstrativo em `exemplos/`. Acrescentar `make demo`, dependente
de `check`, que copia `build/srs.pdf` após a validação. Documentar o link,
a finalidade e o comando no README.

Conferir a igualdade entre o PDF compilado e a demonstração, os arquivos
incluídos no commit e o avanço da branch remota. Usar a configuração GPG
canônica, sem sobrescrever autor, committer ou desativar assinatura.
Após o push, confirmar o hash remoto e acompanhar o workflow de compilação.

## Compatibilidade Linux observada na publicação

O primeiro workflow não encontrou `abntex2.cls`. O pacote Ubuntu
`texlive-publishers` fornece a classe, conforme a
[lista oficial de arquivos](https://packages.ubuntu.com/noble/all/texlive-publishers/filelist).
Acrescentar essa dependência ao workflow e à instalação documentada. Conferir
a resolução da classe com `kpsewhich abntex2.cls` antes da compilação e aguardar
o resultado do workflow corrigido. O PDF demonstrativo não muda nessa correção.
