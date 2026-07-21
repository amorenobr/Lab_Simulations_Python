import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.i18n import language_selector, t
from src.lab_simulations_python.work_energy import calculate_work_energy, energy_series

language_selector()

st.title(t("we_title"))
st.markdown(t("we_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
mass = st.sidebar.slider(t("we_mass"), 0.1, 10.0, 2.0)
initial_height = st.sidebar.slider(t("we_height"), 0.0, 100.0, 50.0)
initial_velocity = st.sidebar.slider(t("we_velocity"), 0.0, 50.0, 0.0)
time_input = st.sidebar.slider(t("time_s"), 0.0, 10.0, 3.0)

st.write(t("we_current_params").format(m=mass, h=initial_height, v=initial_velocity, tm=time_input))

# Main Simulation
if st.button(t("run_simulation")):
    results = calculate_work_energy(mass, initial_height, initial_velocity, time_input)

    st.subheader(t("plots"))

    t_arr, ke, pe, total = energy_series(mass, initial_height, initial_velocity, time_input)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=t_arr, y=ke, mode="lines", name=t("we_ke"), hovertemplate=t("we_hover"))
    )
    fig.add_trace(
        go.Scatter(x=t_arr, y=pe, mode="lines", name=t("we_pe"), hovertemplate=t("we_hover"))
    )
    fig.add_trace(
        go.Scatter(x=t_arr, y=total, mode="lines", name=t("we_total"), hovertemplate=t("we_hover"))
    )
    fig.update_layout(
        title=t("we_energy_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("we_energy_axis"),
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

    col1, col2, col3 = st.columns(3)
    col1.metric(t("we_ke"), f"{results['kinetic_energy']:.2f} J")
    col2.metric(t("we_pe"), f"{results['potential_energy']:.2f} J")
    col3.metric(t("we_total"), f"{results['total_energy']:.2f} J")
