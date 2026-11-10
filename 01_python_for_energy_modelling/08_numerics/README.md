# 08 NumPy and SciPy for energy numerics

| Notebook | Lesson | Topic |
|---|---|---|
| `01_numpy_scipy_newton.ipynb` | M1.3 (+ Maths-1.2) | Vectorisation and broadcasting over hours × assets, sparse linear algebra for networks, why constant-power loads make network equations nonlinear (two solutions, maximum transfer, voltage collapse), Newton's method in one dimension and for systems with a Jacobian |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).
The exercise builds a reusable `newton()` / `newton_system()`, a numerical Jacobian check, and a
10-bus radial feeder with constant-power loads — the direct precursor of AC power flow in Module 04.

## Setup
```bash
pip install numpy scipy pandas
```
Tested with NumPy 2.5 and SciPy 1.18. The availability data in the vectorisation section is synthetic.
