# Energy forecasting (weeks 10–11)

Every model in Modules 02 and 03 took demand, wind and solar as known. Real operation runs on
**forecasts**: the day-ahead market closes at noon, so tomorrow's demand, renewable output and prices
must be predicted today. This module builds those forecasts — from honest baselines to statistical and
machine-learning models and probabilistic forecasts — and asks what forecast errors cost the system.

## How to use this module

Weeks 10–11 of the course plan, ending with **Assessment 1** in week 11. Setup:
`pip install -r requirements.txt` from the repo root (this module adds `statsmodels` and
`scikit-learn`). The lessons use synthetic, Croatia-sized data from [`forecast_data.py`](forecast_data.py)
— demand driven by temperature, with Croatian public holidays — so that every method can be checked
against how the data were made. Real-data cells use ENTSO-E with an `ENTSOE_API_KEY` in `.env` (M1.1)
and are skipped without one.

| Lesson | Topic | Status |
|---|---|---|
| `01_forecasting_basics` | Splitting in time, what is known at noon (the day-ahead information set and its leaks), persistence / seasonal-naive / climatology baselines, MAE, RMSE, bias, MAPE and MASE, errors by hour and on holidays, the TSO's forecast as a benchmark | ready |
| 2 · statistical models | Regression on temperature and calendar, SARIMA, residual diagnostics | planned |
| 3 · machine learning | Gradient boosting, feature engineering, leakage through features, cross-validation in time | planned |
| 4 · probabilistic forecasts | Quantiles and prediction intervals, pinball loss and coverage; solar, wind and price forecasts | planned |
| 5 · forecasts in operations | What forecast errors cost in dispatch (Module 03), reserves and the value of a better forecast | planned |
| Assessment 1 | Week 11: review of Modules 01–03 and this module | planned |

Each lesson: lecture notebook in this folder, exercises in `exercise/`, answer key in
`exercise/solutions/` (submit your own answers before opening it).
