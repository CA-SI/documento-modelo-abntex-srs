# Modelo de especificação de requisitos de software — abnTeX2

Guia-modelo LaTeX em português brasileiro para escrever uma **especificação de
requisitos de software (SRS)**. Mantido pela comunidade de Sistemas de Informação
da **UFV, Campus Rio Paranaíba**, na organização
[CA-SI — Centro Acadêmico de Sistemas de Informação](https://github.com/CA-SI#readme).

O documento explica cada parte de uma SRS e demonstra, com um sistema fictício
de inscrições em eventos, requisitos funcionais e não funcionais, regras de
negócio, dicionário de dados, contratos HTTP/JSON, casos de uso, critérios de
aceite e uma matriz de rastreabilidade. O exemplo contém cinco requisitos
funcionais, quatro requisitos de qualidade, quatro casos de uso e nove cenários
de teste, incluindo procedimentos para concorrência e limites de prazo.
Inclui oito tipos de diagramas UML editáveis: casos de uso, classes, sequência,
atividades, estados, componentes, implantação e pacotes. DER e grafo de
rastreabilidade complementam os modelos. Um guia de adaptação aborda elicitação,
qualidade, arquitetura, privacidade, riscos, planejamento, custos e operação.
Usa a classe **abnTeX2**, com capa, folha de rosto, sumário, referências e
apêndices. O conteúdo é dividido em arquivos para facilitar edição e revisão.

**[Abrir o PDF de demonstração](exemplos/srs-demonstracao.pdf)** — versão
compilada do exemplo, com 54 páginas, para consultar a apresentação, as fichas
e os diagramas sem instalar LaTeX.

## Compilar e verificar

Instale uma distribuição TeX com `latexmk`, pdfLaTeX, BibTeX, abnTeX2 e fontes
Latin Modern, além de Python 3 para a verificação. No Debian/Ubuntu:

```sh
sudo apt-get install latexmk texlive-lang-portuguese texlive-latex-extra texlive-fonts-recommended lmodern python3
make          # gera build/srs.pdf
make check    # compila e verifica IDs, rastreabilidade, marcadores e log
make demo     # verifica e atualiza exemplos/srs-demonstracao.pdf
```

No macOS, o MacTeX completo oferece as dependências TeX. No Windows, use uma
distribuição TeX que disponibilize esses pacotes; com Python 3 instalado, os
comandos equivalentes, sem depender de `make`, são:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build srs.tex
python3 scripts/verificar.py
```

No Overleaf, envie os arquivos do repositório, selecione `srs.tex` como documento
principal e pdfLaTeX como compilador. A verificação Python é executada localmente
ou no CI. O workflow do GitHub Actions compila, verifica e disponibiliza o PDF
nos artefatos de cada execução bem-sucedida.

`make clean` limpa os auxiliares do SRS e preserva seu PDF. `make mrproper`
remove também `build/srs.pdf`. Ambos atuam somente nos arquivos desta compilação.

O PDF em `exemplos/` é versionado separadamente. Após editar as fontes, execute
`make demo` e inclua a demonstração atualizada no mesmo commit. Para atualizar
sem `make`, execute os comandos de compilação e verificação acima e copie
`build/srs.pdf` para `exemplos/srs-demonstracao.pdf`.

## Como adaptar

1. Edite projeto, autores, instituição, local, data e versão em
   [config/metadados.tex](config/metadados.tex).
2. Substitua o exemplo didático nos arquivos de `conteudo/` pelo seu produto.
   Delimite escopo e interfaces antes de detalhar os requisitos.
3. Use `\requisito{ID}{Título}{Prioridade}{Origem}{Enunciado}{Critério de aceite}`.
   Preserve IDs ao reorganizar o texto; use `\reqref{RF-001}` para criar um link.
4. Detalhe condições, fluxos, alternativas e exceções em
   [conteudo/07-casos-de-uso.tex](conteudo/07-casos-de-uso.tex).
5. Edite os modelos em [diagramas/](diagramas/), conferindo nomes, campos,
   multiplicidades, guardas e mensagens com as fichas. Componentes, implantação
   e pacotes são exemplos de design; a adaptação deve justificar suas escolhas.
6. Atualize a matriz e os cenários no capítulo de verificação, incluindo
   alternativas, erros e condições de limite.
7. Use o [guia complementar](conteudo/apendice-b-guia-complementar.tex) para
   especificar os tópicos necessários ao seu contexto, sem atribuir resultados
   de entrevistas, testes ou estimativas que não tenham ocorrido.
8. Cadastre as fontes em `referencias.bib` e execute `make check`.

As fichas aceitam campos opcionais antes dos seis argumentos obrigatórios.
Envolva valores que contêm vírgulas em chaves:

```tex
\requisito[
  categoria={Funcional},
  precondicoes={Sessão válida, evento conhecido},
  gatilho={Participante confirma a inscrição},
  entradas={Identificador do evento},
  saidas={Identificador da inscrição confirmada},
  excecoes={Prazo encerrado ou ausência de vagas},
  relacoes={\ucref{UC-001}; \ctref{CT-002}}
]{RF-002}{Realizar inscrição}{Alta}{STK-002}
{O sistema deve confirmar uma inscrição válida sem exceder a capacidade.}
{\aceite{um evento elegível com vaga}{o participante confirma}
  {uma inscrição é persistida e seu identificador é apresentado}}
```

Para qualidade, use também `metrica`, `meta` e `verificacao`: registre unidade,
ambiente, carga e janela de medição junto do limite exigido. Campos opcionais
ausentes são omitidos. Os exemplos completos estão nos capítulos de RF e RNF.

`tabelasrs` oferece tabelas compactas com colunas `L{largura}` ou `Y`, que
distribui o espaço restante. `\cabecalhosrs` aplica o fundo do cabeçalho.
Envolva a tabela em `quadrosrs` para incluir legenda e fonte no fluxo do texto;
`figurasrs` oferece a mesma organização para diagramas.
Para fichas extensas, use `fichasrs` e `\campoficha{Campo}{Conteúdo}`: a tabela
pode continuar entre campos e repete seu cabeçalho. As fichas de requisitos
reservam espaço antes de começar para reduzir quebras desnecessárias.

Os desenhos usam TikZ e ficam vetoriais no PDF. Os estilos estão em
[config/uml.tex](config/uml.tex); `\diagramasrs{Legenda}{Rótulo}{Conteúdo}`
organiza cada figura. Não é necessário instalar Java, PlantUML ou usar um
serviço externo. A notação tem como referência a
[UML 2.5.1 da OMG](https://www.omg.org/spec/UML/2.5.1/About-UML).

O PDF contém o conteúdo da especificação. Decisões em aberto e tarefas editoriais
devem ser acompanhadas em [issues](https://github.com/CA-SI/documento-modelo-abntex-srs/issues),
com checklist e links para alterações relacionadas. O verificador rejeita
marcadores como `TODO`, `TBD` e `FIXME` no texto compilado.

## Estrutura

```text
srs.tex                   entrada e ordem do documento
config/metadados.tex      projeto, autoria e dados da capa
config/pacotes.tex        apresentação e comando de requisito
config/uml.tex            estilos e comandos para os diagramas vetoriais
conteudo/01-*.tex          introdução e convenções
conteudo/02-*.tex          contexto, usuários e ambiente
conteudo/03-*.tex          interfaces externas
conteudo/04-*.tex          requisitos funcionais
conteudo/05-*.tex          requisitos não funcionais
conteudo/06-*.tex          regras de negócio e dados
conteudo/07-*.tex          casos de uso, fluxos e exceções
conteudo/08-*.tex          rastreabilidade, cenários e procedimentos de teste
conteudo/09-*.tex          modelagem UML, antes da verificação na ordem de leitura
conteudo/apendice-a-*.tex  glossário e modelo de estados
conteudo/apendice-b-*.tex  guia complementar de adaptação
diagramas/uml/            oito tipos UML, um arquivo TeX por desenho
diagramas/complementares/ DER lógico e grafo de rastreabilidade
exemplos/srs-demonstracao.pdf PDF compilado para consulta no GitHub
referencias.bib           fontes bibliográficas
scripts/verificar.py      verificações do modelo e do log
docs/specs/               especificação, plano e tarefas da evolução do modelo
docs/revisao-forks.md      comparação da origem, forks e artigo CA-SI
docs/revisao-referencias.md estruturas aproveitadas dos três modelos recebidos
docs/cobertura-referencias.md tópicos das fontes, destinos e exclusões justificadas
build/                    PDF e auxiliares gerados (fora do Git)
```

## Origem e alcance normativo

Este projeto deriva de [jpeisenbarth/SRS-Tex](https://github.com/jpeisenbarth/SRS-Tex),
baseado no modelo de Karl E. Wiegers. A revisão dos forks e as decisões de
aproveitamento estão em [docs/revisao-forks.md](docs/revisao-forks.md).

A estrutura oferece um ponto de partida para engenharia de requisitos;
a [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) é uma referência
para processos e informações de requisitos. O modelo **não certifica conformidade
com ABNT, IEEE ou ISO**. O uso de abnTeX2 organiza a apresentação, mas não substitui
a avaliação das normas e das exigências do curso ou do projeto.

A evolução das fichas, dos casos de uso e dos testes também se inspira nos
três modelos fornecidos para revisão. O [registro das referências](docs/revisao-referencias.md)
identifica os arquivos e explica as escolhas, sem redistribuir os documentos
recebidos ou transportar seu conteúdo para o exemplo.
Uma [matriz de cobertura](docs/cobertura-referencias.md) relaciona as subseções
dos dois PDFs e os tópicos do DOCX a seu destino no guia, com exclusões explícitas
para funcionalidades e implementações de outros domínios. A revisão também
confere a preservação integral das fichas, dos casos, dos contratos e dos testes
da versão local anterior.

A bibliografia usa `abntex2cite` e BibTeX, cuja implementação é baseada nas
edições de 2002 das normas de citações e referências, conforme a
[documentação do pacote](https://tug.ctan.org/macros/latex/contrib/abntex2/doc/abntex2cite-alf.pdf).
Este SRS não oferece um seletor de edições bibliográficas.

## Projetos relacionados da CA-SI

- [Artigo sobre o guia e modelo abnTeX2 UFV](https://github.com/CA-SI/artigo-modelo-abntex-ufv):
  descreve o pacote de estilo, a escolha da edição das normas e o processo de
  compilação, verificação e distribuição dos modelos acadêmicos.
- [Modelos de documentos acadêmicos abnTeX2 UFV](https://github.com/CA-SI/modelo-documentos-abntex-UFV):
  guia e modelos para TCC e trabalhos acadêmicos.
- [Perfil da organização CA-SI](https://github.com/CA-SI/.github/blob/main/profile/README.md):
  apresentação da comunidade e catálogo de projetos.

## Créditos e licença

O modelo original é de **Jean-Philippe Eisenbarth**, distribuído sob
**GPL-3.0-or-later**, preservada nesta adaptação. Consulte [LICENSE](LICENSE).
A licença deste repositório difere da licença de outros projetos da organização.

Créditos do projeto original:

- [Yiannis Lazarides](https://tex.stackexchange.com/users/963/yiannis-lazarides),
  pela [resposta sobre SRS em LaTeX](https://tex.stackexchange.com/questions/42602/software-requirements-specification-with-latex).
- [Karl E. Wiegers](https://karlwiegers.com), pelo modelo de SRS.
- Ken Rimlinger, pela colaboração no SRS-Tex.
- [François Charoy](https://www.loria.fr/~charoy/), pela sugestão de publicar e
  compartilhar o modelo com estudantes.

Contribuições são bem-vindas por issues e pull requests. Mudanças estruturais
seguem uma especificação por feature em `docs/specs/`, com `spec.md`, `plan.md`
e `tasks.md`.
