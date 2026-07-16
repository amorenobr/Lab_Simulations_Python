import numpy as np
import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.i18n import language_selector, t
from src.lab_simulations_python.oscillations import calculate_oscillation, displacement

st.set_page_config(layout="wide")

language_selector()

st.title(t("osc_title"))
st.markdown(t("osc_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
mass = st.sidebar.slider(t("osc_mass"), 0.1, 10.0, 1.0)
spring_constant = st.sidebar.slider(t("osc_spring"), 1.0, 100.0, 20.0)
amplitude = st.sidebar.slider(t("osc_amplitude"), 0.1, 5.0, 1.0)
damping = st.sidebar.slider(t("osc_damping"), 0.0, 20.0, 0.5)

st.write(t("osc_current_params").format(m=mass, k=spring_constant, amp=amplitude, b=damping))

# Main Simulation
if st.button(t("run_simulation")):
    props = calculate_oscillation(mass, spring_constant, damping)

    t_arr = np.linspace(0, 6 * props["period"], num=1000)
    x = displacement(t_arr, mass, spring_constant, amplitude, damping)

    # Plotting
    st.subheader(t("osc_displacement_vs_time"))

    fig = go.Figure(go.Scatter(x=t_arr, y=x, mode="lines", hovertemplate=t("osc_hover")))

    fig.update_layout(
        title=t("osc_plot_title"),
        xaxis_title=t("time_s"),
        yaxis_title=t("osc_displacement_axis"),
        plot_bgcolor="white",
    )

    fig.update_xaxes(
        range=[0, float(t_arr.max() + 1.0)],
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )
    fig.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    regime_label = t(f"regime_{props['regime']}")
    st.success(t("osc_complete_regime").format(regime=regime_label))

    col1, col2, col3 = st.columns(3)
    col1.metric(t("osc_natural_period"), f"{props['period']:.2f} s")
    col2.metric(t("osc_natural_frequency"), f"{props['natural_frequency']:.2f} Hz")
    col3.metric(t("osc_damping_ratio"), f"{props['damping_ratio']:.2f}")
