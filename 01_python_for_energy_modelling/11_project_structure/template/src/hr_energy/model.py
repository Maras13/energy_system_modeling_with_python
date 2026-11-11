"""Build, solve and summarise the PyPSA model defined by a config dictionary."""

from __future__ import annotations

import logging
import warnings

import pandas as pd
import pypsa

from .data import energy_MWh, is_complete_hourly, synthetic_load

logging.getLogger("pypsa").setLevel(logging.ERROR)
logging.getLogger("linopy").setLevel(logging.ERROR)
# raised inside PyPSA under pandas 3, not by this project; revisit when PyPSA 2.0 is out
warnings.filterwarnings("ignore", message="pandas infers the `str` dtype", category=FutureWarning)


def get_load(config: dict) -> pd.Series:
    """Load time series (MW) as specified in the config."""
    spec, snaps = config["load"], config["snapshots"]
    if spec["source"] == "synthetic":
        return synthetic_load(snaps["start"], snaps["hours"], spec["mean_MW"], spec["daily_amplitude_MW"],
                              spec["weekend_drop_MW"], spec.get("seed", 1))
    s = pd.read_csv(spec["source"], index_col=0, parse_dates=True).iloc[:, 0].rename("load_MW")
    return s.tz_convert("UTC").tz_localize(None) if s.index.tz is not None else s


def build_network(config: dict) -> pypsa.Network:
    """Single-bus network with the generators and load from the config."""
    load = get_load(config)
    if not is_complete_hourly(load):
        raise ValueError("load must be a complete, sorted, unique hourly series")
    n = pypsa.Network()
    n.set_snapshots(load.index)
    n.add("Carrier", "AC")
    n.add("Bus", "HR", carrier="AC")
    for carrier in sorted({g["carrier"] for g in config["generators"].values()}):
        n.add("Carrier", carrier)
    n.add("Load", "demand", bus="HR", carrier="AC", p_set=load)
    for name, g in config["generators"].items():
        n.add("Generator", name, bus="HR", carrier=g["carrier"], p_nom=g["p_nom"],
              marginal_cost=g["marginal_cost"], p_max_pu=g.get("p_max_pu", 1.0))
    return n


def solve(n: pypsa.Network, solver: str = "highs") -> pypsa.Network:
    """Optimise the dispatch; raise if the solver does not report an optimal solution."""
    status, condition = n.optimize(solver_name=solver, log_to_console=False, progress=False,
                                   include_objective_constant=False)
    if condition != "optimal":
        raise RuntimeError(f"optimisation not optimal: {status}, {condition}")
    return n


def summarise(n: pypsa.Network) -> dict:
    """Key results with units, plus the validation checks every run must pass."""
    dispatch, load = n.generators_t.p, n.loads_t.p_set["demand"]
    price = n.buses_t.marginal_price["HR"]
    balance_gap = float((dispatch.sum(axis=1) - load).abs().max())
    cost_by_hand = float((dispatch * n.generators.marginal_cost).sum().sum())
    return {
        "total_cost_EUR": float(n.objective),
        "load_MWh": energy_MWh(load),
        "mean_price_EUR_per_MWh": float(price.mean()),
        "max_balance_gap_MW": balance_gap,
        "cost_check_ok": abs(cost_by_hand - n.objective) <= 1e-6 * max(1.0, abs(n.objective)),
        "energy_by_carrier_MWh": dispatch.T.groupby(n.generators.carrier).sum().T.sum().round(1).to_dict(),
    }
