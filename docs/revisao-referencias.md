# Revisão dos modelos recebidos

Esta revisão complementa a [comparação dos forks](revisao-forks.md). A evolução
das fichas segue a [spec 002](specs/002-fichas-e-especificacao/spec.md).
A modelagem e a revisão de cobertura seguem a
[spec 003](specs/003-modelagem-uml-e-cobertura/spec.md).
Os três arquivos foram fornecidos pelo autor como referências de apresentação
e especificação. Permanecem fora do repositório; não foram alterados.

## Fontes e método de leitura

| Arquivo | Leitura realizada | Contribuição principal |
| --- | --- | --- |
| `Template_SRS_Engenharia_Software_v2_EnergyOS.pdf` (27 páginas) | Texto de todas as páginas; inspeção visual das 27 páginas renderizadas, em folhas de contato; ampliação inicial das fichas. | Requisitos, UML, dados, arquitetura, elicitação, segurança, riscos, planejamento, testes e operação. |
| `SRS-TrabalhoInterdiciplinar.pdf` (51 páginas) | Texto de todas as páginas; inspeção visual das 51 páginas renderizadas, em folhas de contato; ampliação inicial de funcionalidade e caso de uso. | Fichas, ação/resposta, alternativas, classes, atividades, DER, modelo relacional, dicionário e rotas. |
| `Modelo de SRS.docx` | Leitura estrutural do XML do DOCX, incluindo parágrafos e tabelas; sem avaliação da paginação renderizada. | Stakeholders, categorias de requisitos e condições dos casos de uso. |

A leitura identifica padrões aproveitáveis; não representa uma auditoria da
correção técnica ou da conformidade normativa dos documentos recebidos.
Os desenhos relevantes também são conferidos com ampliação. A inspeção seletiva
da revisão de fichas foi ampliada para as 78 páginas e para todos os tópicos
estruturais na revisão de modelagem. A
[matriz de cobertura](cobertura-referencias.md) registra destino e decisão por
subseção das fontes, inclusive o que não pertence ao domínio de inscrições.

Identificadores SHA-256 das fontes:

```text
EnergyOS:
9c9600d49afe0ade05dc409bcd93525a920846d8fc245e07ee719ade9d5752e9
Trabalho interdisciplinar:
d9ea7969e3087d00418a32aeb00f43e3ec10c8424730e4c9320d00c4ae6147cb
Modelo DOCX:
e8d11f3c4bb69272ec7439c144771acac05e460c07d2756839cc3e664fbb1905
```

## Decisões incorporadas

| Padrão observado | Aplicação no modelo SRS |
| --- | --- |
| Fichas extensas de requisitos | Campos obrigatórios preservados e campos opcionais para categoria, precondições, gatilho, entradas, saídas, exceções e relações. |
| Requisitos de qualidade mensuráveis | Métrica, meta, condições de medição e procedimento de verificação em cada RNF. |
| Critérios de aceite observáveis | Exemplos Dado/Quando/Então, incluindo duplicidade, última vaga, titularidade e limite exato de prazo. |
| Identificação de interessados | Quadros de stakeholders, objetivos, responsabilidades e dependências externas. |
| Casos de uso detalhados | Ator, gatilho, precondições e pós-condições; passos com ação e resposta; alternativas e exceções ligadas à etapa. |
| Especificação dos dados e interfaces | Tipos, limites, nulabilidade e campos derivados; contrato HTTP/JSON com respostas, erros e precedência das verificações. |
| Relação entre requisitos e testes | Matriz com objetivos e origem; nove cenários; dois procedimentos com dados, passos, resultado esperado e evidências. |
| Vistas do domínio e do design | Oito tipos UML vetoriais, DER lógico e grafo de rastreabilidade, com fronteiras e finalidade explícitas. |
| Conteúdo complementar de engenharia | Apêndice B com elicitação, perfis/jornada, qualidade, documentação/licenças, ADRs, privacidade, riscos, processo, custos, configuração, operação e aceite. |

Os cabeçalhos têm fundo cinza claro, texto preto e alinhamento consistente.
Tabelas compactas distribuem a largura entre as colunas. Fichas e dicionário
usam tabelas que podem continuar entre linhas, com cabeçalho repetido. Quadros compactos
ficam no fluxo do texto, próximos de suas descrições, sem flutuar entre seções.

A organização passa a ser introdução → contexto → regras e dados → interfaces
→ RF → RNF → casos de uso → modelagem → verificação, seguida de referências,
glossário/estados e guia complementar.
Isso apresenta as restrições e o vocabulário antes de detalhar comportamentos.

## Coerência do exemplo

O domínio continua sendo o sistema fictício de inscrições em eventos. A consulta
de inscrições pessoais foi formalizada em RF-005 e a conservação de operações
confirmadas após reinício normal em RNF-004. Os IDs anteriores permanecem
estáveis. A matriz relaciona cada requisito a um cenário de teste.

Regras especificam concorrência, repetição, prazo em UTC, titularidade,
reinscrição e conservação do instante do primeiro cancelamento. O catálogo
externo não pode reduzir a capacidade abaixo das inscrições ativas. A sessão
define o titular; o cliente não pode escolher outra pessoa no corpo da criação.

Funcionalidades de energia, desafios de Hackathon, times, placar, cronômetro,
cadastro local, SQL e controllers das fontes não foram incorporados. Seu padrão
de especificação recebe exemplos próprios e suas exclusões são registradas.
Os arquivos do SRS local anterior foram comparados integralmente, preservando
nove requisitos, quatro casos de uso, nove cenários e duas regras, além de
contratos, campos, prioridades e aceite. O modelo apresenta elaboração didática própria e
não declara que os testes do sistema fictício foram executados.
