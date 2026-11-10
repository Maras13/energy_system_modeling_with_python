"""Build a student exercise notebook from a solution notebook, and prove the solution works.

    python build_exercise.py path/to/exercise/solutions/02_lp_dispatch_solution.ipynb
    python build_exercise.py SOLUTION.ipynb --student path/to/exercise/02_lp_dispatch.ipynb

Steps:
 1. Execute the solution notebook top to bottom (fresh kernel, cwd = its folder).
    Any error or failed assert -> stop and report the cell. The executed solution
    (with outputs) is saved back in place, so the answer key shows real results.
 2. Make the student version: in code cells, everything between
        ### BEGIN SOLUTION
        ### END SOLUTION
    is replaced by an indented `...  # YOUR CODE HERE`. In markdown cells, text between
        <!-- BEGIN SOLUTION -->  and  <!-- END SOLUTION -->
    becomes "*Your answer here.*". Cells tagged `solution-only` are dropped.
    Outputs are cleared.
 3. Execute the student version and confirm the tests actually test something:
    at least one cell with a solution block must fail. If every cell passes with the
    answers removed, the asserts are too weak (or the solution markers are missing).

Exit code 0 = solution runs, student notebook written, tests bite.
"""
from __future__ import annotations

import argparse
import copy
import os
import re
import sys

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

CODE_BLOCK = re.compile(r"^([ \t]*)### BEGIN SOLUTION[^\n]*\n.*?^[ \t]*### END SOLUTION[^\n]*(\n|$)",
                        re.S | re.M)
MD_BLOCK = re.compile(r"<!--\s*BEGIN SOLUTION\s*-->.*?<!--\s*END SOLUTION\s*-->", re.S)


def execute(nb, cwd, allow_errors=False, timeout=300):
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3", allow_errors=allow_errors,
                            resources={"metadata": {"path": cwd}})
    client.execute()
    return nb


def strip_solutions(nb):
    student = copy.deepcopy(nb)
    keep, n_blocks = [], 0
    for cell in student.cells:
        if "solution-only" in cell.get("metadata", {}).get("tags", []):
            continue
        src = cell.source
        if cell.cell_type == "code":
            src, k = CODE_BLOCK.subn(lambda m: f"{m.group(1)}...  # YOUR CODE HERE{m.group(2)}", src)
            n_blocks += k
            cell.outputs, cell.execution_count = [], None
        elif cell.cell_type == "markdown":
            src, k = MD_BLOCK.subn("*Your answer here.*", src)
            n_blocks += k
        cell.source = src
        keep.append(cell)
    student.cells = keep
    return student, n_blocks


def default_student_path(sol_path):
    folder, name = os.path.split(os.path.abspath(sol_path))
    name = re.sub(r"_solutions?(?=\.ipynb$)", "", name)
    parent = os.path.dirname(folder) if os.path.basename(folder) == "solutions" else folder
    return os.path.join(parent, name)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build + verify an exercise from its solution notebook.")
    ap.add_argument("solution")
    ap.add_argument("--student", help="output path (default: ../<name without _solution>.ipynb)")
    ap.add_argument("--timeout", type=int, default=300, help="seconds per cell")
    a = ap.parse_args(argv)

    sol_path = os.path.abspath(a.solution)
    cwd = os.path.dirname(sol_path)
    nb = nbformat.read(sol_path, as_version=4)

    print(f"[1/3] Executing solution: {sol_path}")
    try:
        execute(nb, cwd, timeout=a.timeout)
    except CellExecutionError as e:
        msg = str(e).strip().splitlines()
        print("FAILED: the solution notebook does not run.\n" + "\n".join(msg[-25:]))
        return 1
    nbformat.write(nb, sol_path)
    n_code = sum(c.cell_type == "code" for c in nb.cells)
    print(f"      ok - {n_code} code cells ran without errors; outputs saved to the solution.")

    student, n_blocks = strip_solutions(nb)
    if n_blocks == 0:
        print("FAILED: no '### BEGIN SOLUTION' / '<!-- BEGIN SOLUTION -->' markers found.")
        return 1
    stu_path = os.path.abspath(a.student) if a.student else default_student_path(sol_path)
    os.makedirs(os.path.dirname(stu_path), exist_ok=True)
    nbformat.write(student, stu_path)
    print(f"[2/3] Student notebook written: {stu_path} ({n_blocks} answer block(s) removed)")

    print("[3/3] Checking that the tests catch an empty answer ...")
    probe = execute(copy.deepcopy(student), os.path.dirname(stu_path), allow_errors=True, timeout=a.timeout)
    stub_cells, failing = 0, 0
    for c in probe.cells:
        if c.cell_type != "code" or "YOUR CODE HERE" not in c.source:
            continue
        stub_cells += 1
        if any(o.get("output_type") == "error" for o in c.get("outputs", [])):
            failing += 1
    # errors usually surface in the assert cell after the stub, so also count those
    errors_total = sum(any(o.get("output_type") == "error" for o in c.get("outputs", []))
                       for c in probe.cells if c.cell_type == "code")
    if errors_total == 0:
        print("FAILED: with the answers removed every cell still passes - the asserts don't test the answers.")
        return 1
    print(f"      ok - {errors_total} cell(s) fail without the answers ({stub_cells} stub cell(s)); tests bite.")
    print("DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
