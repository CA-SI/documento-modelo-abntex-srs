# Modelagem UML e cobertura dos modelos de referência

## Objetivo

Completar o guia-modelo SRS com diagramas UML consistentes e uma revisão de
cobertura dos dois PDFs e do DOCX recebidos. A comparação anterior aproveitou
fichas e testes, mas não preservou explicitamente todos os tópicos didáticos.
Esta evolução recupera esses tópicos sem substituir o domínio de inscrições.

## Critérios de aceite

- Preservar os nove requisitos, quatro casos de uso, nove cenários, duas regras,
  campos de dados, contratos, prioridades, critérios de aceite e limites atuais.
- Acrescentar casos de uso, classes, sequência, atividades, componentes,
  implantação e pacotes; revisar a máquina de estados existente como UML.
- Usar atores fora da fronteira, associações e cardinalidades coerentes,
  mensagens e retornos distintos, decisões com guardas e estados válidos.
- Manter diagramas vetoriais editáveis em TeX, sem Java, serviço remoto,
  imagens rasterizadas ou nova dependência para a compilação.
- Separar modelos conceituais dos exemplos de arquitetura. Uma decomposição
  didática não estabelece tecnologia ou infraestrutura obrigatória.
- Cobrir também DER/modelo lógico e relações entre requisitos e verificação,
  identificando essas representações como complementares à UML.
- Recuperar orientações para elicitação, histórias/jornada, qualidade,
  documentação, licenciamento, privacidade, riscos, planejamento, estimativa,
  custos, configuração, operação e aceite em um apêndice de adaptação.
- Mapear todas as subseções temáticas das referências a uma localização do
  guia ou a uma exclusão fundamentada por domínio ou implementação específica.
  Não afirmar equivalência literal entre aplicações com domínios diferentes.
- Registrar a comparação com a versão local anterior e comprovar que as fichas,
  fluxos, testes e contratos preservados não foram apagados.
- Compilar, verificar referências e inspecionar todas as páginas do PDF final.

## Fora de escopo

Copiar funcionalidades, SQL, marcas ou textos de EnergyOS/Helium; implementar
a aplicação; inventar resultados de elicitação, testes, estimativas ou aprovação;
alterar os arquivos recebidos; criar DOCX; publicar alterações remotas.

## Fontes

Os arquivos recebidos são identificados em `docs/revisao-referencias.md`.
A notação usa como referência a especificação UML 2.5.1 da OMG.
