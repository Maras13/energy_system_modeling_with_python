# hr-energy — dispatch model of a Croatia-like power system

> **Course template (project P1).** Replace this block with one sentence on what *your* project
> answers, e.g. *"How much do imports set the Croatian electricity price in winter?"*

## Question and result
State the question first, then the answer in two or three sentences with the one figure that shows it.
A reader who stops here should still know what you found.

## Method
- **Model:** single-bus linear dispatch in [PyPSA](https://pypsa.org) (HiGHS solver), hourly, one week.
- **Formulation:** minimise Σₜ Σ_g c_g · p_g,t subject to Σ_g p_g,t = d_t (nodal balance) and
  0 ≤ p_g,t ≤ p̄_g · a_g,t (available capacity). The price is the dual of the balance constraint.
- **Inputs:** `config/config.yaml` (every number, with its unit); data sources in `data/README.md`.

## Validation
Every run checks: supply = demand in every hour, objective = Σ p × marginal cost, prices equal the
merit order (single bus), network matches the config. See `tests/` — run `pytest`.

## Limitations
Be explicit: one bus (no grid constraints), no storage or ramping, imports as a fixed-price generator,
synthetic load unless real data are configured, no minimum stable output for thermal plants.

## Reproduce
```bash
conda env create -f environment.yml && conda activate hr-energy   # or: pip install -e ".[dev]"
pytest                                                              # all tests must pass
python -m hr_energy --config config/config.yaml --out results/     # writes results/<name>/
```
Tested with: Python 3.12, PyPSA 1.4.0, HiGHS 1.15, pandas 3.0 (record your `pip freeze` here).

## Project layout
```
config/        scenario settings (YAML) — change scenarios here, not in code
data/          raw/ and processed/ (git-ignored) + README.md with provenance
notebooks/     exploration and figures; import from the package
src/hr_energy/ the code: config, data, model, cli
tests/         pytest: physics and economics checks
results/       generated outputs (git-ignored)
```

## Data and licence
Cite every source with retrieval date (see `data/README.md`). Code licence: choose one (e.g. MIT).
