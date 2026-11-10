"""Reference solver + sanity checks for small energy system models (course modules 02-05).

Usage (CLI):
    python esm_checks.py case.json                       # solve reference model, run checks
    python esm_checks.py case.json --compare results.csv # also check someone else's results
    python esm_checks.py --example > case.json           # print an example case

Usage (Python, e.g. from a notebook):
    from esm_checks import load_case, solve_reference, check_results, merit_order_dispatch
    case = load_case("case.json")
    ref = solve_reference(case)
    report = check_results(case, dispatch=my_dispatch_df, prices=my_prices, total_cost=my_cost)

Case format (JSON) -- units: MW, MWh, EUR/MWh, EUR, hours:
{
  "name": "two-plant dispatch",
  "hours": 1,                          # number of time steps (default 1)
  "demand_MW": 900,                    # number, or list with one value per hour
  "voll": 3000,                        # optional: value of lost load, allows load shedding
  "generators": [
    {"name": "lignite", "marginal_cost": 30, "p_max": 800},
    {"name": "gas", "marginal_cost": 80, "p_max": 500, "ramp_MW_per_h": 200},
    {"name": "solar", "marginal_cost": 0, "p_max": 300, "availability": [0.0, 0.5]},
    {"name": "wind_new", "marginal_cost": 0, "extendable": true,
     "capital_cost": 50, "p_nom_max": 1000, "availability": [...]}
  ],
  "storage": [
    {"name": "battery", "power_MW": 100, "energy_MWh": 400,
     "efficiency_charge": 0.95, "efficiency_discharge": 0.95, "initial_soc_MWh": 0}
  ]
}
For extendable generators, capital_cost is EUR per MW of capacity for the modelled period
(annualise and scale to the number of hours before putting it in the case).
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import warnings

import numpy as np
import pandas as pd

TOL = 1e-4  # MW / EUR tolerance for numerical comparisons


# --------------------------------------------------------------------------- case handling
def load_case(path_or_dict) -> dict:
    case = json.load(open(path_or_dict)) if isinstance(path_or_dict, str) else dict(path_or_dict)
    case.setdefault("name", "unnamed case")
    case.setdefault("hours", 1)
    case.setdefault("storage", [])
    T = int(case["hours"])
    d = case["demand_MW"]
    case["demand_MW"] = [float(d)] * T if np.isscalar(d) else [float(x) for x in d]
    if len(case["demand_MW"]) != T:
        raise ValueError(f"demand_MW has {len(case['demand_MW'])} values but hours = {T}")
    names = [g["name"] for g in case["generators"]] + [s["name"] for s in case["storage"]]
    if len(set(names)) != len(names):
        raise ValueError("generator/storage names must be unique")
    for g in case["generators"]:
        a = g.get("availability", 1.0)
        g["availability"] = [float(a)] * T if np.isscalar(a) else [float(x) for x in a]
        if len(g["availability"]) != T:
            raise ValueError(f"availability of {g['name']} must have {T} values")
        if not g.get("extendable") and "p_max" not in g:
            raise ValueError(f"{g['name']} needs p_max (or extendable: true)")
    return case


def is_static(case) -> bool:
    """True if each hour is independent (no storage, no ramping, no investment)."""
    return not case["storage"] and not any(
        g.get("ramp_MW_per_h") is not None or g.get("extendable") for g in case["generators"])


# --------------------------------------------------------------------------- merit order
def merit_order_dispatch(generators, demand_MW):
    """Greedy merit-order dispatch for ONE hour.

    generators: list of dicts with name, marginal_cost, p_max (already scaled by availability).
    Returns (dispatch dict MW, price EUR/MWh, (price_low, price_high)).
    price_low/high give the valid price range when demand exactly hits a capacity step
    (any price in that range clears the market, and an LP solver may report either end).
    """
    order = sorted(generators, key=lambda g: g["marginal_cost"])
    remaining, dispatch, price = demand_MW, {}, None
    for i, g in enumerate(order):
        p = min(g["p_max"], max(remaining, 0.0))
        dispatch[g["name"]] = p
        if p > TOL:
            price = g["marginal_cost"]
        remaining -= p
    if remaining > TOL:
        return dispatch, math.inf, (math.inf, math.inf)  # not enough capacity
    if price is None:  # zero demand
        price = order[0]["marginal_cost"]
    low, high = price, price
    used = [g for g in order if dispatch[g["name"]] > TOL]
    if used:
        last = used[-1]
        if abs(dispatch[last["name"]] - last["p_max"]) < TOL:  # marginal unit is full
            nxt = [g for g in order if g["marginal_cost"] > last["marginal_cost"]]
            high = nxt[0]["marginal_cost"] if nxt else math.inf
    return dispatch, price, (low, high)


# --------------------------------------------------------------------------- reference LP
def solve_reference(case) -> dict:
    """Build and solve the reference LP with Linopy + HiGHS. Returns a results dict."""
    import linopy
    import xarray as xr

    # We only ever use shifted values from hour 1 on, so the empty first slot is never used.
    warnings.filterwarnings("ignore", message=".*absent slots.*")

    case = load_case(case)
    T = int(case["hours"])
    hours = pd.RangeIndex(T, name="hour")
    gens = case["generators"]
    gnames = pd.Index([g["name"] for g in gens], name="gen")
    avail = xr.DataArray(np.array([g["availability"] for g in gens]).T, coords=[hours, gnames])
    mc = xr.DataArray([float(g["marginal_cost"]) for g in gens], coords=[gnames])
    ext = [g["name"] for g in gens if g.get("extendable")]
    fixed_cap = xr.DataArray([np.inf if g.get("extendable") else float(g["p_max"]) for g in gens],
                             coords=[gnames])

    m = linopy.Model()
    p = m.add_variables(lower=0, upper=(avail * fixed_cap).where(~np.isinf(fixed_cap), np.inf),
                        coords=[hours, gnames], name="p")
    balance_lhs = p.sum("gen")
    objective = (p * mc).sum()

    if ext:
        eidx = pd.Index(ext, name="gen")
        pmax_ext = xr.DataArray([float(g.get("p_nom_max", np.inf)) for g in gens if g.get("extendable")],
                                coords=[eidx])
        p_nom = m.add_variables(lower=0, upper=pmax_ext, coords=[eidx], name="p_nom")
        m.add_constraints(p.sel(gen=ext) <= avail.sel(gen=ext) * p_nom, name="capacity")
        capex = xr.DataArray([float(g.get("capital_cost", 0.0)) for g in gens if g.get("extendable")],
                             coords=[eidx])
        objective = objective + (p_nom * capex).sum()

    ramp = [g for g in gens if g.get("ramp_MW_per_h") is not None]
    if ramp and T > 1:  # ramp limits, MW per hour: |p[t] - p[t-1]| <= r
        ridx = [g["name"] for g in ramp]
        r = xr.DataArray([float(g["ramp_MW_per_h"]) for g in ramp], coords=[pd.Index(ridx, name="gen")])
        later = hours[1:]
        diff = (p - p.shift(hour=1)).sel(hour=later, gen=ridx)
        m.add_constraints(diff <= r, name="ramp_up")
        m.add_constraints(diff >= -r, name="ramp_down")

    for s in case["storage"]:
        n = s["name"]
        eta_c, eta_d = float(s.get("efficiency_charge", 1.0)), float(s.get("efficiency_discharge", 1.0))
        ch = m.add_variables(lower=0, upper=float(s["power_MW"]), coords=[hours], name=f"{n}_charge")
        dis = m.add_variables(lower=0, upper=float(s["power_MW"]), coords=[hours], name=f"{n}_discharge")
        soc = m.add_variables(lower=0, upper=float(s["energy_MWh"]), coords=[hours], name=f"{n}_soc")
        soc0 = float(s.get("initial_soc_MWh", 0.0))
        flow = eta_c * ch - dis / eta_d  # MWh added to the store in each hour
        m.add_constraints(soc.sel(hour=[0]) - flow.sel(hour=[0]) == soc0, name=f"{n}_soc_first")
        if T > 1:
            m.add_constraints((soc - soc.shift(hour=1) - flow).sel(hour=hours[1:]) == 0, name=f"{n}_soc")
        if s.get("cyclic", True):  # end at least as full as we started -> no free energy
            m.add_constraints(soc.sel(hour=[T - 1]) >= soc0, name=f"{n}_cyclic")
        balance_lhs = balance_lhs + dis - ch

    demand = xr.DataArray(case["demand_MW"], coords=[hours])
    if case.get("voll") is not None:
        shed = m.add_variables(lower=0, upper=demand, coords=[hours], name="shed")
        balance_lhs = balance_lhs + shed
        objective = objective + float(case["voll"]) * shed.sum()

    m.add_constraints(balance_lhs == demand, name="balance")
    m.add_objective(objective)
    status, condition = m.solve(solver_name="highs", output_flag=False)

    out = {"status": status, "condition": condition, "model": m}
    if condition != "optimal":
        return out
    dispatch = p.solution.to_pandas()
    dispatch.columns.name = None
    out["dispatch"] = dispatch
    out["prices"] = m.constraints["balance"].dual.to_pandas().rename("price_EUR_per_MWh")
    out["total_cost"] = float(m.objective.value)
    out["storage"] = {s["name"]: pd.DataFrame({
        "charge_MW": m.variables[f"{s['name']}_charge"].solution.to_pandas(),
        "discharge_MW": m.variables[f"{s['name']}_discharge"].solution.to_pandas(),
        "soc_MWh": m.variables[f"{s['name']}_soc"].solution.to_pandas()}) for s in case["storage"]}
    out["p_nom"] = (m.variables["p_nom"].solution.to_pandas() if ext else pd.Series(dtype=float))
    out["shed"] = (m.variables["shed"].solution.to_pandas() if case.get("voll") is not None
                   else pd.Series(0.0, index=hours))
    return out


# --------------------------------------------------------------------------- checks
def _row(check, passed, detail):
    return {"check": check, "passed": bool(passed), "detail": detail}


def check_results(case, dispatch, prices=None, total_cost=None, storage=None, p_nom=None,
                  shed=None, reference=None) -> pd.DataFrame:
    """Sanity-check a dispatch result against a case. Works for ANY model's output.

    dispatch: DataFrame, rows = hours (0..T-1), columns = generator names, values in MW.
    prices:   optional Series of EUR/MWh per hour (dual of the demand balance).
    total_cost: optional float, EUR (objective value of the model being checked).
    storage:  optional {name: DataFrame with charge_MW, discharge_MW, soc_MWh}.
    p_nom:    optional Series of built capacity (MW) for extendable generators.
    reference: optional results dict from solve_reference(case) to compare costs against.
    Returns a DataFrame with one row per check: check, passed, detail.
    """
    case = load_case(case)
    T = int(case["hours"])
    gens = {g["name"]: g for g in case["generators"]}
    rows = []
    dispatch = pd.DataFrame(dispatch).reset_index(drop=True)
    storage = storage or {}
    shed = pd.Series(0.0, index=range(T)) if shed is None else pd.Series(shed).reset_index(drop=True)
    p_nom = pd.Series(dtype=float) if p_nom is None else pd.Series(p_nom)

    missing = set(gens) - set(dispatch.columns)
    rows.append(_row("all generators present", not missing,
                     "ok" if not missing else f"missing columns: {sorted(missing)}"))
    rows.append(_row("one row per hour", len(dispatch) == T, f"{len(dispatch)} rows, expected {T}"))
    if missing or len(dispatch) != T:
        return pd.DataFrame(rows)

    # 1. demand is met in every hour
    supply = dispatch[list(gens)].sum(axis=1) + shed.values
    for n, s in storage.items():
        supply = supply + s["discharge_MW"].values - s["charge_MW"].values
    gap = (supply - pd.Series(case["demand_MW"])).abs()
    rows.append(_row("demand met every hour", gap.max() < 1e-3,
                     f"max mismatch {gap.max():.4g} MW (hour {int(gap.idxmax())})"))

    # 2. no negative generation, no generation above available capacity
    rows.append(_row("no negative generation", (dispatch[list(gens)] >= -TOL).all().all(),
                     f"min value {dispatch[list(gens)].min().min():.4g} MW"))
    over = []
    for n, g in gens.items():
        cap = p_nom.get(n, np.nan) if g.get("extendable") else g["p_max"]
        if pd.isna(cap):
            continue
        limit = np.array(g["availability"]) * cap
        excess = dispatch[n].values - limit
        if excess.max() > 1e-3:
            over.append(f"{n} +{excess.max():.3g} MW in hour {int(excess.argmax())}")
    rows.append(_row("generation within available capacity", not over, "ok" if not over else "; ".join(over)))

    # 3. ramp limits
    bad = []
    for n, g in gens.items():
        r = g.get("ramp_MW_per_h")
        if r is not None and T > 1:
            step = dispatch[n].diff().abs().max()
            if step > r + 1e-3:
                bad.append(f"{n} changes {step:.4g} MW/h > {r}")
    if any(g.get("ramp_MW_per_h") is not None for g in gens.values()):
        rows.append(_row("ramp limits respected", not bad, "ok" if not bad else "; ".join(bad)))

    # 4. storage physics
    for s in case["storage"]:
        n = s["name"]
        if n not in storage:
            rows.append(_row(f"storage {n}: results given", False, "no storage results passed in"))
            continue
        df = storage[n].reset_index(drop=True)
        eta_c, eta_d = s.get("efficiency_charge", 1.0), s.get("efficiency_discharge", 1.0)
        soc_prev = np.concatenate([[s.get("initial_soc_MWh", 0.0)], df["soc_MWh"].values[:-1]])
        expected = soc_prev + eta_c * df["charge_MW"].values - df["discharge_MW"].values / eta_d
        err = np.abs(expected - df["soc_MWh"].values).max()
        rows.append(_row(f"storage {n}: energy balance", err < 1e-3, f"max SOC error {err:.4g} MWh"))
        inb = (df["soc_MWh"] >= -1e-3).all() and (df["soc_MWh"] <= s["energy_MWh"] + 1e-3).all()
        rows.append(_row(f"storage {n}: SOC within 0..{s['energy_MWh']} MWh", inb,
                         f"range {df['soc_MWh'].min():.4g}..{df['soc_MWh'].max():.4g} MWh"))
        both = (np.minimum(df["charge_MW"], df["discharge_MW"]) > 1e-3).sum()
        rows.append(_row(f"storage {n}: no simultaneous charge and discharge", both == 0,
                         f"{both} hour(s) with both (wastes energy; usually a modelling or price issue)"))

    # 5. cost: positive, and consistent with the dispatch
    op_cost = sum((dispatch[n] * g["marginal_cost"]).sum() for n, g in gens.items())
    capex = sum(p_nom.get(n, 0.0) * g.get("capital_cost", 0.0) for n, g in gens.items() if g.get("extendable"))
    recomputed = op_cost + capex + float(case.get("voll") or 0.0) * float(shed.sum())
    rows.append(_row("total cost not negative", recomputed >= -TOL, f"recomputed cost {recomputed:,.2f} EUR"))
    if total_cost is not None:
        rel = abs(total_cost - recomputed) / max(1.0, abs(recomputed))
        rows.append(_row("reported cost matches dispatch", rel < 1e-6,
                         f"reported {total_cost:,.2f} EUR vs recomputed {recomputed:,.2f} EUR"))
    if reference is not None and reference.get("condition") == "optimal":
        rel = (recomputed - reference["total_cost"]) / max(1.0, abs(reference["total_cost"]))
        rows.append(_row("cost equals reference optimum", abs(rel) < 1e-6,
                         f"this {recomputed:,.2f} EUR vs reference {reference['total_cost']:,.2f} EUR "
                         + ("(cheaper than the optimum -> a constraint is missing)" if rel < -1e-6 else
                            "(more expensive -> not optimal or an extra constraint)" if rel > 1e-6 else "")))

    # 6. prices
    if prices is not None:
        prices = pd.Series(prices).reset_index(drop=True)
        mcs = [g["marginal_cost"] for g in gens.values()]
        cap = case.get("voll") if case.get("voll") is not None else max(mcs)
        lo_ok = (prices >= min(0.0, min(mcs)) - TOL).all()
        hi_ok = (prices <= cap + TOL).all() or not is_static(case)
        rows.append(_row("prices within plausible range", lo_ok and hi_ok,
                         f"prices {prices.min():.4g}..{prices.max():.4g} EUR/MWh, "
                         f"marginal costs {min(mcs)}..{max(mcs)} EUR/MWh"))
        if is_static(case):  # each hour independent -> must equal the merit order
            mism, cost_mism = [], []
            for t in range(T):
                avail = [{"name": n, "marginal_cost": g["marginal_cost"],
                          "p_max": g["p_max"] * g["availability"][t]} for n, g in gens.items()]
                mo_disp, mo_price, (lo, hi) = merit_order_dispatch(avail, case["demand_MW"][t] - shed[t])
                if math.isinf(lo):
                    cap = sum(a["p_max"] for a in avail)
                    mism.append(f"hour {t}: demand {case['demand_MW'][t] - shed[t]:.4g} MW > capacity "
                                f"{cap:.4g} MW, so no merit-order price exists (add load shedding / 'voll')")
                elif not (lo - TOL <= prices[t] <= hi + TOL):
                    rng = f"{lo:.4g}" if lo == hi else f"{lo:.4g}..{hi:.4g}"
                    mism.append(f"hour {t}: model price {prices[t]:.4g} vs merit-order price {rng} EUR/MWh")
                lp_c = sum(dispatch.at[t, n] * g["marginal_cost"] for n, g in gens.items())
                mo_c = sum(mo_disp[n] * gens[n]["marginal_cost"] for n in mo_disp)
                if abs(lp_c - mo_c) > 1e-3 * max(1.0, mo_c):
                    cost_mism.append(f"hour {t}: {lp_c:.2f} vs {mo_c:.2f} EUR")
            rows.append(_row("price equals merit-order price", not mism, "ok" if not mism else "; ".join(mism[:5])))
            rows.append(_row("hourly cost equals merit-order cost", not cost_mism,
                             "ok" if not cost_mism else "; ".join(cost_mism[:5])))
    return pd.DataFrame(rows)


def check_reference(case) -> tuple[dict, pd.DataFrame]:
    """Solve the reference model and check it. Returns (results, report)."""
    case = load_case(case)
    ref = solve_reference(case)
    if ref["condition"] != "optimal":
        return ref, pd.DataFrame([_row("solver status optimal", False,
                                       f"{ref['status']} / {ref['condition']} - check demand vs capacity "
                                       "(add 'voll' to allow load shedding)")])
    report = check_results(case, ref["dispatch"], ref["prices"], ref["total_cost"], ref["storage"],
                           ref["p_nom"], ref["shed"])
    report = pd.concat([pd.DataFrame([_row("solver status optimal", True, ref["condition"])]), report],
                       ignore_index=True)
    return ref, report


EXAMPLE = {
    "name": "3 plants, 4 hours, battery",
    "hours": 4,
    "demand_MW": [700, 1100, 1300, 900],
    "generators": [
        {"name": "solar", "marginal_cost": 0, "p_max": 400, "availability": [0.0, 0.6, 0.9, 0.3]},
        {"name": "lignite", "marginal_cost": 30, "p_max": 800, "ramp_MW_per_h": 300},
        {"name": "gas", "marginal_cost": 80, "p_max": 600},
    ],
    "storage": [{"name": "battery", "power_MW": 100, "energy_MWh": 200,
                 "efficiency_charge": 0.95, "efficiency_discharge": 0.95, "initial_soc_MWh": 0}],
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("case", nargs="?", help="case JSON file")
    ap.add_argument("--compare", help="CSV with hour rows and one column per generator (MW); "
                                      "optional 'price' column in EUR/MWh")
    ap.add_argument("--example", action="store_true", help="print an example case and exit")
    a = ap.parse_args(argv)
    if a.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    if not a.case:
        ap.error("give a case file (or --example)")
    case = load_case(a.case)
    pd.set_option("display.width", 160, "display.max_colwidth", 110)
    ref, report = check_reference(case)
    print(f"== Reference model: {case['name']} ==")
    if ref.get("condition") == "optimal":
        print(f"total cost: {ref['total_cost']:,.2f} EUR")
        print(ref["dispatch"].round(2).assign(price_EUR_per_MWh=ref["prices"].round(2)).to_string())
    print(report.to_string(index=False))
    ok = report["passed"].all()
    if a.compare:
        res = pd.read_csv(a.compare)
        prices = res.pop("price") if "price" in res.columns else None
        res = res.drop(columns=[c for c in res.columns if c.lower() in ("hour", "unnamed: 0")])
        cmp_report = check_results(case, res, prices, reference=ref)
        print(f"\n== Checking {a.compare} ==")
        print(cmp_report.to_string(index=False))
        ok = ok and cmp_report["passed"].all()
    print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
