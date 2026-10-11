# Plano de implementação

## Contrato do conteúdo

Manter os arquivos e IDs atuais. Inserir `conteudo/09-modelagem-uml.tex` entre
casos de uso e verificação, conforme a ordem explícita em `srs.tex`.
O apêndice A conserva glossário, explicação dos estados e tabela de transições;
seu desenho passa a um arquivo de diagrama. Acrescentar o apêndice B com um
guia de adaptação dos tópicos complementares encontrados na comparação.

Os desenhos ficam em `diagramas/uml/`, um arquivo por tipo. DER e rastreabilidade
ficam em `diagramas/complementares/`. `config/uml.tex` concentra estilos TikZ e
pequenos comandos de ator, pacote e nó de implantação. Usar os pacotes já
fornecidos pelo TeX Live e pelo CI; manter fonte legível e largura máxima da página.

O diagrama de classes representa Evento, Inscrição e Participante identificado
externamente. Cada inscrição tem um evento e um titular; cada um pode ter várias
inscrições históricas. Unicidade aplica-se somente às inscrições ativas.
Os fluxos respeitam a validação de sessão, consulta de duplicidade antes do
prazo e gravação atômica. A máquina de estados conserva o instante do primeiro
cancelamento e não transforma reinscrição em reativação do registro cancelado.

Componentes, implantação e pacotes são exemplos de organização compatíveis
com os contratos; não impõem framework, linguagem, banco ou serviço em nuvem.
O modelo lógico separa identificador externo de titular de uma chave estrangeira
local e explica limites do mapeamento para SQL e migrações.

## Comparação e cobertura

Ler texto de todas as páginas dos PDFs e a estrutura do DOCX. Inspecionar as
78 páginas dos PDFs por renderização, com ampliação dos modelos relevantes.
Inventariar subseções do EnergyOS, capítulos/subseções do trabalho e tópicos
do DOCX. Criar `docs/cobertura-referencias.md` com fonte, página, destino e
decisão. Usar “preservado”, “adaptado”, “guia complementar” ou “fora do domínio”,
sempre com destino ou justificativa concreta.

O guia complementar oferece campos e critérios para adaptação, não status da
produção do documento. Planejamento e orçamento são métodos/formulários;
não apresentar números fictícios como compromissos do projeto.

## Verificação

Guardar uma cópia temporária das fontes/PDF anteriores. Comparar os arquivos de
RF, RNF, casos, regras, interfaces e testes, preservando todo o conteúdo existente.
Verificar todas as inclusões dos diagramas e usar `make check` como gate.
Recompilar do zero em cópia isolada; conferir vetores, guardas, multiplicidades,
setas, legibilidade e paginação. Atualizar README, registro de revisão e tarefas.
Remover cópias temporárias e manter o PDF final em `build/srs.pdf`.
