---
name: esm-lecture-builder
description: Write lecture/teaching notebooks for the energy system modelling with Python course, in the course's own style (title, objectives, short explain-then-run blocks, check-your-understanding questions). Turns a module plan, outline, screenshot, or topic list into a runnable Jupyter notebook for modules 01–05 — electricity markets and merit order, linear programming with Linopy/HiGHS, shadow prices, storage and ramping, sensitivity analysis, power flow, capacity expansion. Use this whenever someone asks for a lecture, lesson, teaching notebook, class material, "the notebook for week N", or wants a module plan turned into content, even if they don't say "lecture".
---

# Lecture builder

The goal is a notebook a student can work through alone, top to bottom, and come out
understanding one idea well — in the same style as the notebooks they already know.

## 1. Gather the plan
- Read `CLAUDE.md` at the repo root and the target module's `readme.md`.
- Read `references/course_outline.md` to see what students already know and what comes later.
- Look at the lecture before this one (if it exists) and reuse its data, function names and
  variable names — continuity matters more than elegance.
- If the plan is a screenshot you can't read, or the scope is unclear, ask for the text or the
  week. Don't guess at the content of an entire module.

## 2. Plan the notebook (show the plan before writing if the request is vague)
- One notebook = one core idea, 30–60 minutes of student time, roughly 25–45 cells.
  Split bigger topics into numbered parts.
- Write 2–5 objectives as observable skills ("formulate a two-plant dispatch LP in Linopy",
  not "understand LPs").
- Sequence: intuition → tiny example by hand or in a table → code → vary an input →
  interpret in energy terms → connect to what comes next.
- Where the course plan says to compare methods (e.g. LP vs. merit order), make the
  comparison explicit and show the results side by side.

## 3. Write it
- Follow `references/notebook_style.md` exactly for cell order, headings, tone and code style.
- Build the notebook with `nbformat` in a short Python script (reliable JSON), save it in the
  module folder with the next number (`03_linear_programming/02_lp_in_linopy.ipynb`).
- Data: small and transparent. Define it in the notebook or put a CSV in the module's `data/`.
- Every result shown gets a one-sentence energy interpretation and units.

## 4. Verify (never skip)
1. Run it: `python <this-skill>/scripts/run_notebook.py <notebook>` — executes in a fresh
   kernel and saves outputs. Fix and rerun until it passes. Tag cells that fail on purpose
   with `raises-exception`.
2. If the notebook solves a dispatch, storage or expansion model, run the **esm-model-checker**
   skill on the same data. If the notebook's numbers disagree with the reference, the
   notebook is wrong — fix it before handing over.
3. Re-read the explanations against the actual outputs: every "notice that…" must match
   what the cells really print.

## 5. Hand over
Report: file path, the objectives, a section outline (one line per section), the run
result, the model-check result if used, and suggestions for the matching exercise
(the **esm-exercise-builder** skill can write it).
