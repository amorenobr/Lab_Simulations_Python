import pytest

from src.lab_simulations_python.free_fall import calculate_free_fall


def test_free_fall_at_apex():
    """
    Test the kinematics calculation with a known scenario with an object going to the top
    of its flight.
    """
    # Inputs
    initial_position = 20.0  # m
    initial_velocity = 20.0  # m/s
    time = 2.0  # s

    # Get actual results from the function
    results = calculate_free_fall(initial_position, initial_velocity, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(40.38, abs=5e-3)  # m
    assert results["final_velocity"] == pytest.approx(0.38)  # m/s


def test_free_fall_after_apex():
    """
    Test the kinematics calculation with a known scenario with an object falling, and
    velocity negative.
    """
    # Inputs
    initial_position = 20.0  # m
    initial_velocity = 20.0  # m/s
    time = 4.0  # s

    # Get actual results from the function
    results = calculate_free_fall(initial_position, initial_velocity, time)

    # Assert that the actual results are approximately equal to the expected ones
    assert results["final_position"] == pytest.approx(21.52)  # m
    assert results["final_velocity"] == pytest.approx(-19.24)  # m/s
