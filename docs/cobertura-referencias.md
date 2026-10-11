# Cobertura dos modelos de referência

Revisão de 11/10/2026, conforme a [spec 003](specs/003-modelagem-uml-e-cobertura/spec.md).
As fontes e seus SHA-256 estão no [registro de revisão](revisao-referencias.md).
As páginas abaixo são posições no arquivo PDF, começando em 1, e não números
do sumário ou da paginação impressa. O DOCX foi lido por parágrafos e tabelas
do XML; não se atribuem páginas sem renderização.

Esta matriz verifica **cobertura temática e padrões de especificação**. Os três
documentos descrevem domínios ou níveis de detalhe distintos. Não se afirma que
o sistema de inscrições implementa funcionalidades de EnergyOS ou Helium, nem
que os desenhos e textos são cópias dos originais.

## Localização dos destinos

| Código | Arquivo e conteúdo |
| --- | --- |
| I | [Introdução](../conteudo/01-introducao.tex): finalidade, problema, objetivos, escopo, prioridade e organização. |
| C | [Contexto](../conteudo/02-descricao-geral.tex): perspectiva, stakeholders, fronteira, ambiente e premissas. |
| D | [Regras e dados](../conteudo/06-regras-e-dados.tex): RN-001/002, dicionário, invariantes e nulabilidade. |
| API | [Interfaces](../conteudo/03-interfaces.tex): UI, hardware, software externo, comunicação e HTTP/JSON. |
| RF | [Requisitos funcionais](../conteudo/04-requisitos-funcionais.tex): cinco fichas com origem, condições, exceções e aceite. |
| RNF | [Qualidade](../conteudo/05-requisitos-nao-funcionais.tex): quatro fichas mensuráveis e procedimentos. |
| UC | [Casos de uso](../conteudo/07-casos-de-uso.tex): catálogo dos quatro casos, condições, ações/respostas e alternativas. |
| UML | [Modelagem](../conteudo/09-modelagem-uml.tex): §§8.1–8.8, casos, classes, sequência, atividades, componentes, implantação e pacotes. |
| AUX | [Modelos complementares](../conteudo/09-modelagem-uml.tex): §8.9, DER lógico e grafo de rastreabilidade. |
| V | [Verificação](../conteudo/08-verificacao.tex): matriz, nove cenários, procedimentos CT-002/004 e revisão. |
| A | [Apêndice A](../conteudo/apendice-a-glossario-modelos.tex): glossário, UML de estados e tabela de transições. |
| B1 | [Apêndice B](../conteudo/apendice-b-guia-complementar.tex), §B.1: elicitação, perfis, representantes, jornada e histórias. |
| B2 | Mesmo arquivo, §B.2: qualidade, documentação, relatórios, licenças e padrões. |
| B3 | Mesmo arquivo, §B.3: drivers, arquitetura, modelos conceitual/lógico/físico, ADRs e migrações. |
| B4 | Mesmo arquivo, §B.4: classificação, ameaças, segurança e privacidade. |
| B5 | Mesmo arquivo, §B.5: riscos, priorização e impacto de mudanças. |
| B6 | Mesmo arquivo, §B.6: processo, entregas, cronograma/Gantt, estimativa, RACI e custos. |
| B7 | Mesmo arquivo, §B.7: histórico, configuração, branches, pipeline, ambientes, integrações e reversão. |
| B8 | Mesmo arquivo, §B.8: observabilidade, suporte, SLI/SLO, backup, RPO/RTO e recuperação. |
| B9 | Mesmo arquivo, §B.9: portfólio, evidência, aceite de entrega, conclusão, rubrica e artefatos por etapa. |
| META | [Metadados](../config/metadados.tex), capa, folha de rosto, sumário automático e [bibliografia](../referencias.bib). |

“Adaptado” indica que o padrão recebe exemplos do domínio de inscrições.
“Guia complementar” preserva orientação para adaptação, sem impor uma nova
obrigação ao produto fictício. “Fora do domínio” identifica conteúdo específico
que não foi transportado, com justificativa. “Preservado” indica estrutura ou
conteúdo do SRS local já existente, conservado nesta evolução.

