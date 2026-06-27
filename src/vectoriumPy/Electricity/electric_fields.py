"""
Module for electric field calculations.
"""

import numpy as np


def electric_field_point_charge(E, q, r):
    """
    Calculate electric field strength due to a point charge.

    E = k * q / r^2

    parameters:
    E(float): Electric field strength (N/C)
    q(float): Charge (C)
    r(float): Distance from the charge (m)
    """
    k = 8.9875517923e9
    values = [E, q, r].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (E, q, r).")
    if r == 0:
        raise ZeroDivisionError("Distance r cannot be zero.")
    if E is None:
        return k * q / r**2
    elif q is None:
        return E * r**2 / k
    elif r is None:
        return np.sqrt(k * q / E)


def electric_potential_point_charge(V, q, r):
    """
    Calculate electric potential due to a point charge.

    V = k * q / r

    parameters:
    V(float): Electric potential (V)
    q(float): Charge (C)
    r(float): Distance from the charge (m)
    """
    k = 8.9875517923e9
    values = [V, q, r].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (V, q, r).")
    if r == 0:
        raise ZeroDivisionError("Distance r cannot be zero.")
    if V is None:
        return k * q / r
    elif q is None:
        return V * r / k
    elif r is None:
        return k * q / V


def uniform_electric_field(E, V, d):
    """
    Calculate a uniform electric field between two points or plates.

    E = V / d

    parameters:
    E(float): Electric field strength (V/m)
    V(float): Potential difference (V)
    d(float): Separation distance (m)
    """
    values = [E, V, d].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (E, V, d).")
    if d == 0:
        raise ZeroDivisionError("Distance d cannot be zero.")
    if E is None:
        return V / d
    elif V is None:
        return E * d
    elif d is None:
        return V / E
