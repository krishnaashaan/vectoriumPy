"""
This module contains the gravity related calculations for vectoriumPy
"""
import numpy as np
def gravitational_force(m1,m2,r,F):
    '''
    This function calculates the gravitational force between two masses (m1 and m2) separated by a distance (r).
    F = G * (m1 * m2) / r^2
    parameters:
    m1(float):Mass of the first object(kg)
    m2(float):Mass od the second object(kg)
    r(float):Distance between m1 and m2 (m)
    F(float):Gravitational force between m1 and m2 (N)
    '''
    G = 6.67430e-11  # Gravitational constant
    values = [m1, m2, r, F].count(None)
    if values > 1:
        raise ValueError("Please provide values for all but one parameter (m1, m2, r, F).")
    if m1 is None:
        return (F * r**2) / (G * m2)
    elif m2 == None:
        return F * r**2 / (G * m1)
    elif r == None:
        return (G * m1 * m2 / F) ** 0.5
    elif F == None:
        return G * m1 * m2 / r**2
    
def escape_velocity(v,m,r):
    '''
    This function calculates the escape velocity from a celestial body of mass (m) and radius (r).
    v = sqrt(2 * G * m / r)
    parameters:
    m(float):Mass of the celestial body (kg)
    r(float):Radius of the celestial body (m)
    v(float):Escape velocity (m/s)
    '''
    G = 6.67430e-11  # Gravitational constant
    values = [v,m,r].count(None)
    if values > 1:
        raise ValueError("Please provide values for all but one parameter (m, r, v).")
    if m == None:
        return v**2 * r / (2 * G)
    elif r == None:
        return 2 * G * m / v**2
    elif v == None:
        return np.sqrt(2 * G * m / r)
