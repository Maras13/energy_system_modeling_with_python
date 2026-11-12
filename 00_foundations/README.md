# 00 Foundations — electrical engineering and targeted maths

This track runs alongside the main modules in weeks 1–9 and is complete before Module 04
(power flow) needs it. It assumes a data/software background with no circuits experience,
and maths that was studied but is rusty.

| Lesson | Week | Topic | Used later in |
|---|---|---|---|
| `01_ee1_circuits_from_zero` | 1 | Charge, current, voltage, power vs. energy, Ohm, I²R losses, Kirchhoff, nodal analysis, conductance matrix (+ Maths-1.1 linear systems) | Nodal balance in PyPSA (M1), Y-bus (M4) |
| `02_ee1_2_sources_superposition_thevenin` | 1 | Real voltage and current sources, nodal analysis with fixed voltages (the slack bus), superposition (and why power does not superpose), Thevenin equivalents, grid strength, maximum power transfer, first distribution factors | Slack bus and PTDFs (M4), grid strength (M4, M5) |
| Maths-1.2 → taught in [M1.3](../01_python_for_energy_modelling/08_numerics/) | 2 | Newton's method in one and many dimensions, Jacobians, constant-power loads, voltage collapse | AC power flow (M4) |
| `03_ee2_1_ac_phasors_impedance` | 2 | AC and RMS values, phasors as complex numbers, impedance of R, L and C, phasors validated against a time-domain simulation, resonance, the complex admittance matrix (Y-bus), why lines turn voltage angles | Y-bus, AC power flow, DC approximation (M4) |
| EE-2.2–2.3 | 2–3 | Active, reactive and complex power, power factor, power flow over a line | M2, M4 |
| Maths-2 | 4–5 | LP geometry, vertices, duality | M3 |
| EE-3.1–3.3 | 4–7 | Three-phase, per-unit, transmission line models, the Y-bus | M4 |
| Maths-3 | 6–7 | Lagrangians, KKT conditions | M3, M4 (nodal prices) |

Each lesson: lecture notebook in this folder, exercises in `exercise/`, answer key in
`exercise/solutions/` (submit your own answers before opening it).
