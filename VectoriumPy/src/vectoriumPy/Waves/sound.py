"""
This module contains funtions for sound waves  in vectoriumPy.
"""
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
        return f*λ
    elif f is None:
        return v/λ
    elif λ is None:
        return v/f
def Doppler_effect():
    pass
  # Fuction Will be added in the future
    