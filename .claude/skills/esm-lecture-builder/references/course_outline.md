# Course outline — what each module covers and depends on

Use this to place a lecture correctly: reuse what earlier modules taught, don't
re-teach it, and don't use tools a later module introduces.

## 01 Python for energy modelling
Setup (Windows/macOS/Linux, VS Code, venv), bash, Jupyter/Colab, Git & GitHub,
Python basics (types, strings, if, loops, data structures, functions), intermediate
(error handling, iterators/generators, lambda/map/filter/reduce, performance),
advanced (OOP, functional programming, concurrency), pandas (Series/DataFrame, datetime).
**Students can assume:** functions, dicts/lists, pandas DataFrames, datetime index.

## 02 Electricity markets
Load curves and time series, supply curves, merit order, market clearing price,
a `merit_order_dispatch()` function students write themselves.
**Introduces:** the merit order as a greedy algorithm. **Reused in 03.**

## 03 Linear programming (4 weeks, same model rebuilt each week)
1. Pen-and-paper: 2-plant dispatch LP, feasible region, optimal corner.
   Map LP terms to energy terms (variables = generation, objective = cost, constraints = limits).
2. Same LP in Linopy + HiGHS. Run it next to the Module 02 `merit_order_dispatch()`:
   identical results → "the merit order was solving an LP all along".
3. 24 hours: ramp-rate limits and battery storage (charge cheap, discharge expensive).
   Shadow prices: the dual of each hour's demand constraint is the electricity price.
4. Use the model: sensitivity analysis (+5 GW solar, remove lignite, double battery),
   costs/prices/emissions, ending with a 1-page policy brief.

## 04 Power flow analysis
Nodes and lines, DC power flow approximation, line capacity limits, congestion and
nodal prices. Extends the 03 dispatch model from one node to a small network.

## 05 System expansion
Capacity expansion: choose how much to build (investment cost) and how to run it
(operating cost) in one LP; annuities; renewables + storage + network expansion.

> The module plans in the repo are partly screenshots. If something above conflicts with
> the module's `readme.md`, the readme wins — and say so.
