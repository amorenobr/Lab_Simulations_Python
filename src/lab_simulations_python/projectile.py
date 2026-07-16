from typing import Dict

import numpy as np


def calculate_kinematics(initial_velocity: float, launch_angle: float) -> Dict[str, float]:
    """
    Calculates the kinematic parameters for projectile motion

    Args:
        initial_velocity: The initial velocity of the projectile in m/s
        launch_angle: The launch angle in degrees

    Returns:
        A dictionary containing the time of flight, max height, and horizontal range
    """
    g = 9.81
    angle_rad = np.deg2rad(launch_angle)

    t_flight = (2 * initial_velocity * np.sin(angle_rad)) / g
    max_height = (initial_velocity**2 * np.sin(angle_rad) ** 2) / (2 * g)
    horizontal_range = (initial_velocity**2 * np.sin(2 * angle_rad)) / g

    return {
        "t_flight": t_flight,
        "max_height": max_height,
        "horizontal_range": horizontal_range,
    }
