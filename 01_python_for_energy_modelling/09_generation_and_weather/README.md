# 09 From weather to power

| Notebook | Lesson | Topic |
|---|---|---|
| `01_weather_to_power.ipynb` | M1.4 | Capacity factors; wind power and the cube law, hub-height scaling, turbine power curves, Weibull statistics (two independent CF methods); solar position from first principles validated against pvlib, clear-sky irradiance and PV output as an upper bound; real hourly ERA5 weather from Open-Meteo |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).
The exercise builds the full weather → `p_max_pu` pipeline for PyPSA and tests it offline; one
challenge cell downloads real 2024 weather for Split.

## Setup
```bash
pip install numpy pandas scipy pvlib requests
```
Tested with pvlib 0.16.1. Cells that call Open-Meteo need internet access and were **not** executed
when the notebooks were prepared; they skip cleanly without a connection.

## Data source
[Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) (ERA5
reanalysis), free for non-commercial use, CC BY 4.0 — credit the source in your projects.
Watch the units: wind speed defaults to km/h (request `wind_speed_unit=ms`), and
`shortwave_radiation` is the mean of the preceding hour.

> The turbine power curve is generic, not a specific model; solar output assumes horizontal panels.
