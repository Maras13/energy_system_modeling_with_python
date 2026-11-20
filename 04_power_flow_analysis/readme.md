<img width="606" height="1163" alt="Screenshot 2026-04-17 at 15 45 30" src="https://github.com/user-attachments/assets/547430d5-cb54-4cdc-bce9-796544d0df5f" />



<img width="604" height="892" alt="Screenshot 2026-04-17 at 15 45 55" src="https://github.com/user-attachments/assets/355d39ba-b033-4463-b622-c5cbd4e4f524" />





<img width="617" height="716" alt="Screenshot 2026-04-17 at 15 46 27" src="https://github.com/user-attachments/assets/ba8f7f98-d025-4b9a-9586-7b54d942460c" />





<img width="592" height="875" alt="Screenshot 2026-04-17 at 15 46 46" src="https://github.com/user-attachments/assets/a0155999-3002-4cd4-831f-1775f99e670c" />




<img width="607" height="1207" alt="Screenshot 2026-04-17 at 15 47 10" src="https://github.com/user-attachments/assets/5594f1f5-8c7a-4126-9811-1bcbb5335078" />

## How to use this module

Weeks 12–15 of the course plan: networks and reliability. Prerequisites: the foundations track — EE-2.3
(two-bus AC power flow), EE-3.2 (line models) and EE-3.3 (transformers and the Y-bus) — and Module 03's
LP duality for nodal prices. Setup: `pip install -r requirements.txt` from the repo root. The week-15
checkpoint: **your own Newton–Raphson matches pandapower to 10⁻⁸ p.u., and you can explain how the DC
approximation differs.** [`power_flow.md`](power_flow.md) is a reading guide with textbook references.

| Lesson | Topic | Status |
|---|---|---|
| `01_newton_raphson_power_flow` | The AC power flow equations for many buses, your own Newton–Raphson in polar form checked against pandapower to 10⁻⁸ on the IEEE 14-bus system, quadratic convergence, losses and the slack, the loadability limit (and, in the exercise, generator reactive limits) | ready |
| `02_solution_methods` | Gauss–Seidel with acceleration, the fast decoupled load flow with two matrices factorised once, cost per iteration against number of iterations on networks up to 1,354 buses, where decoupling breaks down (high resistance), the slack-angle trap | ready |
| `03_dc_approximation` | The DC power flow derived from the AC equations and its four assumptions, your own DC solver against pandapower, DC against AC (losses, loading, resistance), PyPSA `pf()`/`lpf()` = pandapower on a stylised Croatian 400 kV network; in the exercise, an overload DC cannot see | ready |
| 4 · congestion and nodal prices | PTDFs, line limits in the dispatch LP, locational marginal prices and congestion rent | planned |
| 5 · market coupling | Zones versus nodes, net transfer capacities, flow-based allocation | planned |
| 6 · redispatch and N-1 | Security-constrained dispatch, contingency analysis, redispatch cost | planned |
| 7 · voltage and reactive power | Voltage control, reactive reserves, compensation | planned |
| 8 · frequency and reserves | The swing equation, inertia, reserves; an introduction to dynamic simulation | planned |
| P4 | Portfolio project: the South-East European network, cross-border flows, AC feasibility | planned |

Each lesson: lecture notebook in this folder, exercises in `exercise/`, answer key in
`exercise/solutions/` (submit your own answers before opening it).
