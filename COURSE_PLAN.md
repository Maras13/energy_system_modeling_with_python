# Course plan — Energy System Modelling with Python

**Scope:** ~950 hours · 24 weeks at 40 h/week · three competence levels · six portfolio projects.
**Focus:** Croatia and its neighbours (HR, SI, HU, BA, RS; IT and AT as price references) within the European system.
**Backbone:** one PyPSA model that grows from a single bus into a multi-period, meshed, interconnected expansion model.

## Competence levels
| Level | Content |
|---|---|
| 1 – Core | Python for energy modelling, electricity markets, linear programming, power flow, PyPSA, capacity expansion |
| 2 – Professional | Forecasting, storage and flexibility, European market design, energy economics, data engineering & GIS, reliability |
| 3 – Advanced / research | Stochastic and robust optimization, multi-objective optimization, decomposition, security-constrained optimization, uncertainty |

Level 2 topics are woven into the modules where they belong. Level 3 builds on the core and is applied in the final project.

## 24-week schedule
| Weeks | Phase | Main track | Foundations track | Hours | Output |
|---|---|---|---|---|---|
| 1–3 | Foundations & data | NumPy/SciPy numerics, ENTSO-E API, data validation, energy time series, weather data, PyPSA architecture, first Croatia model | EE-1 DC circuits · EE-2 AC phasors, complex power · Maths-1 linear systems, Newton's method | 120 | **P1** Croatia demand & generation + first PyPSA network |
| 4–5 | Markets | Merit order, market clearing, price formation, merit-order effect, negative prices, carbon pricing, European day-ahead/intraday design | EE-3 three-phase, per-unit · Maths-2 LP geometry | 80 | **P2** SE-Europe market simulation & price comparison |
| 6–7 | Linear programming | Formulation, duality, shadow prices, PyPSA's optimization model (`n.model`), Pyomo comparison | EE-3 line models, Y-bus · Maths-3 Lagrangians, KKT | 80 | |
| 8–9 | Operations & storage | Unit commitment (MILP), ramping, batteries, pumped hydro, reservoirs, demand response, rolling horizon, sensitivity | Foundations complete | 80 | **P3** Dispatch optimization, PyPSA reproduced by hand |
| 10–11 | Forecasting + review | SARIMA, gradient boosting, load/renewable/price forecasts, accuracy and uncertainty · **Assessment 1** | | 80 | Forecasting module |
| 12–15 | Networks & reliability | Power flow equations, own Newton-Raphson, Gauss-Seidel, Fast Decoupled, PyPSA `pf()`/`lpf()` vs pandapower, voltage & reactive power, congestion, PTDFs, nodal prices, market coupling, flow-based allocation, redispatch, N-1, reserves, swing equation, ANDES intro, GIS maps | | 160 | **P4** SE-Europe network, cross-border flows, AC feasibility |
| 16–18 | Expansion planning | CAPEX/OPEX, WACC, NPV, annuities, LCOE, capacity/storage/Power-to-X/transmission expansion, CO₂ targets, multi-period investment, scenarios, adequacy | | 120 | **P5** Expansion scenarios |
| 19 | Review | **Assessment 2** + final project proposal | | 40 | Proposal |
| 20–21 | Advanced optimization | Two-stage stochastic, robust, multi-objective (Pareto), time/space reduction, Benders decomposition, security-constrained optimization | | 80 | Used in final project |
| 22–24 | Final project | Data → market → dispatch → AC feasibility → expansion under uncertainty | | 120 | **P6** Integrated Croatia/SE-Europe study |

## Where the repo content lives
| Folder | Content |
|---|---|
| `00_foundations/` | Electrical engineering (EE-1…3) and targeted maths (Maths-1…3) |
| `01_python_for_energy_modelling/` | Python, data engineering, time series, PyPSA introduction |
| `02_electricity_markets/` | Merit order, market clearing, European market design |
| `03_linear_programming/` | LP, duality, unit commitment, storage, rolling horizon |
| `04_power_flow_analysis/` | Power flow, congestion, nodal prices, reliability and stability |
| `05_system_expansions/` | Energy economics, capacity expansion, scenarios |
| `06_energy_forecasting/` | Forecasting block (weeks 10–11) |
| `07_advanced_optimization/` | Level 3 methods (weeks 20–21) |
| `08_final_project/` | Integrated project (weeks 22–24) |

Each lesson is a lecture notebook plus an `exercise/` notebook; answer keys live in `exercise/solutions/`.

## Checkpoints
| Week | Pass criterion |
|---|---|
| 3 | P1 runs from a clean environment; complex power for a simple AC circuit computed by hand |
| 9 | Dual of a small dispatch LP derived by hand; PyPSA objective and prices reproduced with own Linopy model to 1e-6 |
| 11 | Assessment 1 |
| 15 | Own Newton-Raphson matches pandapower to 1e-8 p.u.; differences to the DC approximation explained |
| 19 | Assessment 2 |
| 24 | Final project reviewed to consultancy / research standard |

Missed checkpoints are closed in the next review week before moving on.

## Daily rhythm (40 h/week)
- **Mornings (~4 h):** theory, derivations, worked examples by hand.
- **Afternoons (~4 h):** coding exercises, the running model, project work.
- **Fridays:** submit exercises for review, tidy the portfolio repo, write the week's README section.

## Validation standard (every project)
Unit checks · energy balance · benchmark against a reference · sensitivity tests · stated assumptions and limitations.
"The solver says optimal" is never enough on its own.

## Core references
| Area | Reference |
|---|---|
| Power systems | Glover, Sarma & Overbye, *Power System Analysis and Design* |
| Markets | Kirschen & Strbac, *Fundamentals of Power System Economics* |
| Optimization | Bertsimas & Tsitsiklis, *Introduction to Linear Optimization*; Boyd & Vandenberghe, *Convex Optimization* |
| Energy system modelling | Tom Brown, TU Berlin *Energy Systems*; Fabian Neumann, *Data Science for Energy System Modelling* |
| Data | ENTSO-E Transparency Platform, Open Power System Data, Renewables.ninja, PyPSA technology-data |
