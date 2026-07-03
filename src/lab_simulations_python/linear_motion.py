import numpy as np
from typing import Dict

def calculate_linear_motion(initial_position: float, initial_velocity: float, acceleration: float, time: float=0.0) -> Dict[str, float]:
    """
    Calculates the kinematic values for linear motion

    Args:
        initial_position: The initial position of the particle in m
        initial_velocity: The initial velocity of the particle in m/s
        acceleration: The constant acceleration in m/s^2
        time: The time in the final position in s

    Returns:
        A dictionary containing the final position and the final velocity
    """

    final_position = initial_position + (initial_velocity * time ) + (0.5 * acceleration * time**2)
    final_velocity = initial_velocity + (acceleration * time)

    return {
            "final_position": final_position,
            "final_velocity": final_velocity,
            }
