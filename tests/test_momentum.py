import pytest

from src.lab_simulations_python.momentum import calculate_momentum, collision_series


def test_momentum_conserved_elastic():
    """Elastic collision: both momentum and kinetic energy are conserved."""
    r = calculate_momentum(m1=2.0, u1=3.0, m2=1.0, u2=1.0, collision_type="elastic")
    assert r["momentum_after"] == pytest.approx(r["momentum_before"])
    assert r["kinetic_energy_after"] == pytest.approx(r["kinetic_energy_before"])


def test_momentum_conserved_inelastic():
    """Inelastic collision: momentum conserved, objects share a velocity, KE is lost."""
    r = calculate_momentum(m1=2.0, u1=3.0, m2=1.0, u2=1.0, collision_type="inelastic")
    assert r["momentum_after"] == pytest.approx(r["momentum_before"])
    assert r["final_velocity_1"] == pytest.approx(r["final_velocity_2"])  # stick together
    assert r["kinetic_energy_after"] < r["kinetic_energy_before"]  # energy lost


def test_equal_mass_elastic_swaps_velocities():
    """Classic result: equal masses in an elastic collision exchange velocities."""
    r = calculate_momentum(m1=1.0, u1=4.0, m2=1.0, u2=0.0, collision_type="elastic")
    assert r["final_velocity_1"] == pytest.approx(0.0)
    assert r["final_velocity_2"] == pytest.approx(4.0)


def test_collision_series_shape_and_start():
    t_arr, x1, x2 = collision_series(
        m1=2.0, u1=3.0, m2=1.0, u2=-1.0, collision_type="elastic", time=5.0
    )
    assert len(t_arr) == len(x1) == len(x2) == 500
    assert x1[0] == pytest.approx(0.0)  # object 1 starts at position o
