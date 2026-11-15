# Portfolio project P2 — South-East Europe: a zonal market model against real prices

**When:** weeks 4–5 of the course plan (about 35 of the module's 80 hours), after M2.1–M2.3.
**Builds on:** M2.1 (clearing and welfare), M2.2 (price formation, capture prices), M2.3 (market
coupling, congestion income, real HR/SI/HU prices), and your P1 repository and its structure (M1.6).
Start from a copy of your P1 repository or of
[`../01_python_for_energy_modelling/11_project_structure/template/`](../01_python_for_energy_modelling/11_project_structure/template/).
**Needs:** an ENTSO-E API token in `.env` (see M1.1).

## The task

Build a public GitHub repository with a **zonal PyPSA market model** of Croatia and at least two
neighbouring bidding zones (Slovenia and Hungary at minimum; Austria or northern Italy as price
references if you like), run it for real weeks, and **compare its prices with the real day-ahead
prices**. Pick one question (or propose your own of similar size):

1. **How well does a merit-order model explain regional prices?** For one winter and one summer week
   (or one month), how closely do your modelled HR, SI and HU prices follow the real ones, and in which
   hours and for which reasons do they fail?
2. **What are Croatia's interconnectors worth?** How often do HR prices converge with SI and HU in
   reality and in your model, and how do congestion income and welfare change as you vary the
   transfer capacities?
3. **When and why do Croatian prices go negative?** Using real data for spring and summer, when do
   negative prices occur in HR, how do they relate to solar output, hydro and neighbouring prices,
   and can your model reproduce them?

Write the question as one sentence at the top of your README.

## Required components

| Area | What is required |
|---|---|
| **Data** | Real ENTSO-E data for every modelled zone and week: day-ahead prices (`query_day_ahead_prices`), load (`query_load`) and generation by type (`query_generation`); cross-border physical flows (`query_crossborder_flows`) for the borders you model. Prices after September 2025 come in **15-minute** steps — convert consistently and document how. Time zones and the DST weeks handled explicitly. Every dataset in `data/README.md` (source, retrieval date, licence, processing). |
| **Model** | PyPSA zonal model built from YAML: one bus per zone, generators per technology with cited or clearly stated costs, real load and renewable output, and bidirectional links for the borders. Transfer capacities from a cited source (ENTSO-E transfer capacity data where available) or justified proxies — capacity data may be missing for borders under flow-based allocation (such as HR–HU), and then the observed maximum flows are a reasonable, stated proxy. At least **two scenarios** as separate config files. |
| **Validation** | The template's tests plus at least **four of your own**: (1) **model vs real prices** per zone — mean absolute error, correlation and the share of hours with converged prices, reported in the README; (2) a **property test** from M2.3 — more capacity on a border never lowers welfare and never widens the price spread **across that border** (spreads on *other* borders can widen — a random search on M2.3's network finds such a case, so do not test for that); (3) a **coupling check** — your zonal prices equal the duals of the zone balances and congestion income + surpluses = welfare (M2.3's identity), on a small fixed case; (4) a **data-quality test** — e.g. the 15-minute-to-hourly conversion keeps energy, no duplicated or missing hours after DST. |
| **Figures** | At least **four**, following the M1.5 conventions: modelled vs real prices over time for each zone, price duration curves (model and real), a figure on convergence or spreads between zones, and one figure answering your question directly. SVG in `figures/`, shown in the README. |
| **README** | Question and answer first, then method (the coupling LP in a few lines), data, validation (with the error metrics), **where and why the model differs from reality**, limitations, and how to reproduce with exact package versions. |
| **Reproducibility** | One command (or a short documented sequence) downloads/prepares the data and reproduces every result; no tokens, absolute paths or large data in Git; your M1.6 `audit_project` passes. |

## Expect your model to be wrong — and explain it

A cost-based merit-order model will **not** reproduce real prices hour by hour, and that is fine.
The strongest projects quantify the gap and attribute it. Typical reasons, each worth testing or at
least discussing:

- **Hydro is not a fixed-cost plant.** Reservoir operators offer at the value of keeping water for
  later (its opportunity cost), not at zero — so prices in hydro-rich hours are higher than a model
  with zero-cost hydro predicts (Module 03 models this properly).
- **Fuel and CO₂ prices move.** Use values for your weeks, cited, and show how sensitive the result is.
- **Borders are flow-based.** Fixed transfer capacities miss loop flows and the Core region's actual
  limits (M2.3, Module 04).
- **Neighbours outside your model.** Austria, Italy, Bosnia and Herzegovina and Serbia trade with your
  zones; treating them as fixed-price imports or exports is a choice to justify.
- **Scarcity and bidding behaviour.** Real offers include start-up costs, mark-ups and scarcity
  pricing that a linear cost model does not have.

## Out of scope (say so in *Limitations*)

Flow-based capacity calculation with PTDFs (Module 04), reservoir and storage optimisation, unit
commitment and ramping (Module 03), investment decisions (Module 05), intraday and balancing markets,
and price forecasting. Your model explains mechanisms and their limits; it does not forecast prices.

## How P2 is assessed

| Criterion | Pass | Strong |
|---|---|---|
| Question & answer | Clear question, answered with evidence | Answer quantified, with error metrics against real prices and the key figure on top |
| Data | Real ENTSO-E data for all zones, validated, provenance recorded | 15-minute data, DST and missing values handled and explained; physical flows compared with the model's flows |
| Model | Zonal model from config, two scenarios, runs | Scenarios isolate one effect each (e.g. capacity, CO₂ price, hydro offer price) |
| Validation | Required tests pass; error metrics reported | The model–reality gap is attributed to specific causes, with at least one tested hypothesis |
| Communication | Four correct figures, complete README | A reviewer understands the result and its limits in one minute |
| Reproducibility | Fresh clone → `pytest` and results | Versions pinned, audit clean, tagged release `v1.0` |

## Submission

Push the repository, tag it `v1.0`, and send me the link with two sentences: the question and the
answer — including how far your model's prices are from the real ones. As with P1, I will review it
like a consultancy reviewer or research supervisor and return a list of what to fix before it goes
into your portfolio.
