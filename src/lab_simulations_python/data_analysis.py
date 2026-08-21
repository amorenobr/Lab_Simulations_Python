from typing import Dict

import numpy as np

from .oscillations import calculate_oscillation, displacement
from .projectile import calculate_kinematics

gravity = 9.81  # m/s^2


def linear_fit(x: np.ndarray, y: np.ndarray) -> Dict[str, float]:
    """
    Ordinary least-squares fit of a straight line y = m x + b, the line minimizing the sum of the squared residuals.

    Args:
        x: The independent variable
        y: The measured dependent variable

    Returns:
        A dictionary with the slope and intercept, their standard errors, and the coefficient of determination R^2.
    """
    n = len(x)
    x_mean, y_mean = float(np.mean(x)), float(np.mean(y))

    sxx = float(np.sum((x - x_mean) ** 2))
    sxy = float(np.sum((x - x_mean) * (y - y_mean)))

    slope = sxy / sxx
    intercept = y_mean - slope * x_mean

    residual = y - (slope * x + intercept)
    sum_squared_residual = float(np.sum(residual**2))
    residual_variance = sum_squared_residual / (n - 2)

    slope_error = float(np.sqrt(residual_variance / sxx))
    intercept_error = float(np.sqrt(residual_variance * (1 / n + x_mean**2 / sxx)))

    total_variation = float(np.sum((y - y_mean) ** 2))

    return {
        "slope": slope,
        "intercept": intercept,
        "slope_error": slope_error,
        "intercept_error": intercept_error,
        "r_squared": 1 - sum_squared_residual / total_variation,
    }


def fit_residuals(x: np.ndarray, y: np.ndarray, slope: float, intercept: float):
    """
    Difference between the measurements and the fitted line, y - (m x + b).

    A good fit leaves residuals scattered randomly about zero, a visible pattern means the model itself is wrong,
    not merely noisy.

    Returns:
        A NumPy array of residuals, in the units of y.
    """
    return y - (slope * x + intercept)


def measure_free_fall(
    gravity: float, noise: float, n_points: int, max_time: float = 2.0, seed: int = 42
):
    """
    Simulated free fall experiment: an object dropped from rest falls d = g t^2 / 2, and the distance is measured
    at evenly spaced time with random error.

    The data is returned already linearized, as t^2 against distance, so a straight line fit applies.

    Args:
        gravity: The true gravitational acceleration in m/s^2
        noise: The standard deviation of the measurement noise in m
        n_points: The number of measurements taken
        max_time: The time of the last measurement in s
        seed: Seed for the random number generator, so a run can be reproduced

    Returns:
        A tuple (time_squared, measured_distance) of NumPy arrays, in s^2 and m
    """
    rng = np.random.default_rng(seed)
    time = np.linspace(max_time / n_points, max_time, n_points)
    measured_distance = 0.5 * gravity * time**2 + rng.normal(0.0, noise, n_points)
    return time**2, measured_distance


def fit_free_fall(time_squared: np.ndarray, measured_distance: np.ndarray) -> Dict[str, float]:
    """
    Recovers gravity from free fall data: d = (g/2) t^2 is a line in t^2 of slope g/2, so g = 2m and its uncertainty
    is twice the slope error.

    Returns:
        A dictionary with the recovered value and error, plus the underlying fit.
    """
    fit = linear_fit(time_squared, measured_distance)
    return {"value": 2 * fit["slope"], "error": 2 * fit["slope_error"], **fit}


def measure_oscillator(
    mass: float,
    spring_constant: float,
    damping_coefficient: float,
    noise: float,
    n_points: int,
    amplitude: float = 1.0,
    seed: int = 42,
):
    """
    Simulated decay experiment. The amplitude of a damped oscillator is measured at successive peaks, one
    damped period apart.

    The envelope A(t) = A0 exp(-gamma t) is linearized by taking logarithms, so the data is returned as time
    against ln(amplitude), a straight line of slope -gamma.

    Args:
        mass: Mass on the spring in kg
        spring_constant: Spring constant k in N/m
        damping_coefficient: The true damping coefficient b in kg/s
        noise: The standard deviation of the amplitude measurement noise in m
        n_points: The number of peaks measured
        amplitude: The initial amplitude in m
        seed: Seed for the random number generator, so a run can be reproduced

    Returns:
        A tuple (peak_time, log_amplitude) of NumPy arrays, in s and dimensionless
    """
    rng = np.random.default_rng(seed)

    gamma = damping_coefficient / (2 * mass)
    omega_0 = calculate_oscillation(mass, spring_constant)["omega_0"]
    damped_period = 2 * np.pi / np.sqrt(omega_0**2 - gamma**2)

    peak_time = np.arange(n_points) * damped_period
    true_amplitude = displacement(peak_time, mass, spring_constant, amplitude, damping_coefficient)
    peak_amplitude = true_amplitude + rng.normal(0.0, noise, n_points)

    return peak_time, np.log(np.maximum(peak_amplitude, 1e-6))


def fit_oscillator(
    peak_time: np.ndarray, log_amplitude: np.ndarray, mass: float
) -> Dict[str, float]:
    """
    Recovers the damping coefficient from a decay curve: ln A is a line in t of slope -gamma, and b = 2 m gamma,
    so b = -2 m and its uncertainty is twice the mass times the slope error.

    Returns:
        A dictionary with the recovered value and error, plus the underlying fit.
    """
    fit = linear_fit(peak_time, log_amplitude)
    return {"value": -2 * mass * fit["slope"], "error": 2 * mass * fit["slope_error"], **fit}


def measure_projectile(initial_velocity: float, noise: float, n_points: int, seed: int = 42):
    """
    Simulated range experiment. A projectile is launched at the same speed over a spread of angles and the
    horizontal range is measured with random error.

    The relation R = v0^2 sin(2 theta) / g is linearized by plotting R against sin(2 theta), a straight line
    through the origin of slope v0^2 / g.

    Args:
        initial_velocity: The true launch speed in m/s
        noise: The standard deviation of the range measurement noise in m
        n_points: The number of launch angles tried
        seed: Seed for the random number generator, so a run can be reproduced

    Returns:
        A tuple (sin_two_theta, measured_range) of NumPy arrays, dimensionless and m
    """
    rng = np.random.default_rng(seed)

    angle = np.linspace(10.0, 80.0, n_points)
    true_range = np.array(
        [calculate_kinematics(initial_velocity, a)["horizontal_range"] for a in angle]
    )
    measured_range = true_range + rng.normal(0.0, noise, n_points)

    return np.sin(2 * np.deg2rad(angle)), measured_range


def fit_projectile(
    sin_two_theta: np.ndarray, measured_range: np.ndarray, gravity: float = gravity
) -> Dict[str, float]:
    """
    Recovers the launch speed from range data. R is a line in sin(2 theta) of slope v0^2 / g, so v0 = sqrt(g m)
    and, propagating the slope error, its uncertainty is v0 dm / (2 m).

    Returns:
        A dictionary with the recovered value and error, plus the underlying fit.
    """
    fit = linear_fit(sin_two_theta, measured_range)

    velocity = float(np.sqrt(gravity * abs(fit["slope"])))
    velocity_error = velocity * fit["slope_error"] / (2 * abs(fit["slope"]))

    return {"value": velocity, "error": velocity_error, **fit}