## EnergyOS — 27 páginas

Todas as subseções numeradas 1.1–10.8 efetivamente presentes na fonte estão
listadas; a numeração não implica que cada capítulo tenha oito subseções.

| Fonte e tópico | Página(s) | Destino | Decisão e alcance |
| --- | --- | --- | --- |
| Capa e identificação | 1 | META | Adaptado: projeto e autoria do exemplo, sem identidade da fonte. |
| Controle, histórico, uso e mapa do documento | 2 | META, I, B7, README | Adaptado: versão, ordem e instruções de edição; histórico por Git e campos de revisão. |
| 1.1 Finalidade da SRS | 3 | I | Preservado. |
| 1.2 Problema e oportunidade | 3 | I, B1 | Adaptado: problema de vagas; orientação para evidência e impacto. |
| 1.3 Objetivos do produto | 3 | I, V, B1 | Adaptado: OBJ-001/003, indicadores e vínculo a verificação. |
| 1.4 Escopo: dentro e fora | 3 | I | Preservado: fronteira explícita. |
| 1.5 Público-alvo e personas | 4 | C, B1 | Adaptado/guia complementar: perfis, contexto, restrições e fonte. |
| 1.6 Glossário, acrônimos e domínio | 4 | A | Preservado. |
| 1.7 Premissas, dependências e restrições | 4 | C | Preservado: PRE, DEP e RES com consequências. |
| 1.8 Referências e padrões | 4 | META, B2 | Adaptado: edição, fonte, cláusula e alcance. |
| 2.1 Mapa de stakeholders | 5 | C, B1 | Adaptado: responsabilidade, representação, influência e participação. |
| 2.2 Contexto do sistema | 5 | C | Preservado: atores e serviços externos. |
| 2.3 Capacidades do produto | 5 | I, RF, UML | Adaptado: consultar, inscrever, acompanhar e cancelar. |
| 2.4 Regras de negócio | 6 | D, V | Preservado: origem e vínculos com requisitos e testes. |
| 2.5 Casos de uso em nível 0 | 6 | UC, UML §8.2 | Adaptado: quatro objetivos de atores fora da fronteira. |
| 2.6 Jornada e cenário de uso | 7 | B1, UC | Guia complementar: etapa, ação, resposta, dificuldade e oportunidade. |
| 3.1 Fontes e técnicas de elicitação | 8 | B1 | Guia complementar: entrevista, observação, oficina, documentos/dados e protótipo. |
| 3.2 Qualidade de um requisito | 8 | I, V, B2 | Preservado/ampliado: atomicidade, clareza, viabilidade, consistência e verificação. |
| 3.3 Template de requisito funcional | 8 | RF, config/pacotes.tex | Adaptado: ficha extensa e campos opcionais. |
| 3.4 Exemplos funcionais EnergyOS | 8 | RF | Adaptado apenas no padrão; funcionalidades de energia ficam fora do domínio. |
| 3.5 Especificação de caso de uso | 9 | UC | Preservado: condições, fluxo, alternativas e exceções. |
| 3.6 Histórias de usuário e BDD | 9 | RF, B1 | Adaptado: história ligada a RF-005 e aceite Dado/Quando/Então. |
| 3.7 RNF / atributos de qualidade | 9 | RNF, B2 | Preservado/ampliado: medida, meta, ambiente e categorias adicionais. |
| 3.8 Requisitos de interface | 10 | API, B7 | Preservado/ampliado: quatro categorias e orientação de parâmetros operacionais. |
| 3.9 Exemplo de contrato de API | 10 | API | Adaptado: rotas, JSON, erros, titularidade e precedência. |
| 3.10 Priorização | 10 | I, B5 | Adaptado/guia complementar: escala explícita e valor, esforço, risco e dependências. |
| 4.1 Classes; catálogo de tipos de modelos | 11 | UML §§8.1/8.3, B3 | Adaptado: atributos, operações, cardinalidades; DER e C4 distinguem-se da UML. |
| 4.2 Sequência | 12 | UML §8.4 | Adaptado: mensagens, retornos, critical e alt; repetição, criação, recusa e falha. |
| 4.3 Atividades | 13 | UML §8.5 | Adaptado: decisões com guardas, ações e finais alternativos. |
| 4.4 Estados | 14 | A | Adaptado: ativa/cancelada, guardas, repetição e novo objeto na reinscrição. |
| 4.5 Componentes | 14–15 | UML §8.6 | Adaptado: responsabilidade interna e integrações externas, sem tecnologia obrigatória. |
| 4.6 Deployment | 15 | UML §8.7 | Adaptado: nós, artefatos e comunicação em ambiente didático. |
| 4.7 Pacotes | 15–16 | UML §8.8 | Adaptado: dependências entre apresentação, aplicação, domínio e adaptadores. |
| 4.8 Entidade-relacionamento | 16 | AUX, D, B3 | Adaptado: entidades, PK/FK, identidade externa e dado derivado. |
| 4.9 Requirement diagram no Mermaid | 16–17 | AUX, V | Adaptado: grafo objetivo/regra/RF/UC/CT e matriz completa; não apresentado como UML ou SysML. |
| 5.1 Drivers arquiteturais | 18 | B3 | Guia complementar: atomicidade, desempenho, autorização e persistência. |
| 5.2 Visão lógica sugerida | 18 | UML, B3 | Adaptado: responsabilidades e dependências; não impõe estrutura física. |
| 5.3 Dicionário de dados | 18 | D, B3, B4 | Preservado/ampliado: tipos, nulabilidade, limites, sensibilidade e uso. |
| 5.4 Invariantes e consistência | 18 | D, RF, A, B3 | Preservado: atomicidade, repetição, UTC e histórico; exclusão física é questão de adaptação. |
| 5.5 ADR | 18–19 | B3 | Guia complementar: contexto, opções, estado, decisão, consequências e evidência. |
| 5.6 Contratos, erros e observabilidade | 19 | API, B7, B8 | Preservado/guia complementar: erros, correlação, logs, métricas, tracing, timeout, repetição e versões. |
| 6.1 Classificação de dados | 20 | B4 | Guia complementar: público, interno, pessoal e segredo. |
| 6.2 Ameaças / STRIDE simplificado | 20 | B4 | Guia complementar: seis categorias de ameaça, com ativo, consequência, controle e verificação. |
| 6.3 Requisitos de segurança | 20 | RNF, B4 | Adaptado: autorização verificada; orientação para selecionar catálogos de controles por contexto e versão. |
| 6.4 Privacidade por design | 20 | B4 | Guia complementar: finalidade, necessidade, fundamento, retenção, acesso, exportação, exclusão e telemetria. |
| 6.5 Registro de riscos | 21 | B5 | Guia complementar: exemplos vinculados a testes e campos completos para avaliação. |
| 7.1 Matriz de rastreabilidade | 21 | V, AUX, B9 | Preservado/ampliado: objetivo, origem, requisito, UC/regra e CT; orientação para componente/evidência. |
| 7.2 Pirâmide / portfólio de testes | 21 | B9 | Guia complementar: unidade, integração, contrato, ponta a ponta e qualidade. |
| 7.3 Template de caso de teste | 21 | V, B9 | Preservado/ampliado: condições, dados, passos, resultado, tipo, automação e evidência. |
| 7.4 Exemplos de testes | 21–22 | V | Adaptado: nove cenários e procedimentos de concorrência e prazo; sem afirmar execução da aplicação. |
| 7.5 Aceite do release | 22 | B9 | Guia complementar: cobertura, risco, segurança, migração, reversão, operação e documentação. |
| 7.6 Definition of Done | 22 | B9 | Guia complementar: revisão, build, testes, evidência e responsáveis pela avaliação. |
| 8.1 Modelo de desenvolvimento | 22 | B6 | Guia complementar: incremental, Kanban, Scrum, sequencial e híbrido com justificativa. |
| 8.2 Roadmap e releases | 22 | B6 | Guia complementar: objetivo, escopo, dependências e critério de saída. |
| 8.3 Gantt em Mermaid | 23 | B6 | Guia complementar: campos e dependências do cronograma; sem reutilizar datas ou exigir Mermaid. |
| 8.4 Estimativa | 23 | B6 | Guia complementar: intervalo, unidade, premissas e capacidade; esforço distinto de prazo. |
| 8.5 RACI | 23 | B6 | Guia complementar: quatro papéis e uma autoridade final por atividade. |
| 8.6 Custo | 23 | B6 | Guia complementar: fórmula, pessoas, infraestrutura, ferramentas, período e contingência. |
| 9.1 Gestão de configuração | 24 | B7 | Guia complementar: documentos, código, esquema e infraestrutura; exclui segredos e dados de produção. |
| 9.2 Branches e versionamento | 24 | B7 | Guia complementar: revisão, PR, versões, tags e notas de entrega. |
| 9.3 Pipeline CI/CD | 24 | B7, README | Guia complementar: estágios da aplicação; CI documental identificado separadamente. |
| 9.4 Ambientes | 24 | B7 | Guia complementar: local, CI, homologação e produção, com dados e evidência. |
| 9.5 Rollback, backup e recuperação | 24–25 | B7, B8 | Guia complementar: migração, compatibilidade, restauração, perda e tempo toleráveis. |
| 9.6 SLOs e suporte | 25 | B8 | Guia complementar: SLI/SLO, janela, alerta, suporte e limites dos RNF já definidos. |
| 10.1 Checklist de revisão | 26 | V, B9 | Preservado/ampliado: cobertura, consistência e evidência. |
| 10.2 Rubrica de autoavaliação | 26 | B9 | Guia complementar: dimensões, critério, evidência e escala; sem nota fictícia. |
| 10.3 Modelo compacto de requisito | 26 | RF, RNF, README | Adaptado: comando editável e exemplo de uso com seis campos obrigatórios. |
| 10.4 Modelo compacto de ADR | 26 | B3 | Guia complementar: campos da decisão, um ADR por decisão. |
| 10.5 Modelo compacto de risco | 27 | B5 | Guia complementar: campos de registro e exemplos relacionados aos CT. |
| 10.6 Artefatos por entrega | 27 | B9 | Guia complementar: descoberta, especificação, design, implementação, verificação e operação. |
| 10.7 Referências recomendadas | 27 | META, B2, B9 | Adaptado: bibliografia própria e identificação de versão/procedência; lista externa não copiada como fontes lidas. |
| 10.8 Nota sobre EnergyOS | 27 | I, B1, B9 | Adaptado: domínio fictício e ausência de alegação de entrevistas/testes executados. |

