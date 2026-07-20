import pytest

from src.lab_simulations_python.newtons_laws import calculate_newtons_laws, newton_series


def test_newtons_laws_with_friction():
    """Block pushed with enough force to overcome friction."""
    mass, applied_force, mu, time = 2.0, 20.0, 0.5, 3.0
    g = 9.81

    results = calculate_newtons_laws(mass, applied_force, mu, time)

    friction = mu * mass * g  # g = 9.81 N
    net = applied_force - friction  # 10.19 N
    a = net / mass  # 5.095 m/s^2
    assert results["friction_force"] == pytest.approx(friction)
    assert results["net_force"] == pytest.approx(net)
    assert results["acceleration"] == pytest.approx(a)
    assert results["final_velocity"] == pytest.approx(a * time)
    assert results["final_position"] == pytest.approx(0.5 * a * time**2)


def test_newtons_laws_below_friction_stays_at_rest():
    """If the applied force can't overcome friction, the block doesn't move."""
    # friction = 0.5 * 2 * 9.81 = 9.81 N; applied force = 5 N is less than that

    results = calculate_newtons_laws(
        mass=2.0, applied_force=5.0, friction_coefficient=0.5, time=4.0
    )
    assert results["net_force"] == pytest.approx(0.0)
    assert results["acceleration"] == pytest.approx(0.0)
    assert results["final_velocity"] == pytest.approx(0.0)
    assert results["final_position"] == pytest.approx(0.0)


def test_newton_series_from_rest():
    """v(t) and x(t) start at zero; frictionless case gives a = F/m."""

    t_arr, v, x = newton_series(mass=1.0, applied_force=10.0, friction_coefficient=0.0, time=5.0)
    assert len(t_arr) == 500
    assert v[0] == pytest.approx(0.0)
    assert x[0] == pytest.approx(0.0)
    assert v[-1] == pytest.approx(10.0 * 5.0)  # a = 10, at t = 5 -> v = 50
