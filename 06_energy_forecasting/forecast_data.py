"""Synthetic, Croatia-sized hourly data for the forecasting module (2023-2025).

The data are generated, not measured: every lesson knows exactly how they were made, so it can check
what a forecasting method gets right and wrong. Their structure follows real Croatian demand -
heating in winter, cooling and tourism in summer, a daily and weekly rhythm, public holidays and
weather that persists for days - at a realistic size (about 17-18 TWh a year). All numbers are
illustrative; the real-data cells in the lessons use ENTSO-E data instead.
"""
import numpy as np
import pandas as pd

# Croatian public holidays 2023-2025 (weekday holidays lower demand like a Sunday).
HOLIDAYS = pd.to_datetime([
    "2023-01-01", "2023-01-06", "2023-04-10", "2023-05-01", "2023-05-30", "2023-06-08", "2023-06-22",
    "2023-08-05", "2023-08-15", "2023-11-01", "2023-11-18", "2023-12-25", "2023-12-26",
    "2024-01-01", "2024-01-06", "2024-04-01", "2024-05-01", "2024-05-30", "2024-06-22",
    "2024-08-05", "2024-08-15", "2024-11-01", "2024-11-18", "2024-12-25", "2024-12-26",
    "2025-01-01", "2025-01-06", "2025-04-21", "2025-05-01", "2025-05-30", "2025-06-19", "2025-06-22",
    "2025-08-05", "2025-08-15", "2025-11-01", "2025-11-18", "2025-12-25", "2025-12-26",
])


def load_data(seed: int = 11) -> pd.DataFrame:
    """Hourly temperature (deg C), holiday flag and electricity demand (MW), 2023-01-01 to 2025-12-31."""
    idx = pd.date_range("2023-01-01", "2025-12-31 23:00", freq="h")
    rng = np.random.default_rng(seed)
    doy, hour, dow = idx.dayofyear.to_numpy(), idx.hour.to_numpy(), idx.dayofweek.to_numpy()

    days = len(idx) // 24                                   # weather anomaly that persists for days
    anomaly = np.zeros(days)
    shocks = rng.normal(0, 1.6, days)
    for d in range(1, days):
        anomaly[d] = 0.85 * anomaly[d - 1] + shocks[d]
    temperature = (13 - 10 * np.cos(2 * np.pi * (doy - 20) / 365)
                   + 3.2 * np.sin(np.pi * (hour - 8) / 12).clip(-1, 1) + np.repeat(anomaly, 24))

    holiday = np.isin(idx.normalize(), HOLIDAYS)
    workday = (dow < 5) & ~holiday
    shape = 0.85 + 0.25 * np.sin(np.pi * (hour - 6) / 14).clip(0) + 0.12 * np.exp(-((hour - 19) / 2.2) ** 2)
    profile = np.where(workday, 1.0, 0.88) * shape
    tourism = 1 + 0.06 * np.exp(-((doy - 205) / 25.0) ** 2)  # July-August coastal demand
    heating, cooling = np.clip(16 - temperature, 0, None), np.clip(temperature - 22, 0, None)

    noise = np.zeros(len(idx))                              # errors persist from hour to hour
    z = rng.normal(0, 30, len(idx))
    for t in range(1, len(idx)):
        noise[t] = 0.9 * noise[t - 1] + z[t]
    demand = (1950 + 38 * heating + 70 * cooling) * profile * tourism + noise
    return pd.DataFrame({"temperature": temperature, "holiday": holiday, "demand": demand}, index=idx)


def temperature_forecast(df: pd.DataFrame, seed: int = 5) -> pd.Series:
    """Day-ahead temperature forecast (deg C) as available at noon the day before: the actual temperature
    plus a forecast error of about 1.3 deg C on average that persists over hours and days."""
    rng = np.random.default_rng(seed)
    error = np.zeros(len(df))
    shocks = rng.normal(0, 0.5, len(df))
    for t in range(1, len(df)):
        error[t] = 0.95 * error[t - 1] + shocks[t]
    return pd.Series(df["temperature"].to_numpy() + error, index=df.index, name="temperature_forecast")
