import numpy as np
from typing import Dict

def calculate_oscillation(mass: float, spring_constant: float, damping_coefficient: float = 0.0) -> Dict[str, float]:
    """
    Calculates the characteristic properties of a damped harmonic oscillator

    Args:
        mass: Mass on the spring in kg
        spring constant: Spring constant k in N/m
        damping coefficient: Damping coefficient b in kg/S (0=undamped)

    Returns:
        A dictionary with natural angular frequency, natural frequency, period,
        damping ratio and the oscillation regime
    """
    
    omega_0 = np.sqrt(spring_constant / mass)
    damping_ratio = damping_coefficient / (2 * np.sqrt(spring_constant * mass))

    if damping_ratio == 0:
        regime = "undamped"
    elif damping_ratio < 1:
        regime = "underdamped"
    elif np.isclose(damping_ratio, 1.0):
        regime = "critically damped"
    else:
        regime = "overdamped"

    return{
            "omega_0": omega_0,
            "natural_frequency": omega_0 / (2 * np.pi),
            "period": 2 * np.pi / omega_0,
            "damping_ratio": damping_ratio,
            "regime": regime,
            }

def displacement(t: np.ndarray, mass: float, spring_constant: float, amplitude: float, damping_coefficient: float = 0.0) -> np.ndarray:
    """
    Position x(t) for a damped harmonic oscillator released from rest at
    x = amplitude (initial conditions x(0)=A, v(0)=0)
    """

    omega_0 = np.sqrt(spring_constant / mass)
    gamma = damping_coefficient / (2 * mass)

    if gamma == 0:
        return amplitude * np.cos(omega_0 * t)

    if gamma < omega_0:
        omega_d = np.sqrt(omega_0**2 - gamma**2)
        return amplitude * np.exp(-gamma * t) * (np.cos(omega_d * t) + (gamma / omega_d) * np.sin(omega_d * t))

    if np.isclose(gamma, omega_0):
        return amplitude * np.exp(-gamma * t) * (1 + gamma *t)

    beta = np.sqrt(gamma**2 - omega_0**2)
    return amplitude * np.exp(-gamma * t) * (np.cosh(beta * t) + (gamma / beta) * np.sinh(beta * t))
