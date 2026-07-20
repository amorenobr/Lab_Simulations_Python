import numpy as np
import pytest

from src.lab_simulations_python.work_energy import calculate_work_energy, energy_series


def test_work_energy_at_start():
    """At t = 0, energies match the initial conditions."""
    mass, h0, v0 = 2.0, 10.0, 0.0
    g = 9.81
    results = calculate_work_energy(mass, h0, v0, time=0.0)
    assert results["kinetic_energy"] == pytest.approx(0.5 * mass * v0**2)  # 0
    assert results["potential_energy"] == pytest.approx(mass * g * h0)  # 196.2
    assert results["total_energy"] == pytest.approx(mass * g * h0)


def test_energy_is_conserved():
    """Total mechanical energy stays constant over time."""
    mass, h0, v0 = 1.5, 20.0, 5.0
    t_arr, ke, pe, total = energy_series(mass, h0, v0, time=3.0)
    initial_total = 0.5 * mass * v0**2 + mass * 9.81 * h0
    assert len(t_arr) == 500
    assert np.allclose(total, initial_total)
    assert np.allclose(ke + pe, total)


def test_energy_conversion():
    """Dropped from rest: PE converts to KE (KE rises, PE falls)."""
    _, ke, pe, _ = energy_series(mass=1.0, initial_height=50.0, initial_velocity=0.0, time=2.0)
    assert ke[-1] > ke[0]  # kinetic energy grows
    assert pe[-1] < pe[0]  # potential energy drops
