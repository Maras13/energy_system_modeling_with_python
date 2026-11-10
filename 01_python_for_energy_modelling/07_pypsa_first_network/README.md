# 07 Your first PyPSA network

| Notebook | Lesson | Topic |
|---|---|---|
| `01_pypsa_first_network.ipynb` | M1.2 | PyPSA data model (snapshots, buses, carriers, loads, generators), static vs. time-varying data, a one-week dispatch of a stylised Croatia-like system, prices, validation against the merit order, emissions, and the LP inside (`n.model`) |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).

## Setup
```bash
pip install pypsa highspy matplotlib entsoe-py python-dotenv
```
Built and tested with PyPSA 1.4.0 and HiGHS.

> The system is **stylised**: round capacities and costs inspired by the Croatian mix, not official
> data, and synthetic load, wind and solar profiles. Real load replaces the synthetic one in exercise
> task 7 (ENTSO-E token needed); real wind and solar profiles follow in M1.4.
