# Notebook style — match the existing course notebooks

These patterns come from the Module 01 notebooks (e.g. `Functions/2_Function_Definitions.ipynb`).
Students have seen them for weeks; keeping them makes new modules feel familiar.

## Cell sequence of a lecture
1. `# <Title>` — one markdown cell, nothing else in it.
2. `## Objectives` — its own cell.
3. One markdown cell: "At the end of this notebook you should be able to:" + 2–5 bullets,
   then 1–3 sentences of motivation that connect to the previous lecture.
4. Teaching blocks, repeated (see below).
5. `## Check your understanding` — its own cell.
6. 2–4 markdown cells, each starting with a **bold title**, holding numbered questions
   that ask the student to predict, change, then run something.
7. A final empty code cell.

## A teaching block
- Markdown: explain one idea in 2–5 short sentences. Name the energy meaning.
- Code: the smallest cell that shows it (often under 10 lines). One idea per cell.
- Code: 1–3 tiny follow-up calls that vary an input, so students see the effect.
- Markdown: say what just happened and why ("Notice that…", "This is because…").
- Leave an empty code cell after important blocks so students can experiment.

Use `### Sub-headings` to group 3–6 blocks into a section. No more than ~45 cells total;
split a longer topic into two notebooks.

## Writing
- Second person, friendly, plain English. Short paragraphs.
- **Bold** key terms the first time they appear. Use `code formatting` for names.
- Every number shown to students carries a unit (MW, MWh, €/MWh, €).
- Prefer a small table (pandas DataFrame) over printing raw objects.
- When a solver result appears, interpret it in one sentence of energy language
  ("Lignite runs at full 800 MW because it is the cheapest plant").

## Code
- Imports in one cell near the top, after the objectives.
- Data as small DataFrames defined in the notebook, or loaded from `data/` with a
  relative path. Show the data before using it.
- Linopy: `m = linopy.Model()`, `m.add_variables`, `m.add_constraints(..., name=...)`,
  `m.add_objective`, `m.solve(solver_name="highs")`. Name every constraint so its dual
  can be read with `m.constraints["name"].dual`.
- Name pandas indexes that become Linopy coordinates (`plants.index.name = "plant"`).
  Unnamed ones show up as `dim_0` in every table students see.
- Show the solver log at most once (the first solve, so students see what a solver reports).
  After that pass `output_flag=False` to `m.solve(...)` to keep outputs readable.
- Plots: matplotlib, one figure per cell, labelled axes with units, a title.
- No hidden helper modules — if a helper is needed, define it in the notebook and explain it.