## Trabalho interdisciplinar — 51 páginas

| Fonte e tópico | Página(s) | Destino | Decisão e alcance |
| --- | --- | --- | --- |
| Capas, identificação e versão | 1–2 | META | Adaptado: instituição e projeto deste modelo. |
| Histórico de revisão | 3–4 | B7 | Guia complementar: campos e recuperação de versões; autores e datas da fonte não copiados. |
| Sumário | 4–6 | META | Preservado: geração automática e links. |
| 1 Introdução | 7 | I | Adaptado: finalidade do sistema fictício e público do documento. |
| 1.1 Tema e 1.2 Objetivo | 8 | I | Adaptado: problema, solução e objetivos de inscrições. |
| 1.3 Problemática / limites / justificativa | 8 | I, C, B1 | Adaptado: escopo, fronteiras, premissas e orientação sobre evidência/impacto. |
| 2 Perspectiva do sistema | 8 | C | Preservado: responsabilidades e serviços externos. |
| 2.1 Stakeholders | 9–10 | C, B1 | Adaptado: necessidades, papéis e representação, sem nomes da equipe da fonte. |
| 3.1 Formato de funcionalidade e RNF associados | 11–17 | RF, RNF, V | Adaptado: fichas separadas, IDs estáveis e relações explícitas em vez de RNF ambíguos repetidos. |
| F1 Configuração da Hackathon | 11 | I, API | Fora do domínio: publicar/editar evento pertence ao catálogo externo; conserva-se a explicitação da fronteira. |
| F2 CRUD de usuário | 11–13 | C, API, RNF | Fora do domínio: cadastro e credenciais pertencem ao provedor; sessão/titularidade continuam especificadas. |
| F3 CRUD de exercícios | 13–14 | — | Fora do domínio: desafios, respostas, categorias e pontuação não fazem parte de inscrições. |
| F4 CRUD de times | 14–16 | — | Fora do domínio: equipes de competição não fazem parte do produto. |
| F5 Cronômetro | 15–16 | D, RF | Fora do domínio: controle de cronômetro não copiado; prazo é regra de inscrição em UTC. |
| F6 Placar | 16–17 | — | Fora do domínio: classificação por pontuação não é objetivo de inscrições. |
| F7 Login | 17 | C, API, RNF | Adaptado apenas no controle de sessão; login e cadastro locais excluídos pela fronteira. |
| 3.2 RNF suplementares | 17–18 | RNF, B2, B7, B8 | Adaptado/guia complementar: acessibilidade, confiabilidade, desempenho, plataforma e comunicação. |
| Alegações Docker/Serverless e LAN/latência | 18 | B2 | Não transportadas: ferramenta ou rede não demonstra disponibilidade nem elimina necessidade de medir desempenho. |
| 4 Catálogo de casos e relação com funcionalidades | 18–19 | UC, V | Preservado: ator, resumo e vínculo RF/UC/CT. |
| 4.1 Caso de uso geral | 20 | UML §8.2 | Adaptado: atores externos e fronteira com quatro objetivos. |
| CdU1 Login e variação de cadastro | 20–22 | UC, C, API | Adaptado no padrão de fluxo e exceções; autenticação local fora do domínio. |
| CdU2 CRUD de Hackathon | 22–24 | UC, I | Adaptado no padrão de condições/alternativas; gestão externa não importada. |
| CdU3 CRUD de exercícios | 24–25 | UC | Adaptado no padrão de fluxo; funcionalidade específica excluída. |
| CdU4 CRUD de usuários | 25–28 | UC, RNF | Adaptado no padrão de permissão/exceção; cadastro local excluído. |
| CdU5 CRUD de times | 28–29 | UC | Adaptado no padrão de fluxo; funcionalidade específica excluída. |
| CdU6 Cronômetro | 29–30 | UC, D | Adaptado no padrão de condição temporal; cronômetro excluído. |
| CdU7 Exercícios e envio de respostas | 30–31 | UC | Adaptado no padrão de alternativa e resposta; desafios/pontuação excluídos. |
| 5 Diagrama de classes | 31 | UML §8.3 | Adaptado: Evento, Inscrição, identidade externa, enumeração e cardinalidades. |
| 6.1 Atividades de login/cadastro | 32 | UML §8.5 | Adaptado no padrão de decisão; atividade é inscrição e sessão é condição externa. |
| 6.2 Atividades de CRUD | 33 | UML §8.5 | Adaptado: ações, guardas e resultados; não cria CRUD genérico como requisito. |
| 6.3 Atividades de respostas | 34 | UML §8.5 | Adaptado no padrão de alternativas; domínio de exercícios excluído. |
| 7.1 DER | 35 | AUX | Adaptado: entidades e cardinalidades, distinguindo DER de UML. |
| 7.2 Modelo relacional | 36 | AUX, B3 | Adaptado: PK/FK e guia de passagem ao esquema físico; tabelas de Helium não copiadas. |
| 7.3 Dicionário | 37–41 | D, B3, B4 | Adaptado: tipos, unidades, obrigatoriedade, nulabilidade, chaves e sensibilidade. |
| 8 Script SQL | 41–48 | B3, B7 | Guia complementar para esquema/migração; DDL MySQL, dez tabelas, cascatas e collations da fonte excluídos por domínio e implementação. |
| 9 CRUDs e rotas | 48–51 | API, B7 | Adaptado: método, caminho, entrada, resposta e erro; controllers, middleware e rotas de framework da fonte excluídos. |
| 10 Relatórios e vínculo RF/CdU | 51 | RF-005, UC-004, V, B2 | Adaptado: consulta pessoal e rastreabilidade; guia define campos, filtros, acesso e exportação de relatórios. |

