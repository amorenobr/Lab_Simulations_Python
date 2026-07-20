import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.i18n import language_selector, t
from src.lab_simulations_python.newtons_laws import calculate_newtons_laws, newton_series

st.set_page_config(layout="wide")

language_selector()

st.title(t("nl_title"))
st.markdown(t("nl_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
mass = st.sidebar.slider(t("nl_mass"), 0.1, 10.0, 2.0)
applied_force = st.sidebar.slider(t("nl_force"), 0.0, 100.0, 20.0)
friction_coefficient = st.sidebar.slider(t("nl_friction"), 0.0, 1.0, 0.2)
time_input = st.sidebar.slider(t("time_s"), 0.0, 10.0, 5.0)

st.write(
    t("nl_current_params").format(m=mass, f=applied_force, mu=friction_coefficient, tm=time_input)
)

# Main Simulation
if st.button(t("run_simulation")):
    results = calculate_newtons_laws(mass, applied_force, friction_coefficient, time_input)

    st.subheader(t("plots"))

    t_arr, v, x = newton_series(mass, applied_force, friction_coefficient, time_input)

    # Velocity vs. Time
    fig_v = go.Figure(go.Scatter(x=t_arr, y=v, mode="lines", hovertemplate=t("nl_hover_velocity")))
    fig_v.update_layout(
        title=t("nl_vel_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("nl_velocity_axis"),
        plot_bgcolor="white",
    )
    fig_v.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )
    fig_v.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )

    # Position vs. Time
    fig_x = go.Figure(go.Scatter(x=t_arr, y=x, mode="lines", hovertemplate=t("nl_hover_position")))
    fig_x.update_layout(
        title=t("nl_pos_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("nl_position_axis"),
        plot_bgcolor="white",
    )
    fig_x.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )
    fig_x.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )

    c1, c2 = st.columns(2)
    c1.plotly_chart(fig_v, width="stretch")
    c2.plotly_chart(fig_x, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("nl_friction_force"), f"{results['friction_force']:.2f} N")
    col2.metric(t("nl_net_force"), f"{results['net_force']:.2f} N")
    col3.metric(t("nl_acceleration"), f"{results['acceleration']:.2f} m/s^2")
    col4.metric(t("nl_final_velocity"), f"{results['final_velocity']:.2f} m/s")
