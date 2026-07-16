import pytest

from src.lab_simulations_python.linear_motion import calculate_linear_motion


def test_linear_motion():
    """
    Test the kinematics calculation with a known scenario (acceleration=0.0).
    """
    # Inputs
    initial_position = 0.0  # m
    initial_velocity = 5.0  # m/s
    acceleration = 0.0  # m/s^2
    time = 5.0  # s

    # Expected results
    expected_final_position = (
        initial_position + (initial_velocity * time) + (0.5 * acceleration * time**2)
    )
    expected_final_velocity = initial_velocity + (acceleration * time)

    # Get actual results from the function
    results = calculate_linear_motion(initial_position, initial_velocity, acceleration, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(expected_final_position)
    assert results["final_velocity"] == pytest.approx(expected_final_velocity)


def test_linear_motion_with_acceleration():
    """
    Test the kinematics calculation with a known scenario (acceleration=3.0).
    """
    # Inputs
    initial_position = 0.0  # m
    initial_velocity = 0.0  # m/s
    acceleration = 3.0  # m/s^2
    time = 5.0  # s

    # Expected results
    expected_final_position = (
        initial_position + (initial_velocity * time) + (0.5 * acceleration * time**2)
    )
    expected_final_velocity = initial_velocity + (acceleration * time)

    # Get actual results from the function
    results = calculate_linear_motion(initial_position, initial_velocity, acceleration, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(expected_final_position)
    assert results["final_velocity"] == pytest.approx(expected_final_velocity)
