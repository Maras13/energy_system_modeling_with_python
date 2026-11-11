"""Time-series helpers. Conventions: UTC index, interval-start labels, power in MW."""

from __future__ import annotations

import numpy as np
import pandas as pd


def synthetic_load(start: str, hours: int, mean_MW: float, daily_amplitude_MW: float,
                   weekend_drop_MW: float, seed: int = 1) -> pd.Series:
    """SYNTHETIC hourly load (MW, naive UTC index) with a daily and weekly shape. Not measured data."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=hours, freq="h")
    local = idx.tz_localize("UTC").tz_convert("Europe/Zagreb")
    hour, weekend = local.hour.to_numpy(), local.dayofweek.to_numpy() >= 5
    load = (mean_MW + daily_amplitude_MW * np.sin((hour - 7) / 24 * 2 * np.pi)
            - weekend_drop_MW * weekend + rng.normal(0, 40, hours))
    return pd.Series(load.round(1), index=idx, name="load_MW")


def energy_MWh(power_MW: pd.Series) -> float:
    """Energy (MWh) of a regularly spaced power series (MW)."""
    step_h = power_MW.index.to_series().diff().median() / pd.Timedelta("1h")
    return float(power_MW.sum() * step_h)


def is_complete_hourly(series: pd.Series) -> bool:
    """True if the index is sorted, unique and has no missing hours."""
    idx = series.index
    if not (idx.is_monotonic_increasing and idx.is_unique):
        return False
    expected = pd.date_range(idx[0], idx[-1], freq="h")
    return len(expected) == len(idx)
