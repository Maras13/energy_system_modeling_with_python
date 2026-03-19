# Energy System Modelling – Reading & Learning Guide  


---

## 🎯 Overview

This guide provides structured resources and a learning path for:

- Power flow analysis  
- Basic principles of power flow in electric networks  
- Implementing DC power flow models in Python  
- Understanding the connection between network constraints and market outcomes  

---


## 📚 1. Power Flow Analysis

Core concepts

Kirchhoff’s laws (KCL, KVL)
Complex power: 
S=P+jQ

Voltage representation: magnitude + angle
Bus admittance matrix (Y-bus)
Types of buses: Slack, PV, PQ
Nonlinear equations:
​	
 
Methods to master
Newton–Raphson (most important)
Gauss–Seidel (basic intuition)
Fast decoupled load flow
👉 These are the core of AC power flow




### Core textbooks

- *Power System Analysis* – Hadi Saadat
- https://dn790008.ca.archive.org/0/items/ebox_ly_EE_EE342/power%20system%20analysis%20-%20hadi%20saadat_320503100.pdf
  - Practical and intuitive  
  - Focus on:
    - Power flow basics  
    - DC approximation  

- *Modern Power System Analysis*
- https://devanush.github.io/naidu.git.io/PSA/Modern%20Power%20System%20Analysis%20by%20Nagrath%20Kothari.pdf
- https://www.taylorfrancis.com/books/mono/10.1201/9781003129769/modern-power-system-analysis-chee-wooi-ten-yunhe-hou
  - More advanced  
  - Recommended for deeper understanding
 
  **Power System Analysis & Design – Glover/Sarma**
  - https://elcom-team.com/Subjects/نحليل%20انطمة%20القوى/power-system-analysis-book-(6th-ed).pdf

---

Methods to master
Newton–Raphson (most important)
Gauss–Seidel (basic intuition)
Fast decoupled load flow
👉 These are the core of AC power flow

---

## 
⚡ 2. DC Power Flow (Simplification you MUST master)

### DC Power Flow Equation

This is critical for markets + optimization.

Key idea
DC power flow = linear approximation of AC

Assumptions
Ignore resistance (lossless lines)
Voltage magnitude = 1 pu
Small angles → linearization
Resulting model

P=Bθ

B: susceptance matrix
θ: voltage angles
What you must be able to do

Build B matrix
Choose slack bus
Solve linear system


- https://github.com/soummyaroy1/dc-power-flow?utm_source=chatgpt.com


### Python tools

#### Primary tool
- PyPSA (Python for Power System Analysis)
  - Large-scale modelling  
  - Optimization + market simulation  
  - Strong integration with spatial data
 

  https://www.udemy.com/course/fundamentals-of-power-system-electrical-engineering-part-1/
  https://www.udemy.com/course/digsilent-powerfactory-power-systems-analysis/

#### Supporting tools
- pandapower → AC power flow   https://www.pandapower.org
- PYPOWER → https://pypi.org/project/PYPOWER/



### Typical workflow

1. Define network (buses, lines)  
2. Build susceptance matrix  
3. Solve linear system  
4. Compute line flows  

---

## 💰 4. Network Constraints & Market Outcomes

### Core idea

Electricity markets are:

> Optimization problems over a spatial network

Concepts to master
1. Economic dispatch
Cheapest generators run first
2. Congestion
Lines get full → cannot send cheap power
3. Locational Marginal Pricing (LMP)
Price at each node =
energy cost
congestion cost
losses (optional)-

### Important insight

- No constraints → single price  
- With constraints → price separation



- https://arxiv.org/abs/2011.11594?utm_source=chatgpt.com

---

### Optimization formulation (DC-OPF)

Minimize:


P = B * θ



Where:
- P = active power injections  
- B = susceptance matrix  
- θ = voltage angles  

---

### Assumptions

- Voltage magnitudes ≈ 1 p.u.  
- Small angle differences  
- Ignore reactive power  

---

### Python tools

#### Primary tool
- PyPSA (Python for Power System Analysis)
  - Large-scale modelling  
  - Optimization + market simulation  
  - Strong integration with spatial data  

#### Supporting tools
- pandapower → AC power flow  
- PYPOWER → academic reference implementation  

#### GIS-related stack
- geopandas  
- shapely  
- xarray  

---

### Typical workflow

1. Define network (buses, lines)  
2. Build susceptance matrix  
3. Solve linear system  
4. Compute line flows  

---

## 💰 4. Network Constraints & Market Outcomes

### Core idea

Electricity markets are:

> Optimization problems over a spatial network

---

### Congestion

When transmission lines are limited:
- Cheap generation cannot reach demand  
- Prices differ across locations  

---

### Key concept: Locational Marginal Pricing (LMP)

Components:
- Energy cost  
- Congestion cost  
- Losses  

---

### Important insight

- No constraints → single price  
- With constraints → price separation  

---

### Optimization formulation (DC-OPF)

Minimize:

Total generation cost



Subject to:
- Power balance  
- Line capacity limits  

---

### Key reference

- PyPSA: Python for Power System Analysis (paper)
  - Links:
    - Power flow  
    - Optimization  
    - Market outcomes  

---

## 🧠 Conceptual Mapping (GIS → Energy Systems)

| GIS Concept        | Energy System Equivalent |
|------------------|------------------------|
| Road network      | Transmission grid       |
| Traffic flow      | Power flow             |
| Congestion        | Line congestion        |
| Travel cost       | Marginal cost          |
| Shortest path     | Economic dispatch      |
| Bottlenecks       | Price separation       |

---

## 🛠️ Suggested Projects

### Project 1 – DC Power Flow (Basic)
- Small network (5–10 nodes)  
- Implement DC power flow in Python  
- Visualize flows  

---

### Project 2 – System Modelling (Recommended)
- Use PyPSA  
- Model Germany or Europe  
- Include:
  - Wind  
  - Solar  
  - Demand  

Visualize:
- Congestion  
- Nodal prices  

---

### Project 3 – Advanced
- Add:
  - Storage  
  - Grid expansion  

Analyze:
- Impact on renewable integration  
- Price changes  

---

## 🚀 Learning Path

### Step 1 – Theory
- Learn AC power flow basics  
- Understand physical constraints  

### Step 2 – Simplification
- Learn DC approximation  
- Understand assumptions  

### Step 3 – Implementation
- Start with simple Python models  
- Move to PyPSA  

### Step 4 – Markets
- Study DC Optimal Power Flow  
- Understand pricing mechanisms  

---

## 🔥 Key Focus Areas (Career-Relevant)

- Spatial energy system modelling  
- Renewable integration  
- Grid congestion analysis  
- Cross-border electricity flows  

---

## 📌 Summary

To transition from GIS to energy modelling:

1. Learn simplified power system physics  
2. Focus on DC power flow  
3. Use Python tools (especially PyPSA)  
4. Understand how network constraints shape markets  

---

