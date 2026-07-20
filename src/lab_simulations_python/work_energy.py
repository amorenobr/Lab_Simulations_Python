from typing import Dict

import numpy as np

g = 9.81  # gravitational acceleration (m/s^2)


def calculate_work_energy(
    mass: float, initial_height: float, initial_velocity: float, time: float = 0.0
) -> Dict[str, float]:
    """
    Calculates the mechanical energy of an object moving vertically under gravity, ilustrating conservation
    of energy (kinetic + potential).

    Args:
        mass: The mass of the object in kg
        initial_height: The initial height above the reference level in m
        initial_velocity: The initial vertical velocity (positive upward) in m/s
        time: The elapsed time in s

    Returns:
        A dictionary containing the kinetic, potential, and total mechanical energy at the given time
    """

    velocity = initial_velocity - g * time
    height = initial_height + initial_velocity * time - 0.5 * g * time**2

    kinetic_energy = 0.5 * mass * velocity**2
    potential_energy = mass * g * height
    total_energy = kinetic_energy + potential_energy

    return {
        "kinetic_energy": kinetic_energy,
        "potential_energy": potential_energy,
        "total_energy": total_energy,
    }


def energy_series(
    mass: float, initial_height: float, initial_velocity: float, time: float, n: int = 500
):
    """
    Kinetic, potential, and total energy over the interval [0, time].

    Args:
        mass: The mass of the object in kg
        initial_height: The initial height above the reference level in m
        initial_velocity: The initial vertical velocity (positive upward) in m/s
        time: The elapsed time in s
        n: The number of samples

    Returns:
        A tuple (t_arr, kinetic, potential, total) of NumPy arrays.
    """

    t_arr = np.linspace(0, time, num=n)
    velocity = initial_velocity - g * t_arr
    height = initial_height + initial_velocity * t_arr - 0.5 * g * t_arr**2

    kinetic = 0.5 * mass * velocity**2
    potential = mass * g * height
    total = kinetic + potential
    return t_arr, kinetic, potential, total
