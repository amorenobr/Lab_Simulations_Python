import streamlit as st
import numpy as np
import plotly.graph_objects as go
from src.lab_simulations_python.projectile import calculate_kinematics

st.set_page_config(layout="wide")
st.title("Projectile Motion Simulation")
st.markdown(
        """
        **Projectile Motion** describes the path of an object launched into the air,
        moving under the influence of gravity alone (air resistance is neglected). The horizontal and
        vertical motions are independent: the horizontal velocity remains constant while the 
        vertical motion accelerates downward with acceleration $g = 9.81\\ \\mathrm{m/s^2}$.

        Given an initial speed $v_0$ and launch angle $\\theta$, the key quantities are:

        - **Time of flight:** $t = \\dfrac{2 v_0 \\sin\\theta}{g}$
        - **Maximum height:** $h = \\dfrac{v_0^2 \\sin^2\\theta}{2g}$
        - **Horizontal range:** $R = \\dfrac{v_0^2 \\sin(2\\theta)}{g}$

        Use the sidebar to set the initial speed and launch angle, then click **Run Simulation** 
        to view the trajectory and calculated results.
        """
        )

# Sidebar for inputs
st.sidebar.header("Simulation Parameters")
velocity_input = st.sidebar.slider("Initial Velocity (m/s)", 1.0, 100.0, 25.0)
angle_input = st.sidebar.slider("Launch Angle (degrees)", 0, 90, 45)

st.write(f"Current parameters: **{velocity_input} m/s** at **{angle_input}°**")

# Main Simulation
if st.button("Run Simulation"):
    # Calculations
    kinematics = calculate_kinematics(velocity_input, angle_input)
    t_flight = kinematics["t_flight"]

    # Trajectory plotting
    st.subheader("Trajectory Plot")

    angle_rad = np.deg2rad(angle_input)
    g = 9.81
    t = np.linspace(0, t_flight, num=500)
    x = velocity_input * np.cos(angle_rad) * t
    y = velocity_input * np.sin(angle_rad) * t - 0.5 * g * t**2

    fig = go.Figure(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                hovertemplate="Range: %{x:.2f} m<br>Height: %{y:.2f} m<extra></extra>",
                )
            )

    fig.update_layout(
            title="Projectile Trajectory",
            xaxis_title="Range (m)",
            yaxis_title="Height (m)",
            plot_bgcolor="white",
            )

    fig.update_xaxes(
            range=[0, float(x.max()+1.0)],
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
    fig.update_yaxes(
            range=[0, float(y.max()+1.0)],
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader("Simulation Results")
    st.success("Simulation Complete!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Time of Flight", f"{kinematics['t_flight']:.2f} s")
    col2.metric("Maximum Height", f"{kinematics['max_height']:.2f} m")
    col3.metric("Horizontal Range", f"{kinematics['horizontal_range']:.2f} m")
