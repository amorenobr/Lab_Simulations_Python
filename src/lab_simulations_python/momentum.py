from typing import Dict

import numpy as np


def _final_velocities(m1: float, u1: float, m2: float, u2: float, collision_type: str):
    """Final velocities of the two objects after a 1D collision."""
    if collision_type == "inelastic":
        v = (m1 * u1 + m2 * u2) / (m1 + m2)  # sitck together
        return v, v
    # elastic collision
    v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)
    v2 = ((m2 - m1) * u2 + 2 * m1 * u1) / (m1 + m2)
    return v1, v2


def calculate_momentum(
    m1: float, u1: float, m2: float, u2: float, collision_type: str = "elastic"
) -> Dict[str, float]:
    """
    Calculates the outcome of a one dimensional collision between two objects.

    Args:
        m1: The mass of object 1 in kg
        u1: The initial velocity of object 1 in m/s
        m2: The mass of object 2 in kg
        u2: The initial velocity of object 2 in m/s
        collision_type: Either "elastic" or "inelastic"

    Returns:
        A dictionary containing the final velocities, the total momentum before and after, and the total kinetic
        energy before and after
    """

    v1, v2 = _final_velocities(m1, u1, m2, u2, collision_type)

    momentum_before = m1 * u1 + m2 * u2
    momentum_after = m1 * v1 + m2 * v2
    kinetic_energy_before = 0.5 * m1 * u1**2 + 0.5 * m2 * u2**2
    kinetic_energy_after = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2

    return {
        "final_velocity_1": v1,
        "final_velocity_2": v2,
        "momentum_before": momentum_before,
        "momentum_after": momentum_after,
        "kinetic_energy_before": kinetic_energy_before,
        "kinetic_energy_after": kinetic_energy_after,
    }


def collision_series(
    m1: float,
    u1: float,
    m2: float,
    u2: float,
    collision_type: str = "elastic",
    time: float = 5.0,
    n: int = 500,
    separation: float = 10.0,
):
    """
    Positions x1(t) and x2(t) of the two objetcs, which collide once if they approach. Object 1 starts at 0, object 2
    starts at `separation` ahead of it.

    Returns:
        A tuple (t_arr, x1, x2) of NumPy arrays.
    """

    v1, v2 = _final_velocities(m1, u1, m2, u2, collision_type)
    t_arr = np.linspace(0, time, num=n)

    # They meet when u1*t = separation + u2*t -> t_c = separation / (u1 - u2), only if u1 > u2
    t_c = separation / (u1 - u2) if u1 > u2 else time + 1.0  # else: no collision
    x_c = separation + u2 * t_c  # collision position

    before = t_arr < t_c
    x1 = np.where(before, u1 * t_arr, x_c + v1 * (t_arr - t_c))
    x2 = np.where(before, separation + u2 * t_arr, x_c + v2 * (t_arr - t_c))
    return t_arr, x1, x2
