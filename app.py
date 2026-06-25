import streamlit as st
import pulp
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Linear Programming Optimizer",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Linear Programming Production Optimizer")
st.markdown("""
This application optimizes the production mix of two products ($x$ and $y$) to maximize total profit 
based on your available material and labor constraints.
""")

st.sidebar.header("🔧 Model Parameters")

# --- STEP 1: OBJECTIVE FUNCTION INPUTS ---
st.sidebar.subheader("Objective Function (Profit)")
profit_x = st.sidebar.number_input("Profit per unit of X ($)", value=30.0, step=1.0)
profit_y = st.sidebar.number_input("Profit per unit of Y ($)", value=40.0, step=1.0)

# --- STEP 2: CONSTRAINT INPUTS ---
st.sidebar.subheader("Resource Constraints")

st.sidebar.markdown("**Constraint 1 (e.g., Material)**")
c1_x = st.sidebar.number_input("Units of Material used per X", value=3.0, step=0.1, key="c1_x")
c1_y = st.sidebar.number_input("Units of Material used per Y", value=5.0, step=0.1, key="c1_y")
c1_max = st.sidebar.number_input("Total Material Available", value=16000.0, step=100.0, key="c1_max")

st.sidebar.markdown("**Constraint 2 (e.g., Labor)**")
c2_x = st.sidebar.number_input("Units of Labor used per X", value=2.5, step=0.1, key="c2_x")
c2_y = st.sidebar.number_input("Units of Labor used per Y", value=1.5, step=0.1, key="c2_y")
c2_max = st.sidebar.number_input("Total Labor Available", value=13000.0, step=100.0, key="c2_max")

# --- MAIN PAGE DISPLAY ---
st.subheader("Current Model Formulation")
st.latex(rf"\text{{Maximize }} C = {profit_x:g}x + {profit_y:g}y")
st.latex(rf"\text{{Subject to:}}")
st.latex(rf"{c1_x:g}x + {c1_y:g}y \le {c1_max:,.0f}")
st.latex(rf"{c2_x:g}x + {c2_y:g}y \le {c2_max:,.0f}")
st.latex(r"x \ge 0, \quad y \ge 0")

st.markdown("---")

# --- STEP 3: SOLVER LOGIC ---
if st.button("🚀 Calculate Optimal Solution", type="primary"):
    # Initialize Problem
    prob = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)
    
    # Decision Variables
    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('y', lowBound=0, cat='Continuous')
    
    # Objective Function
    prob += profit_x * x + profit_y * y, "Total_Profit"
    
    # Constraints
    prob += c1_x * x + c1_y * y <= c1_max, "Material_Constraint"
    prob += c2_x * x + c2_y * y <= c2_max, "Labor_Constraint"
    
    # Solve
    status = prob.solve()
    
    # Check status and display results
    if pulp.LpStatus[status] == "Optimal":
        st.success("🎉 Optimal Solution Found Successfully!")
        
        # Display Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Optimal X Units", value=f"{pulp.value(x):,.2f}")
        with col2:
            st.metric(label="Optimal Y Units", value=f"{pulp.value(y):,.2f}")
        with col3:
            st.metric(label="Maximum Profit", value=f"${pulp.value(prob.objective):,.2f}")
            
        # Slack / Unused Resources Table
        st.subheader("📋 Resource Utilization & Slack")
        
        slack_data = []
        # Constraint 1 Row
        slack_data.append({
            "Resource": "Material (Constraint 1)",
            "Usage / Limit": f"{(c1_x * pulp.value(x) + c1_y * pulp.value(y)):,.2f} / {c1_max:,.2f}",
            "Unused Slack": f"{prob.constraints['Material_Constraint'].slack:,.2f}",
            "Status": "Binding" if prob.constraints['Material_Constraint'].slack == 0 else "Not Binding"
        })
        # Constraint 2 Row
        slack_data.append({
            "Resource": "Labor (Constraint 2)",
            "Usage / Limit": f"{(c2_x * pulp.value(x) + c2_y * pulp.value(y)):,.2f} / {c2_max:,.2f}",
            "Unused Slack": f"{prob.constraints['Labor_Constraint'].slack:,.2f}",
            "Status": "Binding" if prob.constraints['Labor_Constraint'].slack == 0 else "Not Binding"
        })
        
        df_slack = pd.DataFrame(slack_data)
        st.table(df_slack.set_index("Resource"))
        
    else:
        st.error(f"Could not find an optimal solution. Solver Status: {pulp.LpStatus[status]}")
