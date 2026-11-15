# 01 Market clearing

| Notebook | Lesson | Topic |
|---|---|---|
| `01_market_clearing.ipynb` | M2.1 | A day-ahead order book (synthetic, Croatia-sized), aggregate supply and demand curves, uniform-price (pay-as-clear) clearing by walking the curves, which order sets the price, clearing as a welfare-maximisation LP whose dual is the price, consumer and producer surplus (inframarginal rent), and the same market in PyPSA with demand bids — including a sign trap |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).
The exercise completes the clearing algorithm for price ranges, checks the LP dual against it, and
previews the merit-order effect: 800 MW of extra wind cut the price from 110 to 12 EUR/MWh.

All order books are **synthetic**. Real Croatian and neighbouring prices follow in M2.3.
