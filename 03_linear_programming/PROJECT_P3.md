# Portfolio project P3 — Croatian dispatch: PyPSA reproduced by hand

**When:** weeks 8–9 of the course plan (about 40 of the module's 160 hours), after lessons 2–9.
**Builds on:** lessons 2–3 (LP in Linopy, multi-period dispatch, KKT prices), 4 (inside PyPSA,
custom constraints), 5 (sensitivity, adjusted and resource costs), 6 (unit commitment), 7 (reservoirs,
water values, pumped hydro), 8 (demand response), 9 (rolling horizon); and your P1/P2 repository.
Start from a copy of your P2 repository or of
[`../01_python_for_energy_modelling/11_project_structure/template/`](../01_python_for_energy_modelling/11_project_structure/template/).
**Needs:** an ENTSO-E API token in `.env` (see M1.1) for the real-data parts.
**Closes the week-9 checkpoint:** a dual derived by hand, and PyPSA's objective and prices reproduced
by your own Linopy model to 10⁻⁶.

## The task

Build a public GitHub repository with **two implementations of the same dispatch model** of a
Croatia-sized system for at least one real week — **your own Linopy model** and a **PyPSA model** built
from the same configuration — show that they agree, and use them to answer one question. The model
must include at least: thermal plants with ramp limits, a **reservoir hydro plant with inflow and a
water balance**, and **one form of flexibility** (pumped storage, a battery or flexible demand). Pick
one question (or propose your own of similar size):

1. **What is Croatian reservoir hydro worth, and when should it run?** Compute the water value for
   your week, compare an optimal schedule with a zero-cost offer and with the real reservoir
   generation from ENTSO-E, and explain the differences.
2. **What does inflexibility cost?** Add minimum stable output and start-up costs (unit commitment,
   lesson 6) and ramp limits, and measure their effect on cost, curtailment, prices and uplift.
3. **Which flexibility helps Croatia most in a sunny week?** Compare pumped storage, a battery and
   flexible demand of similar size: savings, effect on prices and curtailment, and the break-even
   investment cost each saving would justify (lesson 5).

Write the question as one sentence at the top of your README.

## Required components

| Area | What is required |
|---|---|
| **Data** | Real ENTSO-E data for Croatia (`10YHR-HEP------M`) for your week(s): load (`query_load`), generation by type (`query_generation` — including "Hydro Water Reservoir", "Hydro Pumped Storage" and "Hydro Run-of-river and pondage") and installed capacities (`query_installed_generation_capacity`). Reservoir **inflows are not published**: estimate them and say how — for example from reservoir generation plus the change in filling level (`query_aggregate_water_reservoirs_and_hydro_storage`, weekly, if published for HR) or as a clearly stated proxy. Costs and the CO₂ price cited or clearly stated. Imports and exports either modelled as priced offers (P2) or fixed to observed flows — a choice to justify. Every dataset in `data/README.md` (source, retrieval date, licence, processing); 15-minute data and DST handled as in P2. |
| **Own model** | A Linopy LP written by you, built from the YAML configuration: hourly balance, generator bounds, ramp limits, reservoir water balance with inflow, spillage and a start/end level, your flexibility option. Prices read as duals, with Linopy's sign conventions handled and documented. If you add unit commitment (question 2), prices from the **fixed-commitment LP** (lesson 6). |
| **PyPSA model** | The same system in PyPSA from the same configuration (`StorageUnit` with `inflow` for the reservoir, `ramp_limit_up/down`, etc.); custom rules through `extra_functionality` where PyPSA has no attribute (lesson 4). |
| **Validation** | The template's tests plus at least **five of your own**: (1) **the checkpoint test** — own objective and *every* hourly price equal PyPSA's to a relative tolerance of 10⁻⁶; (2) **a dual by hand** — a 2-plant, 2-hour case of your model whose prices and one ramp or storage dual you derive on paper (in `docs/dual_by_hand.md`) and the test reproduces; (3) **a KKT check** — in every hour where a unit runs strictly between its limits, the price equals its marginal cost plus its ramp terms (lesson 3), and where the reservoir runs between its limits the price equals the water value (lesson 7); (4) **an accounting identity** — what consumers pay equals what generators and storage receive (lesson 5); (5) one test of your own on the part you trust least. |
| **Figures** | At least **four**, following the M1.5 conventions: a dispatch stack for the week, modelled prices (with the real day-ahead price for reference), the reservoir level and water value over the week, and one figure answering your question directly. SVG in `figures/`, shown in the README. |
| **README** | Question and answer first, then the model in equations (the objective and each constraint family, a few lines each), data and inflow estimate, validation (including the checkpoint result), **what the model leaves out**, and how to reproduce with exact package versions. |
| **Reproducibility** | One command (or a short documented sequence) reproduces every result; no tokens, absolute paths or large data in Git; your M1.6 `audit_project` passes. |

## Traps you met in Module 03 — and must avoid here

- **Zero prices after a MILP.** PyPSA reports 0 €/MWh in every hour after unit commitment, without a
  warning (lesson 6). Never read `marginal_price` from a MILP; use the fixed-commitment LP.
- **`n.objective` after a rolling horizon** is only the last window's cost, and
  `optimize_with_rolling_horizon` changes `state_of_charge_initial` (lesson 9). Compute totals from the
  dispatch and build a fresh network for every run.
- **Degenerate optima.** Equally cheap schedules exist (lessons 3 and 9): compare models by objective,
  prices and adjusted costs, not by individual dispatch values.
- **Leftover water.** A model that ends with a different reservoir level than it started with is not
  comparable to one that does not — value the difference at the water value or require the start
  level at the end (lesson 9).
- **Cost versus transfers.** Carbon payments and support payments are transfers; report resource cost
  and consumer cost separately where they matter (lesson 5).

## Out of scope (say so in *Limitations*)

Network constraints inside Croatia and flow-based cross-border limits (Module 04), investment
optimisation (Module 05 — a break-even calculation as in lesson 5 is in scope), reserves and
balancing markets, uncertainty in inflows and forecasts, and price forecasting.

## How P3 is assessed

| Criterion | Pass | Strong |
|---|---|---|
| Question & answer | Clear question, answered with evidence | Answer quantified and tied to a mechanism from Module 03 (water value, uplift, cannibalisation) |
| Equivalence | Own model and PyPSA agree to 10⁻⁶ on objective and prices | Agreement shown for every scenario, and a constraint PyPSA lacks added and validated in both |
| Duals | Prices read correctly; one dual derived by hand | Prices decomposed into marginal costs, ramp and storage terms with the KKT conditions |
| Data | Real Croatian data, provenance recorded, inflow estimate stated | Inflow estimate checked against reservoir filling data; modelled reservoir use compared with the real one |
| Communication | Four correct figures, complete README | A reviewer understands the result and its limits in one minute |
| Reproducibility | Fresh clone → `pytest` and results | Versions pinned, audit clean, tagged release `v1.0` |

## Submission

Push the repository, tag it `v1.0`, and send me the link with two sentences: the question and the
answer — plus the checkpoint result (the largest price difference between your model and PyPSA). As
with P1 and P2, I will review it like a consultancy reviewer or research supervisor and return a list
of what to fix before it goes into your portfolio.
