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

    # Get actual results from the function
    results = calculate_linear_motion(initial_position, initial_velocity, acceleration, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(25.0)  # m
    assert results["final_velocity"] == pytest.approx(5.0)  # m/s


def test_linear_motion_with_acceleration():
    """
    Test the kinematics calculation with a known scenario (acceleration=3.0).
    """
    # Inputs
    initial_position = 0.0  # m
    initial_velocity = 0.0  # m/s
    acceleration = 3.0  # m/s^2
    time = 5.0  # s

    # Get actual results from the function
    results = calculate_linear_motion(initial_position, initial_velocity, acceleration, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(37.5)  # m
    assert results["final_velocity"] == pytest.approx(15.0)  # m/s


def test_linear_motion_stops_at_turning_point():
    """
    Test the kinematics calculation with an object decelerating to a stop.
    """
    # Inputs
    initial_position = 0.0  # m
    initial_velocity = 10.0  # m/s
    acceleration = -2.0  # m/s^2
    time = 5.0  # s

    # Get actual results from the function
    results = calculate_linear_motion(initial_position, initial_velocity, acceleration, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(25.0)  # m
    assert results["final_velocity"] == pytest.approx(0.0, abs=1e-9)  # m/s


def test_linear_motion_returns_to_start():
    """
    Test the kinematics calculation with an object returning to its start.
    """
    # Inputs
    initial_position = 0.0  # m
    initial_velocity = 10.0  # m/s
    acceleration = -2.0  # m/s^2
    time = 10.0  # s

    # Get actual results from the function
    results = calculate_linear_motion(initial_position, initial_velocity, acceleration, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(0.0, abs=1e-9)  # m
    assert results["final_velocity"] == pytest.approx(-10.0)  # m/s
