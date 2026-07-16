import numpy as np

from src.lab_simulations_python.oscillations import calculate_oscillation, displacement


def test_undamped_period():
    """Undamped period should be 2*pi*sqrt(m/K)"""
    props = calculate_oscillation(mass=1.0, spring_constant=4.0, damping_coefficient=0.0)
    assert props["period"] == np.pi
    assert props["regime"] == "undamped"


def test_displacement_starts_at_amplitude():
    """At t=0 the mass is released from rest at x = amplitude"""
    x0 = displacement(np.array([0, 0]), mass=1.0, spring_constant=20.0, amplitude=2.0)
    assert x0[0] == 2.0


def test_dampig_regimes():
    assert calculate_oscillation(1.0, 20.0, 0.5)["regime"] == "underdamped"
    # critical damping: b = 2 * sqrt(k * m)
    b_crit = 2 * np.sqrt(20.0 * 1.0)
    assert calculate_oscillation(1.0, 20.0, b_crit)["regime"] == "critically damped"
    assert calculate_oscillation(1.0, 20.0, b_crit + 5)["regime"] == "overdamped"
