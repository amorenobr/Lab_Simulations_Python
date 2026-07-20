from typing import Dict

import numpy as np

g = 9.81  # gravitational acceleration in m/s^2


def calculate_newtons_laws(
    mass: float, applied_force: float, friction_coefficient: float, time: float = 0.0
) -> Dict[str, float]:
    """
    Calculates the dynamics of a block pushed from rest along a flat surface by an
    applied force, opposed by kinetic friction (Newton's second law).

    Args:
        mass: The mass of the block in kg
        applied_force: The applied horizontal force in N
        friction_coefficient: The coefficient of kinetic friction (dimensionless)
        time: The elapsed time in s

    Returns:
        A dictionary containing the friction force, net force, acceleration,
        and the final velocity and position at the given time
    """

    friction_force = friction_coefficient * mass * g
    net_force = max(applied_force - friction_force, 0.0)  # no motion if force can't beat friction
    acceleration = net_force / mass

    final_velocity = acceleration * time
    final_position = 0.5 * acceleration * time**2

    return {
        "friction_force": friction_force,
        "net_force": net_force,
        "acceleration": acceleration,
        "final_velocity": final_velocity,
        "final_position": final_position,
    }


def newton_series(
    mass: float, applied_force: float, friction_coefficient: float, time: float, n: int = 500
):
    """
    Velocity v(t) and position x(t) of the block over [0, time], starting from rest.

    Args:
        mass: The mass of the block in kg
        applied_force: The applied horizontal force in N
        friction_coefficient: The coefficient of kinetic friction (dimensionless)
        time: The total elapsed time in s
        n: The number of samples

    Returns:
        A tuple (t_arr, v, x) of NumPy arrays.
    """

    friction_force = friction_coefficient * mass * g
    net_force = max(applied_force - friction_force, 0.0)  # no motion if force can't beat friction
    acceleration = net_force / mass

    t_arr = np.linspace(0, time, num=n)
    v = acceleration * t_arr
    x = 0.5 * acceleration * t_arr**2
    return t_arr, v, x
