from vectoriumPy.Waves.sound import sound_wave
from vectoriumPy.Waves.sound import wave_period,angular_frequency,wave_intensity
from vectoriumPy.Waves.light import light_wave,Doppler_effect,Snell_law
import pytest
def test_sound_wave():
    # Test case 1: Calculate velocity given frequency and wavelength
    assert sound_wave(None, 440, 0.78) == 343.2

    # Test case 2: Calculate frequency given velocity and wavelength
    assert sound_wave(343.2, None, 0.78) == (pytest.approx(440, rel=1e-2))

    # Test case 3: Calculate wavelength given velocity and frequency
    assert sound_wave(343.2, 440, None) == 0.78

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        sound_wave(None, None, 0.78)
def test_light_wave():
    # Test case 1: Calculate velocity given frequency and wavelength
    assert light_wave(None, 5e14, 600e-9) == 3e8

    # Test case 2: Calculate frequency given velocity and wavelength
    assert light_wave(3e8, None, 600e-9) == 5e14

    # Test case 3: Calculate wavelength given velocity and frequency
    assert light_wave(3e8, 5e14, None) == 600e-9

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        light_wave(None, None, 600e-9)
def test_Doppler_effect():
    # Test case 1: Calculate observed frequency given source frequency, observer velocity, and source velocity
    assert Doppler_effect(440, None, 30, 20) == 2200

    # Test case 2: Raise ValueError when velocity of the source is zero
    with pytest.raises(ValueError):
        Doppler_effect(440, None, 30, 0)
def test_Snell_law():
    # Test case 1: Calculate refractive index given angles of incidence and refraction
    assert Snell_law(None, None, 30, 20) == (pytest.approx(1.46,rel = 1e-2))

    # Test case 2: Raise ValueError when more than two parameters are None
    with pytest.raises(ValueError):
        Snell_law(None, None, None, 20)

def test_wave_period():
    assert wave_period(None, 50) == 0.02
    assert wave_period(0.02, None) == 50
    with pytest.raises(ValueError):
        wave_period(None, None)

def test_angular_frequency():
    assert angular_frequency(None, 50) == pytest.approx(314.1592653589793, rel=1e-6)
    assert angular_frequency(314.1592653589793, None) == pytest.approx(50, rel=1e-6)
    with pytest.raises(ValueError):
        angular_frequency(None, None)

def test_wave_intensity():
    assert wave_intensity(None, 100, 20) == 5
    assert wave_intensity(5, None, 20) == 100
    assert wave_intensity(5, 100, None) == 20
    with pytest.raises(ZeroDivisionError):
        wave_intensity(None, 100, 0)
    with pytest.raises(ValueError):
        wave_intensity(None, None, 20)
