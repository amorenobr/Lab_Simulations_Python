import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.i18n import language_selector, t
from src.lab_simulations_python.momentum import calculate_momentum, collision_series

st.set_page_config(layout="wide")

language_selector()

st.title(t("mom_title"))
st.markdown(t("mom_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
mass1 = st.sidebar.slider(t("mom_mass1"), 0.1, 10.0, 2.0)
velocity1 = st.sidebar.slider(t("mom_velocity1"), -10.0, 10.0, 3.0)
mass2 = st.sidebar.slider(t("mom_mass2"), 0.1, 10.0, 1.0)
velocity2 = st.sidebar.slider(t("mom_velocity2"), -10.0, 10.0, -1.0)

# Translated radio labels mapped back to the internal collision type keys
collision_options = {t("mom_elastic"): "elastic", t("mom_inelastic"): "inelastic"}
collision_choice = st.sidebar.radio(t("mom_collision_type"), list(collision_options.keys()))
collision_type = collision_options[collision_choice]

st.write(
    t("mom_current_params").format(
        m1=mass1, u1=velocity1, m2=mass2, u2=velocity2, ctype=collision_choice
    )
)

# Main Simulation
if st.button(t("run_simulation")):
    results = calculate_momentum(mass1, velocity1, mass2, velocity2, collision_type)

    st.subheader(t("plots"))

    t_arr, x1, x2 = collision_series(mass1, velocity1, mass2, velocity2, collision_type)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=t_arr, y=x1, mode="lines", name=t("mom_object1"), hovertemplate=t("mom_hover"))
    )
    fig.add_trace(
        go.Scatter(x=t_arr, y=x2, mode="lines", name=t("mom_object2"), hovertemplate=t("mom_hover"))
    )
    fig.update_layout(
        title=t("mom_pos_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("mom_position_axis"),
        plot_bgcolor="white",
    )
    fig.update_xaxes(
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
    st.success(t("sim_complete"))

    ke_lost = results["kinetic_energy_before"] - results["kinetic_energy_after"]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("mom_final_v1"), f"{results['final_velocity_1']:.2f} m/s")
    col2.metric(t("mom_final_v2"), f"{results['final_velocity_2']:.2f} m/s")
    col3.metric(t("mom_momentum"), f"{results['momentum_after']:.2f} kg.m/s")
    col4.metric(t("mom_ke_lost"), f"{ke_lost:.2f} J")
