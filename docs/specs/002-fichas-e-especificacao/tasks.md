# Tarefas

- [x] Extrair e revisar as estruturas dos três modelos recebidos.
- [x] Definir a spec, os contratos de fichas e o plano antes de editar o modelo.
- [x] Padronizar tabelas e criar fichas de requisitos com campos opcionais.
- [x] Detalhar contexto, regras, dados, interfaces, casos de uso e testes.
- [x] Atualizar organização, verificador, README e registro das referências.
- [x] Compilar, exercitar o verificador e inspecionar todas as páginas.

## Validação realizada

- `make check`: nove requisitos, rótulos, rastreabilidade e PDF válidos;
  sem referências indefinidas, destinos duplicados ou caixas fora da margem.
- Dezessete cenários do verificador em cópia isolada: ficha opcional, duplicidade,
  formato de ID, campos vazios, argumentos ausentes, grupo não fechado,
  cobertura exclusiva da matriz, referências RF/UC/CT/RN inexistentes,
  marcadores editoriais, uso legítimo de “todo”, inclusão ausente e erros de log.
- Compilação real de ficha com os seis argumentos originais junto das novas;
  recompilação após alterar um arquivo incluído; compilação do zero;
  `make clean` e `make mrproper` preservando um PDF alheio ao SRS.
- PDF final de 35 páginas renderizado e inspecionado: fichas completas,
  cabeçalho repetido no dicionário, exemplo JSON íntegro, quadros dos casos de
  uso em sequência, diagramas legíveis e nenhum texto cortado ou sobreposto.
- Links locais do README e dos registros de revisão conferidos; fontes recebidas
  preservadas e identificadas por SHA-256; cópias de validação removidas.
