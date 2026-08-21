import numpy as np
import pytest

from src.lab_simulations_python.data_analysis import (
    fit_free_fall,
    fit_oscillator,
    fit_projectile,
    fit_residuals,
    linear_fit,
    measure_free_fall,
    measure_oscillator,
    measure_projectile,
)


def test_perfect_line_is_recovered_exactly():
    x = np.linspace(0.0, 10.0, 25)
    y = 3.0 * x + 2.0

    fit = linear_fit(x, y)

    assert fit["slope"] == pytest.approx(3.0, rel=1e-9)
    assert fit["intercept"] == pytest.approx(2.0, abs=1e-9)
    assert fit["r_squared"] == pytest.approx(1.0, abs=1e-12)
    assert fit["slope_error"] == pytest.approx(0.0, abs=1e-9)


def test_residuals_sum_to_zero():
    x = np.linspace(0.0, 5.0, 30)
    rng = np.random.default_rng(7)
    y = 1.5 * x - 0.5 + rng.normal(0.0, 0.3, 30)

    fit = linear_fit(x, y)
    residual = fit_residuals(x, y, fit["slope"], fit["intercept"])

    assert float(np.sum(residual)) == pytest.approx(0.0, abs=1e-9)


def test_noiseless_free_fall_recovers_gravity():
    x, y = measure_free_fall(gravity=9.81, noise=0.0, n_points=20)
    result = fit_free_fall(x, y)

    assert result["value"] == pytest.approx(9.81, rel=1e-9)
    assert result["r_squared"] == pytest.approx(1.0, abs=1e-12)


@pytest.mark.parametrize("gravity", [1.62, 3.71, 24.79])
def test_free_fall_works_for_other_gravities(gravity):
    x, y = measure_free_fall(gravity=gravity, noise=0.0, n_points=15)

    assert fit_free_fall(x, y)["value"] == pytest.approx(gravity, rel=1e-9)


def test_noisy_free_fall_agrees_within_uncertainty():
    x, y = measure_free_fall(gravity=9.81, noise=0.05, n_points=25)
    result = fit_free_fall(x, y)

    assert abs(result["value"] - 9.81) < 3 * result["error"]
    assert result["error"] > 0.0


def test_more_noise_gives_larger_uncertainty():
    quiet = fit_free_fall(*measure_free_fall(gravity=9.81, noise=0.02, n_points=20))
    loud = fit_free_fall(*measure_free_fall(gravity=9.81, noise=0.20, n_points=20))

    assert loud["error"] > quiet["error"]


def test_more_points_gives_smaller_uncertainty():
    few = fit_free_fall(*measure_free_fall(gravity=9.81, noise=0.05, n_points=10))
    many = fit_free_fall(*measure_free_fall(gravity=9.81, noise=0.05, n_points=80))

    assert many["error"] < few["error"]


def test_noiseless_oscillator_recovers_damping():
    time, log_amplitude = measure_oscillator(
        mass=1.0, spring_constant=10.0, damping_coefficient=0.4, noise=0.0, n_points=8
    )
    result = fit_oscillator(time, log_amplitude, mass=1.0)

    assert result["value"] == pytest.approx(0.4, rel=1e-6)
    assert result["r_squared"] == pytest.approx(1.0, abs=1e-9)


def test_stronger_damping_decays_faster():
    weak = fit_oscillator(
        *measure_oscillator(
            mass=1.0, spring_constant=10.0, damping_coefficient=0.2, noise=0.0, n_points=8
        ),
        mass=1.0,
    )
    strong = fit_oscillator(
        *measure_oscillator(
            mass=1.0, spring_constant=10.0, damping_coefficient=0.8, noise=0.0, n_points=8
        ),
        mass=1.0,
    )

    assert strong["slope"] < weak["slope"] < 0.0
    assert strong["value"] > weak["value"]


def test_noiseless_projectile_recovers_launch_speed():
    x, y = measure_projectile(initial_velocity=20.0, noise=0.0, n_points=15)
    result = fit_projectile(x, y)

    assert result["value"] == pytest.approx(20.0, rel=1e-6)
    assert result["r_squared"] == pytest.approx(1.0, abs=1e-9)


def test_projectile_line_passes_through_origin():
    x, y = measure_projectile(initial_velocity=25.0, noise=0.0, n_points=12)

    assert fit_projectile(x, y)["intercept"] == pytest.approx(0.0, abs=1e-8)


def test_seed_makes_runs_reproducible():
    first = measure_free_fall(gravity=9.81, noise=0.1, n_points=20, seed=1)
    same = measure_free_fall(gravity=9.81, noise=0.1, n_points=20, seed=1)
    other = measure_free_fall(gravity=9.81, noise=0.1, n_points=20, seed=2)

    assert np.allclose(first[1], same[1])
    assert not np.allclose(first[1], other[1])
