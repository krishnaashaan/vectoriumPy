## Module for motion in vectoriumPy

def motion(u,v,a,t,s):

    """
    Function to calculate the motion of an object given its initial velocity, final velocity, acceleration, and time.

    Parameters:
    u (float): Initial velocity (m/s)
    v (float): Final velocity (m/s)
    a (float): Acceleration (m/s^2)
    t (float): Time (s)

    Returns:
    dict: A dictionary containing the calculated values for displacement, average velocity, and final velocity.
    """
    values = [u, v, a, t,s].count(None)
    if values> 1:
        raise ValueError("Please provide values for at least three of the parameters (u, v, a, t).")
    if v is None:
        return u + a * t
    elif u is None:
        return v - a * t
    elif a is None:
        return (v - u) / t
    elif t is None:
        return (v - u) / a
    elif s is None:
        s= u*t + 0.5*a*t**2
        return s

def avg_velocity(u,v):
    """
    Function to calculate the average velocity of an object given its initial and final velocities.
    """
    if u is None or v is None:
        raise ValueError("Please provide values for both initial velocity (u) and final velocity (v).")
    return (u + v) / 2

def angular_velocity(θ, t, ω):
    """
    Function to calculate the angular velocity of an object given its angular displacement and time.
    parameters:
    θ(float): Angular displacement (radians)
    t(float): Time (seconds)
    ω(float): Angular velocity (radians per second)
     ω = θ/t
    """
    values=[θ,t,ω].count(None)
    if values > 1:
        raise ValueError("Please provide values for both angular displacement (theta) and time (t).")
    if ω is None:
        return θ / t
    elif θ is None:
        return ω * t
    elif t is None:
        return θ / ω

def angular_acceleration(ω, t, α):
    """
    Function to calculate the angular acceleration of an object given its angular velocity and time.
    α = ω/t
    parameters:
    ω(float): Angular velocity (radians per second)
    t(float): Time (seconds)
    α(float): Angular acceleration (radians per second squared)
    """
    values=[ω,t,α].count(None)
    if values > 1:
        raise ValueError("Please provide values for both angular velocity (omega) and time (t).")
    if α is None:
        return ω / t
    elif ω is None:
        return α * t
    elif t is None:
        return ω / α

def centripetal_acceleration(v, r,a):
    """
    Function to calculate the centripetal acceleration of an object given its velocity and radius of curvature.
    a = v^2/r
    parameters:
    v(float):Velocity (m/s)
    r(float):Radius of curvature (m)
    a(float):Centripetal acceleration (m/s^2)
    """
    values=[v,r,a].count(None)
    if values > 1:
        raise ValueError("Please provide values for both velocity (v) and radius of curvature (r).")
    if v is None:
        return (r * a) ** 0.5
    elif r is None:
        return v ** 2 / a
    elif a is None:
        return v ** 2 / r

def momentum(m,v,p):
    """
    function to calculate momentrum(p) of an object given mass and velocity.
    p = m * v
    parameters:
    m(float): Mass of the object (kg)
    v(float): Velocity of the object (m/s)
    p(float): Momentum of the object (kg*m/s)
    """
    values=[m,v,p].count(None)
    if values>1:
        raise ValueError("Please provide values for both mass (m) and velocity (v).")
    if p is None:
        p = m*v
        return p
    elif m is None:
        m = p/v
        return m
    elif v is None:
        v = p/m
        return v

def impulse(F,t,J):
    """
    Function to calculate the impulse (J) of an object given the force (F) applied and the time (t) for which it is applied.
    J = F * t
    parameters:
    F(float): Force applied (N)
    t(float): Time for which the force is applied (s)
    J(float): Impulse (N*s)
    """
    values=[F,t,J].count(None)
    if values>1:
        raise ValueError("Please provide values for both force (F) and time (t).")
    if J is None:
        J = F*t
        return J
    elif F is None:
        F = J/t
        return F
    elif t is None:
        t = J/F
        return t

def Tangential_velocity(v,r,ω):
    """
    Function to calculate the tangential velocity of an object given its angular velocity and radius of curvature.
    v = r * ω
    parameters:
    v(float): Tangential velocity (m/s)
    r(float): Radius of curvature (m)
    ω(float): Angular velocity (radians per second)
    """
    values=[v,r,ω].count(None)
    if values>1:
        raise ValueError("Please provide values for both radius of curvature (r) and angular velocity (omega).")
    if v is None:
        v = r*ω
        return v
    elif r is None:
        r = v/ω
        return r
    elif ω is None:
        ω = v/r
        return ω

## More functions will be added in future updates.   