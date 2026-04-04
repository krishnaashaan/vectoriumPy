from vectoriumPy.Optics import  mirror_formula,lens_formula,magnification,power_dioptre
import pytest
def test_mirror_formula():
    assert mirror_formula('?',10,10) == 5
    assert mirror_formula(5,10,'?') ==10
    assert mirror_formula(5,'?',10)==10
    with pytest.raises(ValueError):
        mirror_formula("?","?",10)
       
def test_lens_formula():
    assert lens_formula("?",10,20) == 20
    assert lens_formula(20,"?",10) == 20
    assert lens_formula(20,10,"?") == 20

    with pytest.raises(ValueError):
        lens_formula("?","?",10)

def test_magnification():
    # Mirror mode
    assert magnification(-60,-30,mode='mirror') == {'m': -2.0, 'nature': 'Real & Inverted', 'size': 'Magnified'}
    # Lens mode
    assert magnification(-60,-30,mode='lens')==  {'m': 2.0, 'nature': 'Virtual & Upright', 'size': 'Magnified'}

def test_power_dioptre():
    assert power_dioptre(-20)=={'power_dioptre': -5.0, 'type': 'Diverging (Concave)'}
