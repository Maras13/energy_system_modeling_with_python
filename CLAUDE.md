# Energy System Modelling with Python — course repo

This repo is a teaching course. Most work here is writing or fixing course material
(lecture notebooks, exercises, solutions, READMEs), not building a product. Optimise for
what a learner sees: clear explanations, small runnable steps, and results that are correct.

The full schedule, levels and checkpoints are in `COURSE_PLAN.md`. Read it before adding
material, so new lessons land in the right week and folder.

## Learner profile (shapes every lesson)
- Strong: Python, pandas, SQL, APIs, data pipelines, Git, visualization. Don't re-teach these.
- No electrical engineering background: build circuits and power concepts from first principles.
- Maths studied but rusty: refresh exactly the maths a topic needs, right before it is needed.
- Studies ~40 h/week; goal is research/professional-level skill and a GitHub portfolio.

## Course structure
| Folder | Topic | Core tools |
|---|---|---|
| `00_foundations` | Electrical engineering (EE-1…3) + targeted maths (Maths-1…3) | NumPy, SciPy |
| `01_python_for_energy_modelling` | Python, data engineering, time series, PyPSA introduction | pandas, PyPSA |
| `02_electricity_markets` | Merit order, market clearing, European market design | pandas, PyPSA |
| `03_linear_programming` | LP, duality, unit commitment, storage, rolling horizon | Linopy + HiGHS, PyPSA, Pyomo (comparison) |
| `04_power_flow_analysis` | Power flow, congestion, nodal prices, reliability, stability | NumPy (own solvers), PyPSA, pandapower, ANDES |
| `05_system_expansions` | Energy economics, capacity expansion, scenarios | PyPSA |
| `06_energy_forecasting` | Load, renewable and price forecasting | statsmodels, scikit-learn / gradient boosting |
| `07_advanced_optimization` | Stochastic, robust, multi-objective, decomposition | Linopy, PyPSA |
| `08_final_project` | Integrated Croatia / SE-Europe study | all of the above |

## Case study and data
- Focus: Croatia and neighbours (HR, SI, HU, BA, RS; IT and AT as price references), within Europe.
- Data: ENTSO-E Transparency Platform (API), Open Power System Data, Renewables.ninja,
  PyPSA technology-data, national TSOs and exchanges. Always cite the source and retrieval date.
- Expect gaps in ENTSO-E data for smaller and non-EU zones; detecting and handling them is part
  of the teaching, not something to hide.

## PyPSA is the backbone — never a black box
- One running model grows across modules: single bus → dispatch → opened-up LP → meshed network
  → investment. Reuse the previous lesson's network where possible.
- Whenever PyPSA produces a result, show the underlying formulation (Linopy `n.model`) or
  reproduce it by hand at least once per concept.
- Be precise about PyPSA's limits: `n.optimize()` uses a linearised network (no voltage
  magnitudes, no reactive power, no losses by default); AC physics comes from `n.pf()`.
  PyPSA has no Gauss-Seidel or Fast Decoupled solver (pandapower does; learners also write their own).

## Teaching approach (keep this consistent)
- **Build the same model several times, each time more complex.**
- **Connect every maths concept to an energy concept**: variables = generation,
  objective = total cost, constraints = physical limits, dual of the demand constraint = price.
- **Show that methods agree** when they should, and explain why they differ when they don't.
- First principles: derive, then a worked example by hand, then code, then validation.
- Every notebook validates its own results (units, energy balance, a reference value).

## Conventions
- Lecture notebooks are numbered (`01_ee1_circuits_from_zero.ipynb`). Exercises go in an `exercise/`
  subfolder with matching names; solutions in `exercise/solutions/<name>_solution.ipynb`.
- Single-digit numbers always get a leading zero (`04`, not `4`).
- Units: MW for power, MWh for energy, €/MWh for prices and marginal costs, € for total cost,
  hours for time steps; V, A, Ω, S, W in the foundations. Say the unit in every label and printout.
- Solver: HiGHS (`pip install highspy`), called via `solve(solver_name="highs")`.
- Environment: `requirements.txt` at the repo root is the tested course-wide environment. pandapower
  requires pandas ~=2.3 and PyPSA >= 1.3 requires pandas >= 3, so the course uses PyPSA 1.2.x with
  pandas 2.3. Check a fresh install with `pip install --dry-run -r requirements.txt` and re-run all
  notebooks and the M1.6 template tests before changing any pin.
- Data: small and transparent in lessons; real data in projects, in a `data/` folder; never
  hard-code an absolute path.
- Language: English, friendly, second person ("you"), short paragraphs.

## Skills in this repo (`.claude/skills/`)
- `esm-lecture-builder` – turn a plan into a lecture notebook in the course style.
- `esm-exercise-builder` – write an exercise notebook + solution and prove the solution runs.
- `esm-model-checker` – solve a small dispatch/expansion case and sanity-check the results.

Before handing over any notebook, execute it top to bottom. A notebook that has never run
is not finished.
