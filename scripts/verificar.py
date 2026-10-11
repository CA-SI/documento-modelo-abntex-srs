"""Verifica fichas, rastreabilidade e compilação sem dependências externas."""

from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ID = r"(?:RF|RNF)-[0-9]{3}"
MARKERS = re.compile(
    r"(?-i:\b(?:TODO|TBD|FIXME|XXX)\b)|\b(?:todo|tbd|fixme|xxx)\s*:|"
    r"ainda\s+falta|conferência\s+pendente|versão\s+de\s+trabalho|"
    r"em\s+preparação|será\s+revisado|revisão\s+pendente|a\s+definir",
    re.IGNORECASE,
)


def read_group(text, start, opening, closing):
    """Lê um grupo TeX, preservando delimitadores literais dentro das chaves."""
    depth, braces, position = 1, 0, start + 1
    while position < len(text):
        char = text[position]
        if char == "\\":
            position += 2
            continue
        if opening == "[" and char in "{}":
            braces += 1 if char == "{" else -1
        elif braces == 0:
            if char == opening:
                depth += 1
            elif char == closing:
                depth -= 1
                if depth == 0:
                    return text[start + 1:position], position + 1
        position += 1
    raise ValueError(f"Grupo {opening}{closing} não fechado")


def requirement_records(text):
    """Aceita a assinatura simples e a assinatura com campos opcionais."""
    records = []
    for match in re.finditer(r"\\requisito\b", text):
        position = match.end()
        while position < len(text) and text[position].isspace():
            position += 1
        # Ignora a declaração do comando em \newcommand{\requisito}.
        if position >= len(text) or text[position] not in "[{":
            continue
        if text[position] == "[":
            _, position = read_group(text, position, "[", "]")
        fields = []
        for _ in range(6):
            while position < len(text) and text[position].isspace():
                position += 1
            if position >= len(text) or text[position] != "{":
                raise ValueError("Ficha de requisito não possui seis argumentos obrigatórios")
            value, position = read_group(text, position, "{", "}")
            fields.append(value.strip())
        records.append(fields)
    return records


def main():
    errors, texts, records = [], {}, []
    sources = [ROOT / "srs.tex", *sorted((ROOT / "config").glob("*.tex")),
               *sorted((ROOT / "conteudo").glob("*.tex")),
               *sorted((ROOT / "diagramas").rglob("*.tex"))]
    for path in sources:
        content = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text(encoding="utf-8"))
        texts[path] = content
        if MARKERS.search(content):
            errors.append(f"Marcador editorial em {path.relative_to(ROOT)}")
        for name in re.findall(r"\\input\{([^}]+)\}", content):
            if not (ROOT / f"{name}.tex").is_file():
                errors.append(f"Arquivo incluído ausente: {name}.tex")
        try:
            records.extend(requirement_records(content))
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    ids = [record[0] for record in records]
    for record in records:
        if not re.fullmatch(ID, record[0]):
            errors.append(f"Identificador inválido: {record[0]}")
        if any(not field for field in record[1:]):
            errors.append(f"Campo obrigatório vazio em {record[0]}")
    for identifier, count in Counter(ids).items():
        if count > 1:
            errors.append(f"Identificador duplicado: {identifier}")
    if not ids:
        errors.append("Nenhum requisito identificado")

    combined = "\n".join(texts.values())
    matrix = texts.get(ROOT / "conteudo/08-verificacao.tex", "")
    # Apenas a seção da matriz conta como cobertura; menções nos testes não contam.
    matrix = matrix.split(r"\section{Catálogo de cenários}", 1)[0]
    traced = set(re.findall(rf"\\reqref\{{({ID})\}}", matrix))
    for identifier in sorted(set(ids) - traced):
        errors.append(f"Requisito sem rastreabilidade: {identifier}")
    referenced = set(re.findall(rf"\\reqref\{{({ID})\}}", combined))
    for identifier in sorted(referenced - set(ids)):
        errors.append(f"Referência a requisito inexistente: {identifier}")
    for command, prefix, pattern in [("ucref", "uc", r"UC-[0-9]{3}"),
                                      ("ctref", "ct", r"CT-[0-9]{3}"),
                                      ("rnref", "rn", r"RN-[0-9]{3}")]:
        labels = re.findall(rf"\\label\{{{prefix}:({pattern})\}}", combined)
        for label, count in Counter(labels).items():
            if count > 1:
                errors.append(f"Rótulo duplicado: {prefix}:{label}")
        refs = set(re.findall(rf"\\{command}\{{({pattern})\}}", combined))
        for label in sorted(refs - set(labels)):
            errors.append(f"Referência inexistente: {prefix}:{label}")

    pdf, log = ROOT / "build/srs.pdf", ROOT / "build/srs.log"
    if not pdf.is_file() or not pdf.read_bytes().startswith(b"%PDF-"):
        errors.append("PDF ausente ou inválido: build/srs.pdf")
    if not log.is_file():
        errors.append("Log de compilação ausente: build/srs.log")
    else:
        content = log.read_text(encoding="utf-8", errors="replace")
        for pattern in (r"^!", r"undefined", r"multiply[- ]defined",
                        r"Overfull \\[hv]box", r"Rerun to get cross-references right",
                        r"Table widths have changed", r"destination with the same identifier"):
            if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                errors.append(f"Problema no log: {pattern}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verificação concluída: {len(ids)} requisitos, casos, testes, rastreabilidade e PDF válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
