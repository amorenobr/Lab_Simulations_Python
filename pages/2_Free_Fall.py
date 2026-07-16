import numpy as np
import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.free_fall import calculate_free_fall
from src.lab_simulations_python.i18n import language_selector, t

st.set_page_config(layout="wide")

language_selector()

st.title(t("ff_title"))
st.markdown(t("ff_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
position_input = st.sidebar.slider(t("ff_position"), 0.0, 100.0, 20.0)
velocity_input = st.sidebar.slider(t("ff_velocity"), 0.0, 100.0, 20.0)
time_input = st.sidebar.slider(t("time_s"), 0.0, 100.0, 10.0)

st.write(t("ff_current_params").format(p=position_input, v=velocity_input, tm=time_input))

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    kinematics = calculate_free_fall(position_input, velocity_input, time_input)

    # Plotting
    st.subheader(t("plots"))

    g = 9.81
    t_arr = np.linspace(0, time_input, num=500)
    x = position_input + (velocity_input * t_arr) - (0.5 * g * t_arr**2)
    v = velocity_input - (g * t_arr)

    # Position vs Time
    fig_x = go.Figure(go.Scatter(x=t_arr, y=x, mode="lines", hovertemplate=t("ff_hover_position")))

    fig_x.update_layout(
        title=t("ff_pos_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("ff_position_axis"),
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

    # Velocity vs Time
    fig_v = go.Figure(go.Scatter(x=t_arr, y=v, mode="lines", hovertemplate=t("ff_hover_velocity")))

    fig_v.update_layout(
        title=t("ff_vel_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("ff_velocity_axis"),
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

    # Render both plots side by side
    c1, c2 = st.columns(2)
    c1.plotly_chart(fig_x, width="stretch")
    c2.plotly_chart(fig_v, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2 = st.columns(2)
    col1.metric(t("ff_final_position"), f"{kinematics['final_position']:.2f} m")
    col2.metric(t("ff_final_velocity"), f"{kinematics['final_velocity']:.2f} m/s")
