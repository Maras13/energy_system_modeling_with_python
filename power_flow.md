# Energy System Modelling – Reading & Learning Guide  
*(Tailored for GIS Background)*

---

## 🎯 Overview

This guide provides structured resources and a learning path for:

- Power flow analysis  
- Basic principles of power flow in electric networks  
- Implementing DC power flow models in Python  
- Understanding the connection between network constraints and market outcomes  

---

## 🧭 How GIS Skills Translate to Energy Systems

### Existing strengths
- Spatial thinking → grid topology, transmission networks  
- Data handling → demand, generation, weather data  
- Visualization → flows, congestion, price maps  

### Skills to develop
- Power system physics  
- Linear algebra & optimization  
- Electricity market design  

---

## 📚 1. Power Flow Analysis

### Core textbooks

- *Power System Analysis* – Hadi Saadat  
  - Practical and intuitive  
  - Focus on:
    - Power flow basics  
    - DC approximation  

- *Modern Power System Analysis* – Kundur  
  - More advanced  
  - Recommended for deeper understanding  

---

### Key concepts

- Bus types:
  - PQ bus  
  - PV bus  
  - Slack bus  

- Load flow methods:
  - Newton–Raphson  
  - Fast decoupled method  

- Per-unit system  

---

## ⚡ 2. Basic Principles of Power Flow

### AC Power Flow Equation

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

