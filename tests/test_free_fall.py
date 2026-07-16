import pytest

from src.lab_simulations_python.free_fall import calculate_free_fall


def test_free_fall():
    """
    Test the kinematics calculation with a known scenario.
    """
    # Inputs
    initial_position = 0.0  # m
    initial_velocity = 0.0  # m/s
    g = 9.81  # m/s^2
    time = 5.0  # s

    # Expected results
    expected_final_position = initial_position + (initial_velocity * time) - (0.5 * g * time**2)
    expected_final_velocity = initial_velocity - (g * time)

    # Get actual results from the function
    results = calculate_free_fall(initial_position, initial_velocity, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(expected_final_position)
    assert results["final_velocity"] == pytest.approx(expected_final_velocity)
