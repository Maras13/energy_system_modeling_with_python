import pandas as pd
import pytest

from hr_energy.data import energy_MWh, is_complete_hourly, synthetic_load


def test_energy_is_power_times_time():
    quarter_hours = pd.Series([2000.0] * 8, index=pd.date_range("2025-01-01", periods=8, freq="15min"))
    assert energy_MWh(quarter_hours) == pytest.approx(4000.0)          # 2 h at 2,000 MW
    assert energy_MWh(quarter_hours.resample("h").mean()) == pytest.approx(4000.0)


def test_gaps_and_duplicates_are_detected():
    s = pd.Series(1.0, index=pd.date_range("2025-01-01", periods=5, freq="h"))
    assert is_complete_hourly(s)
    assert not is_complete_hourly(s.drop(s.index[2]))                   # gap
    assert not is_complete_hourly(pd.concat([s, s.iloc[[1]]]).sort_index())  # duplicate


def test_synthetic_load_is_reproducible():
    a = synthetic_load("2025-01-13", 48, 2100, 380, 200, seed=1)
    b = synthetic_load("2025-01-13", 48, 2100, 380, 200, seed=1)
    pd.testing.assert_series_equal(a, b)
    assert 1000 < a.min() and a.max() < 3500, "plausible MW range for this system"
