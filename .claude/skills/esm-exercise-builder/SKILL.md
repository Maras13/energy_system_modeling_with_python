---
name: esm-exercise-builder
description: Create exercise notebooks with matching, verified solutions for the energy system modelling course — merit order, market clearing, linear programming with Linopy/HiGHS, shadow prices, storage, power flow, capacity expansion, or Python/pandas practice with energy data. Writes the solution notebook with marked answer blocks and assert-based checks, runs it, and generates the student version automatically, so the answer key always runs. Use this whenever someone asks for exercises, practice tasks, homework, a challenge, a quiz-style notebook, "tasks for week N", or a solution/answer key for a module, and when fixing an existing exercise whose solution is broken or missing.
---

# Exercise builder

Students lose trust fast when an answer key is wrong or crashes. So every exercise here is
written **solution-first**: one solution notebook is the single source of truth, it is executed
before anything ships, and the student notebook is generated from it by a script.

## Before writing
1. Read the module's `readme.md` and the lecture notebook(s) the exercise belongs to.
   Exercises practise what the lecture taught — same names, data, and conventions — and stretch
   it a little in the Challenge. Don't require tools the course hasn't introduced yet
   (see `../esm-lecture-builder/references/course_outline.md`).
2. Read `references/exercise_format.md` (structure, solution markers, asserts).
3. Decide the file name from the lecture: lecture `02_lp_in_linopy.ipynb` →
   `exercise/02_lp_in_linopy.ipynb` (student) and `exercise/solutions/02_lp_in_linopy_solution.ipynb`.

## Write the solution notebook
- Build it with `nbformat` in a small Python script (easier to get JSON right than hand-editing),
  saved at `exercise/solutions/<name>_solution.ipynb`.
- Warm-ups → Core → Challenge. Each task: markdown prompt, a stub with the solution between
  `### BEGIN SOLUTION` / `### END SOLUTION`, then a separate cell with asserts.
- Energy tasks need numbers that make physical sense: plausible marginal costs (€/MWh),
  capacities (MW), demand (MW), efficiencies (< 1). Keep data tiny so it can be checked by hand.
- Interpretation questions ("Why is the price 80 €/MWh in hour 3?") get a markdown answer
  inside `<!-- BEGIN SOLUTION -->` … `<!-- END SOLUTION -->`.

## Build and verify (always)
```bash
pip install nbclient nbformat ipykernel linopy highspy   # once
python <this-skill>/scripts/build_exercise.py exercise/solutions/<name>_solution.ipynb
```
The script (1) executes the solution and saves its outputs, (2) writes the student notebook
with answers replaced by `...  # YOUR CODE HERE`, (3) runs the student version to prove the
asserts fail without answers. If any step fails, fix the solution or the asserts and rerun —
don't hand over a notebook that hasn't passed.

## Check the modelling, not just the code
A solution can run and still be wrong. For any task that solves a dispatch, storage, or
expansion model, also run the **esm-model-checker** skill on the solution's case before
writing the asserts: the asserts then lock in numbers that are known to be correct.

## Hand-over
Report: the two file paths, the task list (one line each, with difficulty), what the build
script printed (cells run, answer blocks, "tests bite"), and the model-check result if used.
Mention anything a teacher should know (e.g. "Task 6 has two valid answers at a capacity step").
