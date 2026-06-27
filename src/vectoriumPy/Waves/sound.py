"""
This module contains funtions for sound waves  in vectoriumPy.
"""
import numpy as np


def sound_wave(v,f,λ):
    """
    Calculate the velocity(v),frequency(f),and the wavelength(λ)of a sound wave
    
    Parameters:
    v (float): Velocity of the sound wave (m/s)
    f (float): Frequency of the sound wave (Hz)
    λ (float): Wavelength of the sound wave (m)
    Returns:
    tuple: A tuple containing the velocity, frequency, and wavelength of the sound wave.
    """
    known=[v,f,λ].count(None)
    if known>1:
        raise ValueError('Please provide values for at least three of the parameters.')
    if v is None:
        v = f*λ
        return v
    elif f is None:
        f = v/λ
        return f
    elif λ is None:
        λ = v/f
        return λ

def wave_period(T,f):
    """
    Calculate period and frequency of a wave.
    T = 1 / f
    parameters:
    T(float): Period (s)
    f(float): Frequency (Hz)
    """
    known = [T,f].count(None)
    if known != 1:
        raise ValueError("Please provide exactly one unknown parameter (T or f).")
    if T is None:
        return 1 / f
    elif f is None:
        return 1 / T

def angular_frequency(ω,f):
    """
    Calculate angular frequency from frequency.
    ω = 2πf
    parameters:
    ω(float): Angular frequency (rad/s)
    f(float): Frequency (Hz)
    """
    known = [ω,f].count(None)
    if known != 1:
        raise ValueError("Please provide exactly one unknown parameter (ω or f).")
    if ω is None:
        return 2 * np.pi * f
    elif f is None:
        return ω / (2 * np.pi)

def wave_intensity(I,P,A):
    """
    Calculate wave intensity.
    I = P / A
    parameters:
    I(float): Intensity (W/m^2)
    P(float): Power (W)
    A(float): Area (m^2)
    """
    known = [I,P,A].count(None)
    if known > 1:
        raise ValueError("Please provide values for at least two of the parameters (I, P, A).")
    if A == 0:
        raise ZeroDivisionError("Area cannot be zero.")
    if I is None:
        return P / A
    elif P is None:
        return I * A
    elif A is None:
        return P / I

  # Fuction Will be added in the future
    
