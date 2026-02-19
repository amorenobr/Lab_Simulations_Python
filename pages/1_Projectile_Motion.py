import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.lab_simulations_python.projectile import calculate_kinematics

st.set_page_config(layout="wide")
st.title("Projectile Motion Simulation")
st.write("Use the sidebar to adjust the simulation parameters and click 'Run Simulation' to see the results")

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

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Projectile Trajectory")
    ax.set_xlabel("Range (m)")
    ax.set_ylabel("Height (m)")
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    ax.set_ylim(bottom=0)
    st.pyplot(fig)

    # Results
    st.subheader("Simulation Results")
    st.success("Simulation Complete!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Time of Flight", f"{kinematics['t_flight']:.2f} s")
    col2.metric("Maximum Height", f"{kinematics['max_height']:.2f} m")
    col3.metric("Horizontal Range", f"{kinematics['horizontal_range']:.2f} m")
