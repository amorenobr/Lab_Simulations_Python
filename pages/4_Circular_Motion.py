import numpy as np
import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.circular_motion import calculate_circular_motion, circular_series
from src.lab_simulations_python.i18n import language_selector, t

st.set_page_config(layout="wide")

language_selector()

st.title(t("circ_title"))
st.markdown(t("circ_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
radius = st.sidebar.slider(t("circ_radius"), 0.1, 10.0, 2.0)
angular_velocity = st.sidebar.slider(t("circ_omega"), 0.1, 10.0, 2.0)
time_input = st.sidebar.slider(t("time_s"), 0.0, 20.0, 5.0)

st.write(t("circ_current_params").format(r=radius, w=angular_velocity, tm=time_input))

# Main Simulation
if st.button(t("run_simulation")):
    results = calculate_circular_motion(radius, angular_velocity, time_input)

    st.subheader(t("plots"))

    # Plot 1: Circular path + current position marker
    theta = np.linspace(0, 2 * np.pi, 200)
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)

    fig_circle = go.Figure()
    fig_circle.add_trace(
        go.Scatter(x=circle_x, y=circle_y, mode="lines", hoverinfo="skip", showlegend=False)
    )
    fig_circle.add_trace(
        go.Scatter(
            x=[results["x"]],
            y=[results["y"]],
            mode="markers",
            marker={"size": 12},
            showlegend=False,
            hovertemplate=t("circ_hover_pos"),
        )
    )
    fig_circle.update_layout(
        title=t("circ_path_title"),
        xaxis_title=t("circ_x_axis"),
        yaxis_title=t("circ_y_axis"),
        plot_bgcolor="white",
    )
    fig_circle.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
        scaleanchor="x",
        scaleratio=1,
    )

    # Plot 2: x(t) and y(t) sinusoids
    t_arr, x_series, y_series = circular_series(radius, angular_velocity, time_input)
    fig_sin = go.Figure()
    fig_sin.add_trace(go.Scatter(x=t_arr, y=x_series, mode="lines", name="x(t)"))
    fig_sin.add_trace(go.Scatter(x=t_arr, y=y_series, mode="lines", name="y(t)"))
    fig_sin.update_layout(
        title=t("circ_components_title"),
        xaxis_title=t("time_s"),
        yaxis_title=t("circ_pos_axis"),
        plot_bgcolor="white",
    )
    fig_sin.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )
    fig_sin.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="black",
    )

    c1, c2 = st.columns(2)
    c1.plotly_chart(fig_circle, width="stretch")
    c2.plotly_chart(fig_sin, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("circ_speed"), f"{results['linear_speed']:.2f} m/s")
    col2.metric(t("circ_period"), f"{results['period']:.2f} s")
    col3.metric(t("circ_frequency"), f"{results['frequency']:.2f} Hz")
    col4.metric(t("circ_centripetal"), f"{results['centripetal_acceleration']:.2f} m/s^2")
