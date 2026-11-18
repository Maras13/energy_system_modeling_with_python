# Assessments

Two assessments check the course at its halfway points (course plan, *Checkpoints*): **Assessment 1** in
week 11 covers weeks 1–11, **Assessment 2** in week 19 covers weeks 12–18. A missed or failed
assessment is closed in the next review week before moving on.

## Assessment 1 — weeks 1–11

[`assessment_1.ipynb`](assessment_1.ipynb): eight tasks across the foundations track (EE and maths),
Module 01 (Python and data), Module 02 (markets), Module 03 (linear programming and operations) and the
forecasting module. **6 hours, 100 points, pass mark 60.**

**Rules**

- Open book — your notes, the course notebooks and library documentation — but your own work: no
  help from other people or AI assistants.
- Every function must run from a fresh kernel in the course environment (`pip install -r requirements.txt`).
- The test cells check that results are **consistent** (energy conserved, the power triangle closing,
  the KKT pattern holding) — not that they are right. Passing all tests does not mean full marks.
- Written answers are short, precise and in your own words; they carry as many points as the code.
- Submit the notebook run from top to bottom. The answer key in [`solutions/`](solutions/) is opened only
  after marking.

**Marking**

| Task | Topic | Points | Full marks need |
|---|---|---|---|
| 1 | Three-phase power and power-factor correction | 8 | Correct S, Q, I and capacitor; why the operator cares about current, not energy |
| 2 | Newton's method on a power-flow equation | 8 | Converging Newton iteration with a guard for infeasible P; the maximum-transfer limit explained physically |
| 3 | 15-minute data across both clock changes | 12 | Gaps found and filled, energy conserved, 23- and 25-hour days identified; what tz-naive handling breaks |
| 4 | Market clearing as a welfare LP; carbon switching price | 12 | Correct price with the dual's sign handled; accepted and rejected bids explained; switching price |
| 5 | Dispatch LP with a ramp limit | 16 | Own LP = PyPSA to 10⁻⁶; the negative price derived from the binding ramp constraint with KKT |
| 6 | A reservoir and its water value | 12 | Water value as a positive dual; KKT pattern; why a zero-price offer misuses water |
| 7 | Code review of a leaky forecast | 18 | All three leaks named with their effect; an honest forecast (time split, available features, temperature forecast); a clear message to the colleague |
| 8 | Newsvendor decision and brief | 14 | Correct quantile and direction; the saving; a brief under 120 words with recommendation, number and risk |

Within each task, about half the points are for working code and correct numbers and half for the
explanation. Partial credit is given for a correct method with an arithmetic slip, and for a clearly
reasoned answer that reaches a wrong number.

## Assessment 2 — weeks 12–18

Planned for week 19, after the networks and expansion-planning modules.
