"""Static checks on the saved notebooks; no code is executed.

Usage (from the repository root):
    python tests/check_notebooks.py

Checks:
1. every executable line of code has a comment, on the line itself or on the line above;
2. every notebook opens with a title, the series line and a Study guide;
3. no saved output contains an error, and no cell or output contains a local file path.
"""
import ast
import io
import re
import sys
import tokenize
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))
SERIES = "*Python for Engineers: Case Studies from Calculator to Simulation*"
LOCAL_PATH = re.compile(r"(/home/|/Users/|/tmp/|/mnt/|[A-Z]:\\\\Users|ipykernel_)")
URL = re.compile(r"https?://\S+")


def has_local_path(text):
    """True if the text contains a local file path (web addresses are ignored)."""
    return bool(LOCAL_PATH.search(URL.sub("", text)))


def uncovered_lines(src):
    """Return the code lines that have no comment on them or directly above them."""
    lines = src.splitlines()
    tokens = list(tokenize.generate_tokens(io.StringIO(src + "\n").readline))
    trailing = {t.start[0] for t in tokens
                if t.type == tokenize.COMMENT and t.line.strip() != t.string.strip()}
    logical, start = [], None
    skip = (tokenize.NL, tokenize.COMMENT, tokenize.INDENT, tokenize.DEDENT, tokenize.ENCODING, tokenize.ENDMARKER)
    for t in tokens:
        if start is None and t.type in skip:
            continue
        if start is None:
            start = t.start[0]
        if t.type == tokenize.NEWLINE:
            logical.append((start, t.start[0]))
            start = None
    missing = []
    for s, e in logical:
        first = lines[s - 1].strip()
        if first.startswith(('"""', "'''", 'r"""')):
            continue
        if any(n in trailing for n in range(s, e + 1)):
            continue
        k = s - 2
        while k >= 0 and not lines[k].strip():
            k -= 1
        if k >= 0 and lines[k].strip().startswith("#"):
            continue
        missing.append(f"line {s}: {first[:70]}")
    return missing


def check(path):
    """Return a list of problems found in one notebook."""
    nb = nbformat.read(path, as_version=4)
    problems = []
    head = nb.cells[0].source
    if not head.startswith("# ") or SERIES not in head:
        problems.append("cell 0: missing title or series line")
    if "## Study guide" not in nb.cells[1].source:
        problems.append("cell 1: missing Study guide")
    for i, cell in enumerate(nb.cells):
        if has_local_path(cell.source):
            problems.append(f"cell {i}: local file path in source")
        if cell.cell_type != "code":
            continue
        src = "\n".join("pass  # magic" if l.lstrip().startswith(("!", "%")) else l for l in cell.source.splitlines())
        ast.parse(src)
        problems += [f"cell {i}, {m}: no comment" for m in uncovered_lines(src)]
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                problems.append(f"cell {i}: saved error output")
            text = str(out.get("text", "")) + str(out.get("data", {}).get("text/plain", ""))
            if has_local_path(text):
                problems.append(f"cell {i}: local file path in output")
    return problems


def main():
    failed = 0
    for path in NOTEBOOKS:
        problems = check(path)
        print(f"{'ok' if not problems else 'FAILED':6s} {path.name}")
        for p in problems[:10]:
            print("       ", p)
        failed += bool(problems)
    print(f"\n{len(NOTEBOOKS) - failed} of {len(NOTEBOOKS)} notebooks passed the static checks.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
