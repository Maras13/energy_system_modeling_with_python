# Course outline — what each part covers and depends on

Use this to place a lesson correctly: reuse what came before, don't re-teach it, and don't
use tools a later part introduces. The week-by-week schedule is in `COURSE_PLAN.md` (repo root).

## 00 Foundations (weeks 1–9, alongside the main track)
EE-1 DC circuits: charge, current, voltage, power vs. energy, Ohm, I²R losses, Kirchhoff,
nodal analysis, conductance matrix · EE-2 AC: phasors, impedance, active/reactive/complex power ·
EE-3 three-phase, per-unit, transmission line models, the Y-bus ·
Maths-1 linear systems, Newton's method · Maths-2 LP geometry, duality · Maths-3 Lagrangians, KKT.
**The learner has no EE background**: never assume circuit knowledge that EE-1…3 hasn't taught yet.

## 01 Python for energy modelling (weeks 1–3)
Existing Python/pandas material (setup, Git, basics → advanced, pandas) — the learner already
knows this well. New: NumPy/SciPy numerics, ENTSO-E API, data validation, energy time series,
weather data, PyPSA architecture and a first Croatia network. **Project P1.**

## 02 Electricity markets (weeks 4–5)
Merit order, market clearing, price formation, merit-order effect of renewables, negative
prices, carbon pricing, European day-ahead/intraday design, a `merit_order_dispatch()` function.
**Project P2** (SE-Europe market simulation, price comparison).

## 03 Linear programming (weeks 6–9)
1. Pen and paper: 2-plant dispatch LP, feasible region, optimal corner.
2. Same LP in Linopy + HiGHS, side by side with the merit order (identical results).
3. Duality and shadow prices; PyPSA's own optimization model (`n.model`); Pyomo comparison.
4. Unit commitment (MILP), ramping, storage (batteries, pumped hydro, reservoirs), demand
   response, rolling horizon, sensitivity analysis. **Project P3.**

## 06 Energy forecasting (weeks 10–11)
SARIMA, gradient boosting, load/renewable/price forecasts, accuracy and uncertainty.

## 04 Power flow analysis (weeks 12–15)
Power flow equations, own Newton-Raphson, Gauss-Seidel, Fast Decoupled; PyPSA `pf()`/`lpf()`
vs. pandapower; voltage and reactive power; congestion, PTDFs, nodal prices; market coupling,
flow-based allocation, redispatch; N-1; reserves; swing equation, frequency stability, ANDES;
GIS network maps. **Project P4.**

## 05 System expansion (weeks 16–18)
CAPEX/OPEX, WACC, NPV, annuities, LCOE; capacity, storage, Power-to-X and transmission
expansion; CO₂ constraints; multi-period investment; scenarios; adequacy. **Project P5.**

## 07 Advanced optimization (weeks 20–21)
Two-stage stochastic, robust, multi-objective, time/space reduction, Benders decomposition,
security-constrained optimization.

## 08 Final project (weeks 22–24)
Integrated Croatia / SE-Europe study: data → market → dispatch → AC feasibility → expansion
under uncertainty. **Project P6.**

> If anything here conflicts with a module's `readme.md`, the readme wins — and say so.
