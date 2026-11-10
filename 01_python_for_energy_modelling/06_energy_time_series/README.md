# 06 Energy time series

| Notebook | Lesson | Topic |
|---|---|---|
| `01_entsoe_data_and_validation.ipynb` | M1.1 | ENTSO-E Transparency Platform, security token, Croatian load with `entsoe-py`, time zones and DST, validation checks, resampling MW vs. MWh |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).

## Setup
```bash
pip install entsoe-py python-dotenv
```
Put your token in a `.env` file (`ENTSOE_API_KEY=...`). `.env` is already in `.gitignore` — never commit it.
Without a token the notebooks still run; cells that download real data are skipped.

> The teaching sample in these notebooks is **synthetic** (shaped like ENTSO-E data, with planted
> defects). Real Croatian data come from the ENTSO-E API with your own token.
