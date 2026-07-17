import numpy as np
import pytest

from src.lab_simulations_python.circular_motion import calculate_circular_motion, circular_series


def test_circular_motion():
    """Unifrom circular motion with a known scenario (t=0)."""
    radius = 2.0
    angular_velocity = 3.0

    results = calculate_circular_motion(radius, angular_velocity, time=0.0)

    assert results["linear_speed"] == pytest.approx(angular_velocity * radius)  # 6.0
    assert results["period"] == pytest.approx(2 * np.pi / angular_velocity)
    assert results["frequency"] == pytest.approx(angular_velocity / (2 * np.pi))
    assert results["centripetal_acceleration"] == pytest.approx(
        angular_velocity**2 * radius
    )  # 18.0
    # at t=0 the particle sits at (r, 0)
    assert results["x"] == pytest.approx(radius)
    assert results["y"] == pytest.approx(0.0)


def test_circular_series():
    """The position arrays starts at (r, 0) and never leave the circle."""
    radius = 1.5
    t_arr, x, y = circular_series(radius, angular_velocity=2.0, time=5.0)

    assert len(t_arr) == 500
    assert x[0] == pytest.approx(radius)
    assert y[0] == pytest.approx(0.0)
    # radius is constant: x^2 + y^2 == r^2 everywhere
    assert np.allclose(x**2 + y**2, radius**2)
