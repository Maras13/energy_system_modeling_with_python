import numpy as np
import pytest

from hr_energy.model import build_network, solve, summarise


@pytest.fixture
def solved(config):
    return solve(build_network(config))


def test_network_matches_config(config, solved):
    """Compare against the config, an independent source - not against the network's own data."""
    for name, g in config["generators"].items():
        assert solved.generators.at[name, "p_nom"] == g["p_nom"]
        assert solved.generators.at[name, "p_max_pu"] == g.get("p_max_pu", 1.0)
        limit = g["p_nom"] * g.get("p_max_pu", 1.0)
        assert solved.generators_t.p[name].max() <= limit + 1e-6, f"{name} above its available capacity"


def test_supply_meets_demand_every_hour(solved):
    assert summarise(solved)["max_balance_gap_MW"] < 1e-6


def test_objective_equals_cost_recomputed_by_hand(solved):
    assert summarise(solved)["cost_check_ok"]


def test_price_follows_the_merit_order(solved):
    """Single bus, no storage or ramping: each hour's price is the cost of the last plant needed."""
    gens = solved.generators.sort_values("marginal_cost")
    available = (gens.p_nom * gens.p_max_pu).cumsum()
    for t, demand in solved.loads_t.p_set["demand"].items():
        expected = gens.marginal_cost[available >= demand - 1e-6].iloc[0]
        assert solved.buses_t.marginal_price.at[t, "HR"] == pytest.approx(expected)


def test_infeasible_system_fails_loudly(config):
    config["generators"] = {"tiny": {"carrier": "gas", "p_nom": 100, "marginal_cost": 50}}
    with pytest.raises(RuntimeError, match="not optimal"):
        solve(build_network(config))


def test_energy_by_carrier_adds_up_to_load(solved):
    s = summarise(solved)
    assert np.isclose(sum(s["energy_by_carrier_MWh"].values()), s["load_MWh"], rtol=1e-6)
