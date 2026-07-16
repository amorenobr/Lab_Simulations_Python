import numpy as np
import pytest

from src.lab_simulations_python.projectile import calculate_kinematics


def test_projectile_kinematics():
    """
    Tests the kinematics calculation with a known scenario (45-degree launch).
    """
    # Inputs
    initial_velocity = 10.0  # m/s
    launch_angle = 45.0  # degrees

    # Expected results
    g = 9.81
    angle_rad = np.deg2rad(launch_angle)
    expected_t_flight = (2 * initial_velocity * np.sin(angle_rad)) / g
    expected_max_height = (initial_velocity**2 * np.sin(angle_rad) ** 2) / (2 * g)
    expected_range = (initial_velocity**2 * np.sin(2 * angle_rad)) / g

    # Get actual results from the function
    results = calculate_kinematics(initial_velocity, launch_angle)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["t_flight"] == pytest.approx(expected_t_flight)
    assert results["max_height"] == pytest.approx(expected_max_height)
    assert results["horizontal_range"] == pytest.approx(expected_range)
