
<img width="584" height="820" alt="Screenshot 2026-04-17 at 15 31 36" src="https://github.com/user-attachments/assets/22d81879-1ab5-4663-8ed9-416c00fd3d62" />

<img width="586" height="709" alt="Screenshot 2026-04-17 at 15 31 25" src="https://github.com/user-attachments/assets/a2ad2bfe-1dec-43e4-81e2-9bdcfc6172c4" />

<img width="589" height="965" alt="Screenshot 2026-04-17 at 15 31 09" src="https://github.com/user-attachments/assets/7b854ca3-e85a-4fe4-ac32-a40899f1af40" />

<img width="594" height="777" alt="Screenshot 2026-04-17 at 15 31 51" src="https://github.com/user-attachments/assets/76af9476-a68a-4ec0-a2bd-e72d25606e46" />


<img width="600" height="797" alt="Screenshot 2026-04-17 at 15 32 16" src="https://github.com/user-attachments/assets/7c339ccc-6b1b-4e0a-806c-4fbda51d310e" />

## How to use this module

**Core path (24-week plan):** the energy lessons below. They assume you already know Python, pandas and Git.

| Folder | Lesson | Topic | Status |
|---|---|---|---|
| [`06_energy_time_series/`](06_energy_time_series/) | M1.1 | ENTSO-E data for Croatia: API token, time zones and DST, validation, cleaning, resampling power vs. energy | ready |
| [`07_pypsa_first_network/`](07_pypsa_first_network/) | M1.2 | First PyPSA network: data model, one-week dispatch, prices, validation, emissions, the LP inside | ready |
| [`08_numerics/`](08_numerics/) | M1.3 | NumPy and SciPy for energy numerics: vectorisation, sparse linear algebra, why power flow is nonlinear, Newton's method (covers Maths-1.2) | ready |
| [`09_generation_and_weather/`](09_generation_and_weather/) | M1.4 | From weather to power: capacity factors, wind cube law and power curves, Weibull statistics, solar position and clear-sky PV, real ERA5 weather from Open-Meteo, PyPSA `p_max_pu` profiles | ready |
| [`10_energy_visualisation/`](10_energy_visualisation/) | M1.5 | Visualising energy data: plot conventions, seasonal daily profiles, DST-safe heatmaps, load and residual-load duration curves, stacked dispatch with prices, price vs. residual load, saving figures | ready |
| [`11_project_structure/`](11_project_structure/) | M1.6 | Reproducible projects: src layout, validated config, physics tests and mutation testing, CLI, environments, data provenance, README — with a working template | ready |

**Portfolio project P1** (weeks 2–3): [`PROJECT_P1.md`](PROJECT_P1.md) — Croatian electricity from data to a first dispatch model, built on the M1.6 template.

**Optional refresher (not part of the 24-week path):** folders `01`–`05` (installation, bash/Jupyter/VS Code,
Git, general Python from basics to advanced, pandas). They are general data-analytics material without
energy content, written for learners new to Python. Notes from a review in November 2026:

- They pin older versions (pandas 2.2.3). On current pandas, `05_pandas_intro/01_pandas.ipynb` and
  `02_datetime.ipynb` raise errors in several cells (e.g. the removed `"T"` frequency alias, changed
  indexing); some failures are deliberate exercise gaps. Use the pinned `requirements.txt` if you run them.
- PostgreSQL, pgAdmin and Docker in the setup guides are not needed for the core path.

See [`COURSE_PLAN.md`](../COURSE_PLAN.md) for the full schedule.
