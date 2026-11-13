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
| `04_ee2_2_active_reactive_complex_power` | 2 | Instantaneous power, active/reactive/apparent power, S = V·I*, power factor and its correction, conservation of complex power, power transfer P = V₁V₂ sin δ / X, accuracy of the DC approximation, P–δ and Q–V coupling | DC power flow, PTDFs (M4), market coupling (M2), voltage control (M4) |
| `05_ee2_3_ac_power_flow` | 3 | Bus types (slack, PQ, PV), the AC power flow equations, Newton's method checked against pandapower, the P–V curve and loadability limit, voltage control with a PV bus and its reactive power limit | AC power flow, voltage stability (M4) |
| Maths-2 | 4–5 | LP geometry, vertices, duality | M3 |
| `06_ee3_1_three_phase_per_unit` | 4 | Balanced three-phase systems, phase and line-to-line voltages, constant three-phase power, why three phases save conductor material, the per-phase equivalent (why V_LL²/Z* is three-phase power), the per-unit system, base changes, transformers in per-unit checked against pandapower | Network data, pandapower and PyPSA models (M4) |
| `07_ee3_2_transmission_line_models` | 5 | Line parameters of overhead lines and cables, the nominal π model and ABCD two-ports, line charging (why long AC cables need HVDC), the Ferranti effect checked against pandapower, surge impedance loading, shunt reactors, the exact long-line model and its equivalent π | Line data in pandapower and PyPSA, voltage control (M4) |
| EE-3.3 | 6–7 | Transformers with tap changers and phase shifters, building the Y-bus of a real network from data | M4 |
| Maths-3 | 6–7 | Lagrangians, KKT conditions | M3, M4 (nodal prices) |

Each lesson: lecture notebook in this folder, exercises in `exercise/`, answer key in
`exercise/solutions/` (submit your own answers before opening it).

Setup: `pip install -r requirements.txt` from the repo root (EE-2.3 onwards uses pandapower).
