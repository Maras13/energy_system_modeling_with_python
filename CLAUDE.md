# Energy System Modelling with Python — course repo

This repo is a teaching course. Most work here is writing or fixing course material
(lecture notebooks, exercises, solutions, READMEs), not building a product. Optimise for
what a student sees: clear explanations, small runnable steps, and results that are correct.

## Course flow
Five modules that build on each other. Later modules reuse functions and data from earlier ones.

| Folder | Topic | Core tools |
|---|---|---|
| `01_python_for_energy_modelling` | setup, bash, Git, Python basics → advanced, pandas | Python, pandas, Jupyter |
| `02_electricity_markets` | demand, supply curves, merit order, market clearing | pandas, matplotlib |
| `03_linear_programming` | LP for dispatch, shadow prices, storage, sensitivity | Linopy + HiGHS |
| `04_power_flow_analysis` | networks, DC power flow, line limits, congestion | PyPSA / Linopy |
| `05_system_expansions` | capacity expansion, investment vs. operation | PyPSA / Linopy |

The detailed plan for each module lives in that module's `readme.md`. Read it before writing
material for the module. Some plans are screenshots; if you cannot read them, ask for the text.

## Teaching approach (keep this consistent)
- **Build the same model several times, each time more complex.** Module 03 example:
  pen-and-paper 2-plant LP → same LP in Linopy → 24 h with ramping and storage →
  sensitivity analysis and a 1-page policy brief.
- **Connect every maths concept to an energy concept**: variables = generation,
  objective = total cost, constraints = physical limits, dual of the demand constraint = price.
- **Show that methods agree** when they should (e.g. LP dispatch == merit-order dispatch
  for a single hour without extra constraints). Students trust the solver when they see this.

## Conventions
- Lecture notebooks: numbered, e.g. `02_lp_in_linopy.ipynb`. Exercises go in an `exercise/`
  subfolder next to the lecture, with matching numbers. Solutions in `exercise/solutions/`.
- Single-digit numbers always get a leading zero (`04`, not `4`).
- Units: MW for power, MWh for energy, €/MWh for prices and marginal costs, € for total cost,
  hours for time steps. Say the unit in every axis label, column name, and printed result.
- Solver: HiGHS (`pip install highspy`), called via `model.solve(solver_name="highs")`.
- Data: small, hand-made, or clearly sourced. Put files in a `data/` folder in the module;
  never hard-code an absolute path.
- Language: English, friendly, second person ("you"), short paragraphs.

## Skills in this repo (`.claude/skills/`)
- `esm-lecture-builder` – turn a module plan into a lecture notebook in the course style.
- `esm-exercise-builder` – write an exercise notebook + solution and prove the solution runs.
- `esm-model-checker` – solve a small dispatch/expansion case and sanity-check the results.

Before handing over any notebook, execute it top to bottom. A notebook that has never run
is not finished.
