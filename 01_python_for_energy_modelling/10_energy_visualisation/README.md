# 10 Visualising energy data

| Notebook | Lesson | Topic |
|---|---|---|
| `01_visualising_energy_data.ipynb` | M1.5 | Plot conventions (units, local time, one colour per carrier, honest baselines), weekly time series, seasonal daily profiles, DST-safe year heatmaps, load and residual-load duration curves, stacked dispatch with step prices, price vs. residual load (the merit order, visible), monthly energy mix |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).
Plot functions return their data as well as the figure, so the exercise tests what the eye cannot
(e.g. that a stacked dispatch adds up to the load).

## Setup
```bash
pip install numpy pandas scipy matplotlib pvlib pypsa highspy
```
Tested with PyPSA 1.4.0 and pvlib 0.16.1. Figures are **not** stored in the notebooks in this repo
(to keep the files small) — run the notebooks to see them. Dispatching the full year takes a few seconds.

> All data in this lesson are **synthetic**: one year built from M1.2–M1.4 (Croatia-like load shape,
> wind from the M1.4 power curve, clear-sky solar with random clouds), dispatched in the stylised M1.2
> network. Plausible in shape, not measured.
