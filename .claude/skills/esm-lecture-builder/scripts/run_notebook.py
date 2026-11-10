"""Execute a notebook top to bottom in a fresh kernel and save its outputs.

    python run_notebook.py path/to/lecture.ipynb [--allow-errors]

Cells tagged `raises-exception` may fail on purpose (e.g. a lecture that shows an error).
Prints a one-line summary per failing cell and exits 1 if anything unexpected failed.
"""
import argparse
import os
import sys

import nbformat
from nbclient import NotebookClient


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("notebook")
    ap.add_argument("--timeout", type=int, default=300)
    a = ap.parse_args(argv)
    path = os.path.abspath(a.notebook)
    nb = nbformat.read(path, as_version=4)
    NotebookClient(nb, timeout=a.timeout, kernel_name="python3", allow_errors=True,
                   resources={"metadata": {"path": os.path.dirname(path)}}).execute()
    bad = []
    for i, c in enumerate(nb.cells):
        if c.cell_type != "code":
            continue
        errs = [o for o in c.get("outputs", []) if o.get("output_type") == "error"]
        if errs and "raises-exception" not in c.get("metadata", {}).get("tags", []):
            bad.append(f"cell {i}: {errs[0]['ename']}: {errs[0]['evalue'][:200]}")
    nbformat.write(nb, path)
    n = sum(c.cell_type == "code" for c in nb.cells)
    if bad:
        print(f"FAILED: {len(bad)} of {n} code cells raised errors:\n  " + "\n  ".join(bad))
        return 1
    print(f"OK: {n} code cells ran without unexpected errors; outputs saved to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
