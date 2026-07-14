import streamlit as st
import numpy as np
import plotly.graph_objects as go
from src.lab_simulations_python.projectile import calculate_kinematics
from src.lab_simulations_python.i18n import t, language_selector

st.set_page_config(layout="wide")

language_selector()

st.title(t("pj_title"))
st.markdown(t("pj_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
velocity_input = st.sidebar.slider(t("pj_velocity"), 1.0, 100.0, 25.0)
angle_input = st.sidebar.slider(t("pj_angle"), 0, 90, 45)

st.write(t("pj_current_params").format(v=velocity_input, a=angle_input))

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    kinematics = calculate_kinematics(velocity_input, angle_input)
    t_flight = kinematics["t_flight"]

    # Trajectory plotting
    st.subheader(t("pj_trajectory_plot"))

    angle_rad = np.deg2rad(angle_input)
    g = 9.81
    t_arr = np.linspace(0, t_flight, num=500)
    x = velocity_input * np.cos(angle_rad) * t_arr
    y = velocity_input * np.sin(angle_rad) * t_arr - 0.5 * g * t_arr**2

    fig = go.Figure(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                hovertemplate=t("pj_hover"))
            )

    fig.update_layout(
            title=t("pj_traj_title"),
            xaxis_title=t("pj_range_axis"),
            yaxis_title=t("pj_height_axis"),
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
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3 = st.columns(3)
    col1.metric(t("pj_time_of_flight"), f"{kinematics['t_flight']:.2f} s")
    col2.metric(t("pj_max_height"), f"{kinematics['max_height']:.2f} m")
    col3.metric(t("pj_horizontal_range"), f"{kinematics['horizontal_range']:.2f} m")
