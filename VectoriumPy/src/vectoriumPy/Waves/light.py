"""
Module for light & its properties related functions
"""
def light_wave(v,f,λ):
    """
    Calculate the velocity(v),frequency(f),and the wavelength(λ)of a light wave
    
    Parameters:
    v (float): Velocity of the light wave (m/s)
    f (float): Frequency of the light wave (Hz)
    λ (float): Wavelength of the light wave (m)
    Returns:
    tuple: A tuple containing the velocity, frequency, and wavelength of the light wave.
    """
    unknown_count = [v,f,λ].count(None)
    if unknown_count > 1:
        raise ValueError('Please provide values for at least two of the parameters.')
    if v is None:
        return f*λ
    elif f is None:
        return v/λ
    elif λ is None:
        return v/f
def Doppler_effect(Fs,Fo,v,v_s):
    """
    Calculate the observed frequency (F) of a sound wave using the Doppler effect formula.

    Parameters:
    Fs (float): Source frequency (Hz)
    Fo (float): Observed frequency (Hz)
    v (float): Velocity of the observer (m/s)
    v_s (float): Velocity of the source (m/s)

    Returns:
    float: The observed frequency (F) in Hz.
    """
    if v_s == 0:
        raise ValueError("Velocity of the source cannot be zero.")

    F = Fs * ((v + v_s) / (v - v_s))
    return F
def Snell_law(n1,n2,θ1,θ2):
    """
    Calculate the refractive index(n) using Snell's law.

    Parameters:
    n1 (float): Refractive index of the first medium
    n2 (float): Refractive index of the second medium
    θ1 (float): Angle of incidence (degrees)
    θ2 (float): Angle of refraction (degrees)

    Returns:
    float: The refractive index (n)
    """
    import math

    none_count = [n1, n2, θ1, θ2].count(None)
    if none_count > 2:
        raise ValueError('Please provide values for at least two of the parameters.')

    def to_rad(angle):
        return None if angle is None else math.radians(angle)

    # Both refractive indices missing but angles present -> return ratio sin(θ1)/sin(θ2)
    if n1 is None and n2 is None:
        θ1r = to_rad(θ1)
        θ2r = to_rad(θ2)
        if θ1r is None or θ2r is None:
            raise ValueError('Insufficient known parameters to compute refractive indices.')
        return math.sin(θ1r) / math.sin(θ2r)

    # Compute n1 when missing
    if n1 is None:
        θ1r = to_rad(θ1)
        θ2r = to_rad(θ2)
        if n2 is None or θ1r is None or θ2r is None:
            raise ValueError('Insufficient known parameters to compute n1.')
        return n2 * math.sin(θ2r) / math.sin(θ1r)

    # Compute n2 when missing
    elif n2 is None:
        θ1r = to_rad(θ1)
        θ2r = to_rad(θ2)
        if θ1r is None or θ2r is None:
            raise ValueError('Insufficient known parameters to compute n2.')
        return n1 * math.sin(θ1r) / math.sin(θ2r)

    # Compute missing angle(s)
    elif θ1 is None:
        θ2r = to_rad(θ2)
        if θ2r is None:
            raise ValueError('Insufficient known parameters to compute θ1.')
        if n1 == 0:
            raise ValueError('Invalid refractive index n1.')
        return math.degrees(math.asin((n2 * math.sin(θ2r)) / n1))

    elif θ2 is None:
        θ1r = to_rad(θ1)
        if θ1r is None:
            raise ValueError('Insufficient known parameters to compute θ2.')
        if n2 == 0:
            raise ValueError('Invalid refractive index n2.')
        return math.degrees(math.asin((n1 * math.sin(θ1r)) / n2))

    # If both refractive indices provided, return them
    return n1, n2