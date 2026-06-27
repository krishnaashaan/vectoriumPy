"""
This module deals with projectile motion.
"""
from typing import Optional, Sequence, Union

import numpy as np


Number = Union[int, float]


def _validate_single_unknown(values: Sequence[object]) -> None:
    if values.count(None) != 1:
        raise ValueError("Please provide exactly one unknown parameter as None.")


def _validate_gravity(g: Number) -> None:
    if g == 0:
        raise ZeroDivisionError("Acceleration due to gravity cannot be zero.")


def _validate_arcsin_value(value: Number) -> Number:
    if value < -1 or value > 1:
        raise ValueError("No real angle solution exists for the provided values.")
    return value


def _require_value(value: Optional[Number], name: str) -> Number:
    if value is None:
        raise ValueError(f"Please provide a value for {name}.")
    return value


def projectile_motion(u,θ,t,g=9.81):
    """
    Calculate the horizontal and vertical components of projectile motion.

    Parameters:
    u (float): Initial velocity (m/s)
    θ (float): Angle of projection (degrees)
    t (float): Time of flight (s)
    g (float, optional): Acceleration due to gravity (m/s²). Default is 9.81 m/s².

    Returns:
    tuple: A tuple containing the horizontal and vertical components of projectile motion.
    """
    if None in (u, θ, t):
        raise ValueError("Please provide values for initial velocity (u), angle (θ), and time (t).")
    # Convert angle from degrees to radians
    θ_rad = np.radians(θ)

    # Calculate horizontal and vertical components
    horizontal_component = u * np.cos(θ_rad) * t
    vertical_component = u * np.sin(θ_rad) * t - 0.5 * g * t**2

    return horizontal_component, vertical_component


def projectile_time_of_flight(T,u,θ,g=9.81):
    """
    Calculate total time of flight for a projectile launched and landing at the same height.

    T = (2 * u * sin(θ)) / g
    """
    _validate_single_unknown([T,u,θ])
    _validate_gravity(g)
    if T is None:
        u = _require_value(u, "initial velocity (u)")
        θ = _require_value(θ, "angle (θ)")
        θ_rad = np.radians(θ)
        return (2 * u * np.sin(θ_rad)) / g
    elif u is None:
        T = _require_value(T, "time of flight (T)")
        θ = _require_value(θ, "angle (θ)")
        θ_rad = np.radians(θ)
        denominator = 2 * np.sin(θ_rad)
        if denominator == 0:
            raise ZeroDivisionError("sin(θ) cannot be zero when calculating initial velocity.")
        return (T * g) / denominator
    elif θ is None:
        T = _require_value(T, "time of flight (T)")
        u = _require_value(u, "initial velocity (u)")
        if u == 0:
            raise ZeroDivisionError("Initial velocity u cannot be zero when calculating angle.")
        ratio = _validate_arcsin_value((T * g) / (2 * u))
        return np.degrees(np.arcsin(ratio))


def projectile_max_height(H,u,θ,g=9.81):
    """
    Calculate maximum height for a projectile launched from ground level.

    H = (u^2 * sin^2(θ)) / (2 * g)
    """
    _validate_single_unknown([H,u,θ])
    _validate_gravity(g)
    if H is None:
        u = _require_value(u, "initial velocity (u)")
        θ = _require_value(θ, "angle (θ)")
        θ_rad = np.radians(θ)
        return (u**2 * np.sin(θ_rad)**2) / (2 * g)
    elif u is None:
        H = _require_value(H, "maximum height (H)")
        θ = _require_value(θ, "angle (θ)")
        θ_rad = np.radians(θ)
        denominator = np.sin(θ_rad)**2
        if denominator == 0:
            raise ZeroDivisionError("sin(θ) cannot be zero when calculating initial velocity.")
        value = (2 * g * H) / denominator
        if value < 0:
            raise ValueError("No real initial velocity solution exists for the provided values.")
        return np.sqrt(value)
    elif θ is None:
        H = _require_value(H, "maximum height (H)")
        u = _require_value(u, "initial velocity (u)")
        if u == 0:
            raise ZeroDivisionError("Initial velocity u cannot be zero when calculating angle.")
        value = (2 * g * H) / u**2
        if value < 0:
            raise ValueError("No real angle solution exists for the provided values.")
        ratio = _validate_arcsin_value(np.sqrt(value))
        return np.degrees(np.arcsin(ratio))


def projectile_range(R,u,θ,g=9.81):
    """
    Calculate horizontal range for a projectile launched and landing at the same height.

    R = (u^2 * sin(2θ)) / g
    """
    _validate_single_unknown([R,u,θ])
    _validate_gravity(g)
    if R is None:
        u = _require_value(u, "initial velocity (u)")
        θ = _require_value(θ, "angle (θ)")
        θ_rad = np.radians(θ)
        return (u**2 * np.sin(2 * θ_rad)) / g
    elif u is None:
        R = _require_value(R, "range (R)")
        θ = _require_value(θ, "angle (θ)")
        θ_rad = np.radians(θ)
        denominator = np.sin(2 * θ_rad)
        if denominator == 0:
            raise ZeroDivisionError("sin(2θ) cannot be zero when calculating initial velocity.")
        value = (R * g) / denominator
        if value < 0:
            raise ValueError("No real initial velocity solution exists for the provided values.")
        return np.sqrt(value)
    elif θ is None:
        R = _require_value(R, "range (R)")
        u = _require_value(u, "initial velocity (u)")
        if u == 0:
            raise ZeroDivisionError("Initial velocity u cannot be zero when calculating angle.")
        ratio = _validate_arcsin_value((R * g) / u**2)
        return 0.5 * np.degrees(np.arcsin(ratio))
