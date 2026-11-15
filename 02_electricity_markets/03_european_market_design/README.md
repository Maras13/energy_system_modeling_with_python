# 03 European market design

| Notebook | Lesson | Topic |
|---|---|---|
| `03_european_market_design.ipynb` | M2.3 | The European market timeline (forward, day-ahead SDAC with 15-minute market time units since delivery day 1 October 2025, intraday SIDC, balancing); Croatia as a bidding zone coupled over its Slovenian and (since June 2022) Hungarian borders; three-zone market coupling (synthetic SI, HR, HU) as one welfare LP, checked against PyPSA; price convergence and price splits; congestion income and the welfare identity; why transfer capacities miss loop flows and what flow-based coupling adds; loading real day-ahead prices for HR, SI and HU from ENTSO-E and measuring their convergence |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).
The exercise builds the coupling LP, values each border's capacity (envelope theorem) and shows who
gains and who loses when markets are coupled.

**Real data:** the ENTSO-E download needs an API token in `.env` (see M1.1). It was **not run** while
this course was built; the analysis function is tested on a synthetic stand-in with the same shape.
Market facts are sourced in the notebook (SDAC, CROPEX).
