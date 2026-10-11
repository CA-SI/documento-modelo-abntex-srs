LATEXMK ?= latexmk
PYTHON ?= python3
LATEXFLAGS = -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build

.PHONY: all check demo clean mrproper

all:
	$(LATEXMK) $(LATEXFLAGS) srs.tex

check: all
	$(PYTHON) scripts/verificar.py

# Atualiza o PDF demonstrativo versionado somente após verificar a compilação.
demo: check
	mkdir -p exemplos
	cp build/srs.pdf exemplos/srs-demonstracao.pdf

# Limpa somente os auxiliares do SRS e preserva build/srs.pdf.
clean:
	$(LATEXMK) -c -outdir=build srs.tex

# Remove também o PDF do SRS, sem atingir outros PDFs.
mrproper:
	$(LATEXMK) -C -outdir=build srs.tex
