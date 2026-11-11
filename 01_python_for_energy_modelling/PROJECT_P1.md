# Portfolio project P1 — Croatian electricity: from data to a first dispatch model

**When:** weeks 2–3 of the course plan (about 50 hours), alongside the foundations track.
**Checkpoint (week 3):** your P1 repository runs from a clean environment — `pytest` passes and one
command reproduces every result.
**Builds on:** M1.1 (ENTSO-E data), M1.2 (PyPSA), M1.3 (numerics), M1.4 (weather → profiles),
M1.5 (figures), M1.6 (project structure). Start from a copy of
[`11_project_structure/template/`](11_project_structure/template/).

## The task

Build a public GitHub repository that answers **one concrete question** about the Croatian power
system with real data and a validated single-bus PyPSA model. Pick one question (or propose your own
of similar size):

1. **Who sets the price?** In a winter week and a summer week, which technologies are marginal, and how
   much do imports matter?
2. **What does more solar do?** How do residual load, prices and curtailment change as solar capacity
   grows in a summer week?
3. **How good is the merit order?** How closely does your model's dispatch reproduce actual ENTSO-E
   generation by type for one week, and where does it fail — and why?

Write the question as one sentence at the top of your README. A sharp question beats a large model.

## Required components

| Area | What is required |
|---|---|
| **Data** | Real Croatian load from ENTSO-E (at least the weeks you model) and real wind and solar profiles from weather data (Open-Meteo or Renewables.ninja), each validated and cleaned with your M1.1/M1.4 code. Capacities and costs from a cited source, or stated as stylised assumptions. Every dataset recorded in `data/README.md` (source, retrieval date, licence, processing). |
| **Model** | PyPSA, built from a YAML config; at least **two scenarios** as separate config files. |
| **Validation** | The template's tests plus at least **three of your own**: one comparing against an independent source (data or config, not the model's own output), one **property test** (e.g. more capacity never raises cost), and one data-quality test. All pass. |
| **Figures** | At least **four** figures following the M1.5 conventions (units, local time, one colour per carrier, honest axes), saved as SVG in `figures/` and shown in the README. |
| **README** | Template structure: question and result first, then method (with the LP formulation), validation, limitations, reproduce (with exact package versions). |
| **Reproducibility** | One command (or a short documented sequence) downloads/prepares data and reproduces all results; no secrets, absolute paths or large data in Git. Your M1.6 `audit_project` passes. |

## Out of scope (say so in *Limitations*)

Grid constraints between regions (Module 04), storage and reservoir hydro operation, ramping and
minimum stable output (Module 03), investment decisions (Module 05). Treat imports as a fixed-price
generator unless you have a better justified approach. Your model explains mechanisms; it does not
forecast prices.

## How P1 is assessed

| Criterion | Pass | Strong |
|---|---|---|
| Question & answer | Clear question, answered with evidence | Answer quantified, with the key figure on top and a sanity check against real data (e.g. ENTSO-E prices or generation) |
| Data | Real data, validated, provenance recorded | Data problems found, handled and explained (gaps, DST, units) |
| Model | Runs from config, two scenarios | Scenarios chosen to isolate one effect each |
| Validation | Required tests pass | Tests demonstrably catch bugs (show one mutation you tried) |
| Communication | Four correct figures, complete README | A reviewer understands the result in one minute |
| Reproducibility | Fresh clone → `pytest` and results | Versions pinned, audit clean, tagged release `v1.0` |

## Submission

Push the repository, tag it `v1.0`, and send me the link with two sentences: the question and the
answer. I will review it like a consultancy reviewer or research supervisor would — and return a list
of what to fix before it goes into your portfolio.
