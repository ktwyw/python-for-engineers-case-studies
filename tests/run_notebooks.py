"""Execute every notebook from top to bottom and report any error.

Usage (from the repository root):
    python tests/run_notebooks.py                 # all notebooks
    python tests/run_notebooks.py 05 08           # only notebooks whose names start with 05 or 08

Each notebook runs in its own temporary folder, so files it writes (CSV files, figures, GIFs)
do not end up in the repository. The saved notebooks are not modified.
"""
import shutil
import sys
import tempfile
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))


def run(path):
    """Execute one notebook in a fresh temporary folder; return a list of error descriptions."""
    nb = nbformat.read(path, as_version=4)
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(path, tmp)
        client = NotebookClient(nb, timeout=900, kernel_name="python3", resources={"metadata": {"path": tmp}})
        try:
            client.execute()
        except CellExecutionError as err:
            return [str(err).strip().splitlines()[-1]]
    errors = []
    for i, cell in enumerate(nb.cells):
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                errors.append(f"cell {i}: {out['ename']}: {out['evalue']}")
    return errors


def main():
    prefixes = sys.argv[1:]
    selected = [p for p in NOTEBOOKS if not prefixes or p.name.startswith(tuple(prefixes))]
    failed = 0
    for path in selected:
        start = time.time()
        errors = run(path)
        status = "ok" if not errors else "FAILED"
        print(f"{status:6s} {time.time() - start:6.1f} s  {path.name}")
        for e in errors:
            print("       ", e)
        failed += bool(errors)
    print(f"\n{len(selected) - failed} of {len(selected)} notebooks ran without errors.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
