import streamlit as st
import numpy as np
import plotly.graph_objects as go
from src.lab_simulations_python.oscillations import calculate_oscillation, displacement

st.set_page_config(layout="wide")
st.title("Damped Harmonic Oscillator Simulation")
st.write("Use the sidebar to adjust the simulation parameters and click 'Run Simulation' to see the results")

# Sidebar for inputs
st.sidebar.header("Simulation Parameters")
mass = st.sidebar.slider("Mass (kg)", 0.1, 10.0, 1.0)
spring_constant = st.sidebar.slider("Spring Constant k (N/m)", 1.0, 100.0, 20.0)
amplitude = st.sidebar.slider("Initial Amplitude (m)", 0.1, 5.0, 1.0)
damping = st.sidebar.slider("Damping Coefficient b (kg/s)", 0.0, 20.0, 0.5)

st.write(
        f"Current parameters: mass **{mass} kg**, k **{spring_constant} N/m**, "
        f"Amplitude **{amplitude} m**, damping **{damping} kg/s**"
        )

# Main Simulation
if st.button("Run Simulation"):
    props = calculate_oscillation(mass, spring_constant, damping)

    t = np.linspace(0, 6 * props["period"], num=1000)
    x = displacement(t, mass, spring_constant, amplitude, damping)
    
    # Plotting
    st.subheader("Displacement vs. Time")

    fig = go.Figure(
            go.Scatter(
                x=t,
                y=x,
                mode="lines",
                hovertemplate="Time: %{x:.2f} s<br>Displacement: %{y:.3f} m<extra></extra>",
                )
            )

    fig.update_layout(
            title="Oscillator Displacement",
            xaxis_title="Time (s)",
            yaxis_title="Displacement (m)",
            plot_bgcolor="white",
            )

    fig.update_xaxes(
            range=[0, float(t.max()+1.0)],
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
            )
    fig.update_yaxes(
            ticks="outside", showgrid=True, gridcolor="lightgray",
            zeroline=True, zerolinewidth=2, zerolinecolor="black",
           )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader("Simulation Results")
    st.success(f"Simulation Complete = regime: **{props['regime']}**")

    col1, col2, col3 = st.columns(3)
    col1.metric("Natural Period", f"{props['period']:.2f} s")
    col2.metric("Natural Frequency", f"{props['natural_frequency']:.2f} Hz")
    col3.metric("Damping Ratio", f"{props['damping_ratio']:.2f}")
