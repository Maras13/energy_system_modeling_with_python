---
name: esm-model-checker
description: Solve a small electricity dispatch, storage, or capacity-expansion case with Linopy + HiGHS and sanity-check the results (demand met, capacity and ramp limits, storage energy balance, non-negative cost, cost equals the true optimum, prices match the merit order). Use this whenever an energy system model in this course is written, changed, or produces numbers that will be shown to students — lecture or exercise notebooks for modules 02–05, solution notebooks, merit-order functions, LP dispatch, shadow prices, battery models, sensitivity runs, expansion models — and whenever someone asks "is this result right?", "why is the price X?", or a model gives surprising costs, prices, or dispatch. Also use it to explain results, not only to find bugs.
---

# Energy model checker

A modelling bug in this course is worse than a crash: the notebook runs, prints a number,
and students learn the wrong thing. This skill checks results against physics and economics
using an independent reference model, so mistakes surface before students see them.

## What you get

`scripts/esm_checks.py` (run from this skill's folder, or import it) provides:

- `load_case(path_or_dict)` — reads a small JSON case (generators, demand, optional storage,
  ramping, load shedding, extendable capacity). Run `python esm_checks.py --example` to see the format.
- `solve_reference(case)` — builds and solves the reference LP. Returns dispatch (MW), prices
  (€/MWh, dual of the demand balance), total cost (€), storage results, built capacity.
- `merit_order_dispatch(generators, demand)` — greedy one-hour dispatch with the valid price range.
- `check_results(case, dispatch, prices, total_cost, storage, p_nom, shed, reference)` —
  checks **any** model's output, not just the reference. Returns a table of checks.
- CLI: `python esm_checks.py case.json [--compare results.csv]`. Exit code 0 means all passed.

Needs `linopy`, `highspy`, `pandas`, `xarray` (`pip install linopy highspy`).

## Workflow

1. **Describe the case as JSON.** Translate the notebook's data (plants, marginal costs,
   capacities, demand per hour, availability profiles, storage) into the case format.
   Keep the same names as the notebook so columns line up. Save it next to the notebook
   being checked, e.g. `exercise/solutions/checks/<notebook>_case.json`.
2. **Solve the reference.** `python esm_checks.py case.json`. If it is not optimal, the case
   itself is broken (usually demand above capacity: add `"voll"` for load shedding).
3. **Get the model's results** — run the notebook (or the relevant cells) and collect:
   a dispatch DataFrame (rows = hours 0..T-1, columns = generator names, MW), and where
   available prices, total cost, storage results, built capacity.
4. **Check them** with `check_results(..., reference=ref)` or write them to CSV and use
   `--compare`. Do this in a scratch script, not inside the student notebook.
5. **Report** in plain language (template below). For every failed check, say what is wrong,
   the likely cause in the model, and the fix.

## What the checks mean (use these to diagnose)

| Check fails | Usually means |
|---|---|
| demand met every hour | balance constraint missing or wrong sign; storage charge/discharge flipped |
| generation within available capacity | upper bound missing; availability profile not applied |
| ramp limits respected | ramp constraint missing, or only one direction modelled |
| storage energy balance | efficiency applied on the wrong side; SOC not linked between hours |
| no simultaneous charge and discharge | negative prices or a cost-free loop; often harmless but worth explaining |
| cost **cheaper** than reference | a constraint is missing (the model can do something physics forbids) |
| cost **more expensive** than reference | not solved to optimality, extra constraint, or wrong cost coefficient |
| reported cost ≠ cost recomputed from dispatch | objective built incorrectly (wrong coefficient, units, missing term) |
| price ≠ merit-order price (single-hour/static cases) | wrong dual read, sign convention, or wrong marginal costs |

## Things that are NOT errors (don't flag them)

- **Price at a capacity step.** If demand exactly equals the capacity of the cheapest plants,
  any price between that plant's cost and the next one clears the market; solvers may report
  either end. The checker accepts the whole range — explain this to students if it shows up.
- **Prices above every marginal cost** in expansion models: capital cost is recovered through
  scarcity prices in peak hours. With load shedding, the price can equal the VOLL.
- **Prices with storage/ramping** don't equal a single plant's marginal cost; inter-temporal
  constraints shift them. The merit-order comparison is only run for static cases.
- **Tiny values like -0.0 or 1e-9** are solver tolerance, not negative generation.

## Report format

```
## Model check: <notebook or case name>
**Result:** ✅ all N checks passed | ❌ K of N checks failed
**Reference optimum:** <cost> € — <one sentence on the dispatch, in energy terms>

| Check | Result | Detail |
|---|---|---|
...

**Problems and fixes** (only if something failed)
1. <what is wrong> — <likely cause> — <concrete fix in the notebook's code>

**Worth telling students** (optional): anything surprising but correct, e.g. a price at a
capacity step or a scarcity price.
```

## Notes
- Keep cases small (≤ 48 hours, a handful of plants) — this is a teaching check, not a study.
- For PyPSA models (modules 04–05), read results from `n.generators_t.p`, `n.buses_t.marginal_price`
  and `n.objective`; single-bus cases map directly onto the case format. For multi-bus networks,
  check each bus's balance by hand and use the reference only for single-bus versions.
- If a check fails because the *case* simplifies something the notebook models on purpose,
  say so instead of reporting a bug.