## Modelo de SRS — DOCX

| Tópico da fonte | Destino | Decisão e alcance |
| --- | --- | --- |
| Projeto, subsistema/recurso e versão | META, I | Adaptado: identificação e fronteira explícitas. |
| Orientações de campos automáticos Word / RUP | README, B6, B7 | Adaptado: instruções de edição TeX e escolha de processo; atalhos Word e obrigatoriedade de RUP não transportados. |
| Histórico da revisão | B7 | Guia complementar: data, versão, descrição, autor e IDs afetados. |
| Índice analítico | META | Preservado: sumário automático. |
| Introdução / definição da solução | I | Preservado: finalidade e problema da inscrição. |
| Escopo | I | Preservado: dentro/fora e serviços externos. |
| Público-alvo | I, C, B1 | Preservado/ampliado: leitores, usuários e perfis. |
| Definições, acrônimos e abreviações | A | Preservado. |
| Referências | META, B2 | Adaptado: fontes próprias, versão, procedência e alcance. |
| Organização do documento | I, README | Preservado/ampliado: ordem explícita, UML e apêndice B. |
| Visão geral do sistema | C | Preservado. |
| Necessidades/responsabilidades/representante dos stakeholders | C, B1 | Adaptado: papéis do domínio e orientação para representação. |
| Arquitetura funcional | I, RF, UML, B3 | Adaptado: capacidades, fronteira e vistas de responsabilidades. |
| Regras de negócio | D | Preservado. |
| Caso de uso nível 0 | UML §8.2 | Adaptado: desenho dos quatro casos existentes. |
| Requisitos funcionais e localização de ferramentas | RF, README, B9 | Adaptado: fichas e localização de fontes/automação; sem exigir ferramenta comercial. |
| Exemplo F1 / NF1.1 / NF1.2 de Hackathon | RF, RNF, I | Adaptado no padrão; evento único e cadastro por administrador não inseridos na aplicação de inscrições. |
| RNF: usabilidade | RNF-003, B2 | Preservado/guia complementar: teclado, perfil, tarefa, treinamento e acesso. |
| RNF: confiabilidade | RNF-004, B2, B8 | Preservado/guia complementar: reinício; disponibilidade, MTBF, MTTR, precisão e taxas de erro com definições próprias. |
| RNF: desempenho | RNF-001, B2, B8 | Preservado/guia complementar: tempo, percentil, capacidade, recursos, carga e janela. |
| RNF: suportabilidade | B2, B7, B8 | Guia complementar: manutenção, configuração, diagnóstico, atualização e documentação. |
| Restrições de design | C, B2, B3 | Preservado/guia complementar: distinguir obrigação imposta e escolha de tecnologia. |
| Interfaces do usuário | API, RNF-003 | Preservado. |
| Interfaces de hardware | API, B7 | Preservado/guia complementar: escopo atual e orientação de parâmetros físicos quando necessários. |
| Interfaces de software | API | Preservado: catálogo e identidade com campos, validade e falha. |
| Interfaces de comunicação | API, B7 | Preservado/guia complementar: HTTP/JSON, protocolos, rede, portas, limite e repetição. |
| Documentação e licenciamento | B2 | Guia complementar: público, formato, idioma, acesso, atualização e direitos de uso. |
| Observações legais, copyright e outras | B2 | Guia complementar: direitos, recursos e marcas com fonte; sem avisos jurídicos inventados. |
| Padrões aplicáveis | META, B2 | Adaptado: edição, cláusula e verificação; não certifica conformidade. |
| Priorização | I, RF, RNF, B5 | Preservado/guia complementar: escala e critérios de seleção. |
| Rastreabilidade | V, AUX | Preservado/ampliado: matriz completa e grafo ilustrativo. |
| Classes: atributos, métodos e relações | UML §8.3 | Adaptado: conceitos do domínio e multiplicidades. |
| Modelagem de desenvolvimento selecionada | B6 | Guia complementar: escolha e justificativa de processo. |
| Cronograma geral | B6 | Guia complementar: atividades, marcos, dependências, equipe e esforço/prazo. |
| Custo geral e parcial | B6 | Guia complementar: subtotais, total, unidades, período, premissas e fontes de taxas. |

