from vectoriumPy.Energy import Kinetic_energy,Potential_energy,Mechanical_energy,Work,Power,Elastic_potential_energy,Efficiency
import pytest

def test_Kinetic_energy():
    # Case 1: Finding Kinetic energy
    assert Kinetic_energy(None,100,10) == 5000

    # Case 2 : Finding mass
    assert Kinetic_energy(100,None,10) == 2

    # Case 3 : Finding velocity
    assert Kinetic_energy(20000,100,None) ==  20

def test_Potential_():
    # Potential energy: PE = m * g * h (g passed explicitly)
    assert Potential_energy(None, 10, 9.8, 5) == 490
    assert Potential_energy(490, None, 9.8, 5) == 10
    assert Potential_energy(490, 10, 9.8, None) == 5

def test_Mechanical_energy():
    # Mechanical energy: ME = KE + PE
    # case 1 finding ME
    assert Mechanical_energy(None, 100, 200) == 300
    # case 2 finiding KE
    assert Mechanical_energy(300, None, 200) == 100
    # case 3 finiding PE
    assert Mechanical_energy(300, 100, None) == 200


def test_Work():
    # Work: W = F * d * cos(θ)
    assert Work(10, 5, 60, None) == pytest.approx(25, rel=1e-6)
    assert Work(None, 5, 60, 25) == pytest.approx(10, rel=1e-6)
    assert Work(10, None, 60, 25) == pytest.approx(5, rel=1e-6)
    # theta returned in degrees when None
    assert Work(10, 5, None, 25) == pytest.approx(60, rel=1e-6)

def test_Power():
    # Power: P = W / t
    assert Power(None, 100, 10) == pytest.approx(10, rel=1e-6)
    assert Power(10, None, 10) == pytest.approx(100, rel=1e-6)
    assert Power(10, 100, None) == pytest.approx(10, rel=1e-6)

def test_elastic_potential_energy():
    assert Elastic_potential_energy(None, 100, 0.2) == pytest.approx(2, rel=1e-6)
    assert Elastic_potential_energy(2, None, 0.2) == pytest.approx(100, rel=1e-6)
    assert Elastic_potential_energy(2, 100, None) == pytest.approx(0.2, rel=1e-6)
    with pytest.raises(ValueError):
        Elastic_potential_energy(None, None, 0.2)

def test_efficiency():
    assert Efficiency(None, 75, 100) == 75
    assert Efficiency(75, None, 100) == 75
    assert Efficiency(75, 75, None) == 100
    with pytest.raises(ZeroDivisionError):
        Efficiency(None, 75, 0)
    with pytest.raises(ValueError):
        Efficiency(None, None, 100)

