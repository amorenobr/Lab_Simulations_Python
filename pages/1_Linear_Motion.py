import streamlit as st
import numpy as np
import plotly.graph_objects as go
from src.lab_simulations_python.linear_motion import calculate_linear_motion

st.set_page_config(layout="wide")
st.title("Linear Motion Simulation")
st.markdown(
        """
        **Linear Motion** describes the path of an object on X with a constant acceleration.

        Given an initial position $x_0$, and initial velocity $v_0$, a constant acceleration $a$, and a time $t$, we obtain:

        - **Final position:** $x_f = x_0 + (v_0 * t) + \\dfrac{1}{2}*a*t^2$
        - **Final velocity:** $v_f = v_0 + a * t$

        Use the sidebar to set the initial position, initial velocity, constant acceleration and time, then click the 
        "Run Simulation" to view the plots and calculated results.
        """
        )

# Sidebar for inputs
st.sidebar.header("Simulation Parameters")
position_input = st.sidebar.slider("Initial Position (m)", 0.0, 100.0, 20.0)
velocity_input = st.sidebar.slider("Initial Velocity (m/s)", 0.0, 100.0, 20.0)
acceleration_input = st.sidebar.slider("Constant Acceleration (m/s^2)", 0.0, 30.0, 5.0)
time_input = st.sidebar.slider("Time (s)", 0.0, 100.0, 10.0)

st.write(f"Current parameters: **{position_input} m**, **{velocity_input} m/s**, **{acceleration_input} m/s^2** and **{time_input} s**")

# Main Simulation
if st.button("Run Simulation"):
    # Calculations
    kinematics = calculate_linear_motion(position_input, velocity_input, acceleration_input, time_input)


    # Plotting
    st.subheader("Plots")

    t = np.linspace(0, time_input, num=500)
    x = position_input + (velocity_input * t) + (0.5 * acceleration_input * t**2)
    v = velocity_input + (acceleration_input * t)

    # Position vs Time
    fig_x = go.Figure(
            go.Scatter(
                x=t,
                y=x,
                mode="lines",
                hovertemplate="Time: %{x:.2f} s<br>Position: %{y:.2f} m<extra></extra>",
                )
            )

    fig_x.update_layout(
            title="Position vs. Time",
            xaxis_title="Time (s)",
            yaxis_title="Position (m)",
            plot_bgcolor="white",
            )

    fig_x.update_xaxes(
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
    fig_x.update_yaxes(
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
#    st.plotly_chart(fig_x, width="stretch") 

     # Velocity vs Time
    fig_v = go.Figure(
            go.Scatter(
                x=t,
                y=v,
                mode="lines",
                hovertemplate="Time: %{x:.2f} s<br>Velocity: %{y:.2f} m/s<extra></extra>",
                )
            )

    fig_v.update_layout(
            title="Velocity vs. Time",
            xaxis_title="Time (s)",
            yaxis_title="Velocity (m/s)",
            plot_bgcolor="white",
            )

    fig_v.update_xaxes(
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
    fig_v.update_yaxes(
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
#    st.plotly_chart(fig_v, width="stretch")

    # Render both plots side by side
    c1, c2 = st.columns(2)
    c1.plotly_chart(fig_x, width="stretch")
    c2.plotly_chart(fig_v, width="stretch")

    # Results
    st.subheader("Simulation Results")
    st.success("Simulation Complete!")

    col1, col2 = st.columns(2)
    col1.metric("Final Position", f"{kinematics['final_position']:.2f} m")
    col2.metric("Final Velocity", f"{kinematics['final_velocity']:.2f} m/s")