## Preservação do SRS local e verificação

O ponto de comparação é o PDF local de 35 páginas anterior a esta evolução,
e não o template original do upstream. Uma cópia temporária das fontes anteriores
permitiu comparar o conteúdo completo antes da limpeza dos intermediários.
As alterações de outra revisão já presentes no workspace foram conservadas.

Os arquivos de introdução, contexto, regras/dados, interfaces, RF, RNF,
casos de uso e verificação permanecem idênticos em bytes. Foram preservados
nove requisitos (RF-001 a RF-005 e RNF-001 a RNF-004), quatro UC, nove CT, duas RN,
prioridades, critérios de aceite, contratos e todos os campos das fichas.
O apêndice A conserva o glossário, o texto introdutório dos estados e a tabela
completa de transições; somente o desenho é substituído e explicado.

Os oito tipos UML são casos de uso, classes, sequência, atividades, estados,
componentes, implantação e pacotes. DER e rastreabilidade são modelos de apoio.
As fontes vetoriais ficam em `diagramas/`, sem imagens dos documentos recebidos.
Os novos modelos não ampliam o domínio nem mudam o contrato de API.

A versão final tem 54 páginas. `make check` e a compilação limpa em cópia
isolada foram aprovados; o texto extraído das duas compilações é idêntico.
As 54 páginas foram inspecionadas por renderização, com ampliação dos diagramas.
Não há referências indefinidas, caixas excedidas ou destinos PDF duplicados no
log final. O verificador inclui as fontes dos diagramas na análise de referências,
inclusões e marcadores editoriais. Duas verificações negativas em cópia isolada
confirmaram a rejeição de um requisito inexistente e de uma inclusão ausente
inseridos em um arquivo de diagrama; os arquivos foram restaurados em seguida.
As referências originais são conferidas novamente por SHA-256 e permanecem
inalteradas. Essas verificações tratam do documento; não executam testes da
aplicação fictícia nem certificam a correção dos documentos de origem.

