import pytest
import numpy as np
from vectoriumPy import magnetic_force,magnetic_flux,amperes_law

def test_magnetic_force():
    assert magnetic_force(None,1.6e-19,2.0e6,0.5,90) == 1.6e-13 # Newtons
    assert magnetic_force(1.6e-13,None,2.0e6,0.5,90) == 1.6e-19 # Coloumbs
    assert magnetic_force(1.6e-13,1.6e-19,None,0.5,90)== 2.0e6 # m/s
    assert magnetic_force(1.6e-13,1.6e-19,2.0e6,None,90)==0.5 # Tesla
    with pytest.raises(ValueError):
        magnetic_force(None,None,10,1,90)

def test_magnetic_flux():
    assert magnetic_flux(None,0.5,2,30) == 0.87 #Wb
    assert magnetic_flux(0.87,None,2,30) == 0.5 # Tesla
    assert magnetic_flux(0.87,0.5,None,30) == 2.01 # m²
    with pytest.raises(ValueError):
        magnetic_flux(None,None,10,90)

def test_amperes_law():
    assert amperes_law(None,4*np.pi*1e-7,5,0.1) == 1e-05 # Tesla
    assert amperes_law(1e-5,None,5,0.1) == 1.2566370614359175e-06 # μ
    assert amperes_law(1e-5,4*np.pi*1e-7,None,0.1) == 5 # Amperes
    assert amperes_law(1e-5,4*np.pi*1e-7,5,None) == 0.1 # meters
    with pytest.raises(ValueError):
        amperes_law(None,None,10,0.1)