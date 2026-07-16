import numpy as np
import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.i18n import language_selector, t
from src.lab_simulations_python.linear_motion import calculate_linear_motion

st.set_page_config(layout="wide")

language_selector()

st.title(t("lm_title"))
st.markdown(t("lm_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
position_input = st.sidebar.slider(t("lm_position"), 0.0, 100.0, 20.0)
velocity_input = st.sidebar.slider(t("lm_velocity"), 0.0, 100.0, 20.0)
acceleration_input = st.sidebar.slider(t("lm_acceleration"), 0.0, 30.0, 5.0)
time_input = st.sidebar.slider(t("time_s"), 0.0, 100.0, 10.0)

st.write(
    t("lm_current_params").format(
        p=position_input, v=velocity_input, a=acceleration_input, tm=time_input
    )
)

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    kinematics = calculate_linear_motion(
        position_input, velocity_input, acceleration_input, time_input
    )

    # Plotting
    st.subheader(t("plots"))

    t_arr = np.linspace(0, time_input, num=500)
    x = position_input + (velocity_input * t_arr) + (0.5 * acceleration_input * t_arr**2)
    v = velocity_input + (acceleration_input * t_arr)

    # Position vs Time
    fig_x = go.Figure(go.Scatter(x=t_arr, y=x, mode="lines", hovertemplate=t("lm_hover_position")))

    fig_x.update_layout(
        title=t("lm_pos_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("lm_position_axis"),
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
    fig_v = go.Figure(go.Scatter(x=t_arr, y=v, mode="lines", hovertemplate=t("lm_hover_velocity")))

    fig_v.update_layout(
        title=t("lm_vel_vs_time"),
        xaxis_title=t("time_s"),
        yaxis_title=t("lm_velocity_axis"),
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
    col1.metric(t("lm_final_position"), f"{kinematics['final_position']:.2f} m")
    col2.metric(t("lm_final_velocity"), f"{kinematics['final_velocity']:.2f} m/s")
