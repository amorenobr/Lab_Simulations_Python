import numpy as np
import plotly.graph_objects as go
import streamlit as st

from src.lab_simulations_python.data_analysis import (
    fit_free_fall,
    fit_oscillator,
    fit_projectile,
    fit_residuals,
    measure_free_fall,
    measure_oscillator,
    measure_projectile,
)
from src.lab_simulations_python.i18n import language_selector, t

st.set_page_config(layout="wide")

language_selector()

st.title(t("da_title"))
st.markdown(t("da_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
experiment = st.sidebar.radio(
    t("da_experiment"),
    ("free_fall", "oscillator", "projectile"),
    format_func=lambda key: t(f"da_exp_{key}"),
)
seed = int(st.sidebar.number_input(t("da_seed"), min_value=0, max_value=9999, value=42, step=1))

if experiment == "free_fall":
    true_value = st.sidebar.slider(t("da_true_gravity"), 1.0, 25.0, 9.81, step=0.01)
    noise = st.sidebar.slider(t("da_noise_dist"), 0.0, 1.0, 0.10, step=0.01)
    n_points = st.sidebar.slider(t("da_n_points"), 5, 60, 20)

    x, y = measure_free_fall(true_value, noise, n_points, seed=seed)
    result = fit_free_fall(x, y)
    quantity, unit = t("da_q_gravity"), "m/s^2"
    x_title, y_title = t("da_ff_x"), t("da_ff_y")

elif experiment == "oscillator":
    mass = st.sidebar.slider(t("osc_mass"), 0.1, 10.0, 1.0)
    spring_constant = st.sidebar.slider(t("osc_spring"), 1.0, 100.0, 20.0)
    true_value = st.sidebar.slider(t("da_true_damping"), 0.1, 0.8, 0.40, step=0.05)
    amplitude = st.sidebar.slider(t("da_amplitude"), 0.5, 5.0, 2.0, step=0.1)
    noise = st.sidebar.slider(t("da_noise_amp"), 0.0, 0.02, 0.005, step=0.001)
    n_points = st.sidebar.slider(t("da_n_peaks"), 4, 10, 8)

    x, y = measure_oscillator(
        mass, spring_constant, true_value, noise, n_points, amplitude=amplitude, seed=seed
    )
    result = fit_oscillator(x, y, mass)
    quantity, unit = t("da_q_damping"), "kg/s"
    x_title, y_title = t("da_osc_x"), t("da_osc_y")

else:
    true_value = st.sidebar.slider(t("da_true_velocity"), 5.0, 50.0, 20.0, step=0.5)
    noise = st.sidebar.slider(t("da_noise_range"), 0.0, 5.0, 1.0, step=0.1)
    n_points = st.sidebar.slider(t("da_n_angles"), 5, 40, 15)

    x, y = measure_projectile(true_value, noise, n_points, seed=seed)
    result = fit_projectile(x, y)
    quantity, unit = t("da_q_velocity"), "m/s"
    x_title, y_title = t("da_proj_x"), t("da_proj_y")

st.write(t("da_current_params").format(q=quantity, v=true_value, u=unit, n=n_points))

# Main Simulation
if st.button(t("run_simulation")):
    fitted_line = result["slope"] * x + result["intercept"]
    residual = fit_residuals(x, y, result["slope"], result["intercept"])

    # The log of a clamped amplitude means the signal has fallen below the noise
    if experiment == "oscillator" and bool(np.any(y <= np.log(1e-6) + 1e-9)):
        st.warning(t("da_noise_floor"))

    # Plotting
    st.subheader(t("da_data_and_fit"))

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name=t("da_measured"),
            marker={"size": 9, "color": "#1f77b4"},
            hovertemplate=t("da_hover"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=fitted_line,
            mode="lines",
            name=t("da_fit_line"),
            line={"color": "black", "width": 2},
            hovertemplate=t("da_hover"),
        )
    )
    fig.update_layout(
        title=t("da_plot_title"),
        xaxis_title=x_title,
        yaxis_title=y_title,
        plot_bgcolor="white",
    )
    fig.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=False,
    )
    fig.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=False,
    )
    st.plotly_chart(fig, witdh="stretch")

    st.subheader(t("da_residual_plot"))

    fig_residual = go.Figure()
    fig_residual.add_trace(
        go.Scatter(
            x=x,
            y=residual,
            mode="markers",
            name=t("da_residuals"),
            marker={"size": 9, "color": "#1f77b4"},
            hovertemplate=t("da_residual_hover"),
        )
    )
    fig_residual.add_hline(y=0.0, line_width=2, line_color="black")
    fig_residual.update_layout(
        title=t("da_residual_title"),
        xaxis_title=x_title,
        yaxis_title=t("da_residuals"),
        plot_bgcolor="white",
    )
    fig_residual.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=False,
    )
    fig_residual.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=False,
    )
    st.plotly_chart(fig_residual, witdh="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("da_complete").format(q=quantity))

    deviation = abs(result["value"] - true_value) / result["error"] if result["error"] > 0 else 0.0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(
        t("da_recovered"),
        f"{result['value']:.3f} {unit}",
        delta=f"±{result['error']:.3f}",
        delta_color="off",
    )
    col2.metric(t("da_true"), f"{true_value:.3f} {unit}")
    col3.metric(t("da_deviation"), f"{deviation:.1f} σ")
    col4.metric(t("da_r_squared"), f"{result['r_squared']:.4f}")
