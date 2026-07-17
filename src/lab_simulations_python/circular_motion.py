from typing import Dict

import numpy as np


def calculate_circular_motion(
    radius: float, angular_velocity: float, time: float = 0.0
) -> Dict[str, float]:
    """
    Calculates the kinematic values for uniform circular motion

    Args:
        radius: The radius of the circular path in m
        angular_velocity: The angular velocity in rad/s
        time: The elapsed time in s

    Returns:
        A dictionary containing the linear speed, period, frequency,
        centripetal acceleration, and the position (x, y) at the given time
    """

    linear_speed = angular_velocity * radius
    period = 2 * np.pi / angular_velocity
    frequency = angular_velocity / (2 * np.pi)
    centripetal_acceleration = angular_velocity**2 * radius

    angle = angular_velocity * time
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    return {
        "linear_speed": linear_speed,
        "period": period,
        "frequency": frequency,
        "centripetal_acceleration": centripetal_acceleration,
        "x": x,
        "y": y,
    }


def circular_series(radius: float, angular_velocity: float, time: float, n: int = 500):
    """
    Position components x(t_arr) and y(t_arr) over the interval [0, time].

    Returns:
        A tuple (t_arr, x, y) of NumPy arrays.
    """

    t_arr = np.linspace(0, time, num=n)
    x = radius * np.cos(angular_velocity * t_arr)
    y = radius * np.sin(angular_velocity * t_arr)
    return t_arr, x, y
