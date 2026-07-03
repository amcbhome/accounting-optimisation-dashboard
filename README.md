# Accounting Optimisation Dashboard

An interactive decision-support application built with Python and Streamlit that demonstrates linear programming techniques used in accounting, management accounting, and business optimisation.

The application enables users to perform real-time **what-if analysis** by varying objective functions and operational constraints to identify optimal business decisions.

---

## Live Demo

https://acca-optimisation-june26-mq9aziacqlsegrmeavczfj.streamlit.app/

---

## Overview

Linear programming is an optimisation technique used in management accounting and operations research to maximise profit or minimise cost subject to constraints such as labour, materials, and production capacity.

This project transforms traditional static textbook examples into an interactive web application where users can experiment with different business scenarios and instantly observe how changes affect optimal outcomes.

Rather than solving a single fixed problem, this tool provides a reusable optimisation engine for decision support and learning.

---

## Business Problem

Organisations frequently need to answer questions such as:

- Which combination of products maximises profit or contribution?
- How should limited labour and material resources be allocated?
- What happens if capacity constraints change?
- How does demand variation affect optimal decisions?
- Which scenario produces the best financial outcome?

These problems are central to:

- Performance Management
- Management Accounting
- Operations Research
- Supply Chain Planning
- Resource Allocation
- Production Planning

---

## Solution

The application allows users to define and modify:

- Objective function coefficients (profit/contribution/cost per unit)
- Decision variables
- Resource constraints
- Capacity limits
- Optimisation direction (Maximise or Minimise)

The model is then solved using linear programming methods, and results are updated instantly.

Users can repeatedly adjust inputs to perform **what-if analysis** and observe how optimal decisions change in real time.

---

## Features

- Interactive Streamlit web interface
- Linear programming optimisation engine
- Fully configurable objective function
- Adjustable constraints and limits
- Real-time scenario (what-if) analysis
- Instant recalculation of optimal solutions
- Educational breakdown of optimisation logic
- Browser-based deployment (no installation required for users)

---

## Screenshot

*(Add your screenshot here)*

```
images/dashboard.png
```

---

## Application Architecture

```
User Input
      │
      ▼
Streamlit Interface
      │
      ▼
Linear Programming Model
      │
      ▼
Optimisation Solver
      │
      ▼
Optimal Solution
      │
      ▼
What-if Analysis Output
```

---

## Technology Stack

- Python
- Streamlit
- PuLP (Linear Programming Solver)
- NumPy
- Pandas

---

## Running the Application Locally

Clone the repository:

```bash
git clone https://github.com/amcbhome/accounting-optimisation-dashboard.git
```

Navigate into the project directory:

```bash
cd accounting-optimisation-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## Educational Purpose

This project is inspired by optimisation techniques taught in the ACCA Performance Management (PM) syllabus.

The ACCA technical article introduces linear programming as a method for solving product mix and resource allocation problems where organisations aim to maximise contribution subject to constraints.

The article can be found here:

https://www.accaglobal.com/uk/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/linear-programming.html

This application is an independent implementation that extends those concepts into an interactive decision-support tool built with Python and Streamlit.

---

## Skills Demonstrated

- Python programming
- Linear programming modelling
- Management accounting concepts
- Decision support systems
- Data-driven analysis
- What-if scenario modelling
- Streamlit dashboard development
- Business optimisation techniques

---

## Example Applications

This tool can model:

- Product mix optimisation
- Resource allocation problems
- Transportation and distribution problems
- Production planning
- Budget optimisation
- Capacity planning
- Blending problems

---

## Why This Project?

Traditional linear programming examples are static and difficult to explore beyond a single solution.

This dashboard transforms optimisation into an interactive environment where users can:
- Change assumptions
- Test scenarios
- Compare outcomes
- Understand sensitivity of decisions

This makes optimisation concepts more intuitive and practically useful.

---

## Future Improvements

- Graphical feasible region visualisation
- Sensitivity analysis (shadow prices, reduced costs)
- Integer programming support
- Multi-objective optimisation
- Scenario comparison dashboard
- Exportable reports (PDF/Excel)
- Advanced business templates (ACCA-style presets)

---

## Author

**Alastair McBride**  
BAcc (Hons) Accounting  

Interests:
- Management Accounting
- Data Analytics
- Python Development
- Business Optimisation
- Decision Support Systems
- AI in Accounting
```

If you want next upgrade, I can help you turn this into a **portfolio landing page** or make your README more “recruiter-optimised” (more impact, fewer words, higher interview conversion).
