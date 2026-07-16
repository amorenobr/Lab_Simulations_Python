from typing import Dict


def calculate_free_fall(
    initial_position: float, initial_velocity: float, time: float = 0.0
) -> Dict[str, float]:
    """
    Calculates the kinematic values for free fall

    Args:
        initial_position: The initial position of the particle in m
        initial_velocity: The initial velocity of the particle in m/s
        time: The time in the final position in s

    Returns:
        A dictionary containing the final position and the final velocity
    """

    g = 9.81

    final_position = initial_position + (initial_velocity * time) - (0.5 * g * time**2)
    final_velocity = initial_velocity - (g * time)

    return {
        "final_position": final_position,
        "final_velocity": final_velocity,
    }