Impressões SHA-256 dos arquivos integralmente preservados:

| Arquivo em `conteudo/` | SHA-256 anterior e final |
| --- | --- |
| `01-introducao.tex` | `c2287cf9479a1b01e685effec7af3caf95d044baa971f07e380a052d158deb62` |
| `02-descricao-geral.tex` | `cf6a6987b7bef65a442ddcc368640964c7c821b6db8194e7c92c95a3c0e93858` |
| `03-interfaces.tex` | `6fd6f02e23b886dacdcd49bcf8242a4294453ed5a7132769fdbe35eee44ae6e3` |
| `04-requisitos-funcionais.tex` | `111d39d53ccd6826b43eb947ae1ca58155099916b0d889b68ee7de49f85fb0c9` |
| `05-requisitos-nao-funcionais.tex` | `507d5c0d763b380366a01e5ec5f8e8f886e478bc4e8078aec2995ccf3cf841d6` |
| `06-regras-e-dados.tex` | `3c0fa29d1c872f63a29c9721aeceab6f7525a15e1d6acab94c0b814bb2cf3f98` |
| `07-casos-de-uso.tex` | `7ba79e2401075cb7436566f0ff165fa25a479bb14aa97964e0ece9b97a72bcf2` |
| `08-verificacao.tex` | `f7ec6b2cb5d8ee8c5063f15759381c99c2cac206ed363ac0d6e74a6e3e60dba9` |

A notação tem como referência a [UML 2.5.1 da OMG](https://www.omg.org/spec/UML/2.5.1/About-UML).
A seta inicial da máquina de estados não recebe gatilho ou guarda; a criação
elegível é condição de início do objeto. Artefatos de implantação são desenhados
como elementos internos aos nós. A conferência também considerou os registros
primários da OMG sobre [transição inicial](https://issues.omg.org/issues/UMLR-803)
e a [notação de artefatos implantados](https://www.omg.org/spec/UML/ISO/19505-2/PDF).
