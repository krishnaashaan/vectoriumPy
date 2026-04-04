"""
Kinematics helper functions for VectoriumPy.
All functions accept None as the unknown placeholder (pythonic).
"""

def motion(u, v, a, t, s):
    """Compute one missing value among u, v, a, t, s for linear motion.

    Relations used:
    v = u + a*t
    s = u*t + 0.5*a*t**2

    Provide exactly one argument as None to compute it. If more than one
    is None a ValueError is raised.
    """
    params = [u, v, a, t, s]
    unknowns = params.count(None)
    if unknowns > 1:
        raise ValueError("Please provide values for at least three of the parameters (u, v, a, t, s).")

    if v is None:
        return u + a * t
    elif u is None:
        return v - a * t
    elif a is None:
        return (v - u) / t
    elif t is None:
        return (v - u) / a
    elif s is None:
        return u * t + 0.5 * a * t ** 2

    # If nothing is None, return displacement by default
    return s


def avg_velocity(u, v):
    """Average velocity (u+v)/2. Both u and v must be provided."""
    if u is None or v is None:
        raise ValueError("Please provide values for both initial velocity (u) and final velocity (v).")
    return (u + v) / 2


def angular_velocity(theta, t, omega):
    """Compute one of angular displacement (theta in degrees), time t, or angular velocity omega (deg/s)."""
    values = [theta, t, omega]
    if values.count(None) > 1:
        raise ValueError("Please provide values for two of the angular parameters.")
    elif omega is None:
        return theta / t
    elif theta is None:
        return omega * t
    elif t is None:
        return theta / omega
    return omega


def angular_acceleration(omega, t, alpha):
    """Compute one of angular velocity (omega), time t, or angular acceleration alpha.

    Relation: alpha = omega / t
    """
    values = [omega, t, alpha]
    if values.count(None) > 1:
        raise ValueError("Please provide values for two of the angular acceleration parameters.")
    elif alpha is None:
        return omega / t
    elif omega is None:
        return alpha * t
    elif t is None:
        return omega / alpha
    return alpha


def centripetal_acceleration(v, r, a):
    """Compute centripetal acceleration relation: a = v**2 / r

    Provide exactly one None to compute that value.
    """
    values = [v, r, a]
    if values.count(None) > 1:
        raise ValueError("Please provide values for two of the centripetal parameters.")
    elif a is None:
        return v ** 2 / r
    elif v is None:
        return (a * r) ** 0.5
    elif r is None:
        return v ** 2 / a
    return a


def momentum(m, v, p):
    """p = m * v; compute missing one when None provided."""
    values = [m, v, p]
    if values.count(None) > 1:
        raise ValueError("Please provide values for two of the momentum parameters.")
    elif p is None:
        return m * v
    elif m is None:
        return p / v
    elif v is None:
        return p / m
    return p


def impulse(F, t, J):
    """J = F * t; compute missing one when None provided."""
    values = [F, t, J]
    if values.count(None) > 1:
        raise ValueError("Please provide values for two of the impulse parameters.")
    elif J is None:
        return F * t
    elif F is None:
        return J / t
    elif t is None:
        return J / F
    return J


def Tangential_velocity(v, r, omega):
    """v = r * omega; compute missing one when None provided."""
    values = [v, r, omega]
    if values.count(None) > 1:
        raise ValueError("Please provide values for two of the tangential velocity parameters.")
    elif v is None:
        return r * omega
    elif r is None:
        return v / omega
    elif omega is None:
        return v / r
    return v
