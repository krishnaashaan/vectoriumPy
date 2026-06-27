from vectoriumPy import first_law_thermodynamics,entropy,enthalpy,Gibbs_free_energy,Helmholtz_free_energy,ideal_gas_law,Latent_Heat
import pytest
def test_first_law_thermodynamics():
    # Case 1: ΔU is unknown
    assert first_law_thermodynamics(None, 50, 20) == 30
    # Case 2: Q is unknown
    assert first_law_thermodynamics(100, None, 20) == 120
    # Case 3: W is unknown
    assert first_law_thermodynamics(100, 50, None) == -50 # THE SYSTEM IS BEING COMPRESSED
    # Case 4: More than one parameter is unknown
    with pytest.raises(ValueError):
        first_law_thermodynamics(None, None, 20)

def test_entropy():
    # Case 1 ΔS is unknown
    assert entropy(100,50,None) == 2
    # Case 2 Q is unknown
    assert entropy(None,50,2) == 100
    # Case 3 T is unknown
    assert entropy(100,None,2) == 50
    # Case 4: Temperature is zero or negative
    with pytest.raises(ValueError):
        entropy(100, 0, None)
    # Case 5: More than one parameter is unknown
    with pytest.raises(ValueError):
        entropy(None, None, 2)

def test_enthalpy():
    # Case 1 H is unknown
    assert enthalpy(None,100,50,2)== 200
    # Case 2 U is unknown
    assert enthalpy(200,None,50,2)== 100
    # Case 3 P IS unknown
    assert enthalpy(200,100,None,2)== 50
    # Case 4 V is unknown
    assert enthalpy(200,100,50,None)== 2
    # Case 5: More than one parameter is unknown
    with pytest.raises(ValueError):
        enthalpy(None, None, 50, 2)

def test_Gibbs_free_energy():
    # Case1 G is unknown
    assert Gibbs_free_energy(None,100,50,2) ==0
    # Case 2 H is unknown
    assert Gibbs_free_energy(0,None,50,2)== 100
    # Case 3 T is unknown 
    assert Gibbs_free_energy(0,100,None,2)== 50
    # Case 4 S is unknown
    assert Gibbs_free_energy(0,100,50,None)==2
    # Case 5: Temperature is zero or negativete
    with pytest.raises(ValueError):
        Gibbs_free_energy(None,100,0,2)
    # Case 6: More than one parameter is unknown
    with pytest.raises(ValueError):
        Gibbs_free_energy(None, None,50,2)

def test_Helmholtz_free_energy():
    # Case 1 A is unknown
    assert Helmholtz_free_energy(None,100,50,2) == 0
    # Case 2 U is unknown
    assert Helmholtz_free_energy(0,None,50,2) == 100
    #Case 3 T is unknown 
    assert Helmholtz_free_energy(0,100,None,2)== 50
    # Case 4 S is unknown
    assert Helmholtz_free_energy(0,100,50,None)==2
    # Case 5: Temperature is zero or negative
    with pytest.raises(ValueError):
        Helmholtz_free_energy(None,100,0,2)
    # Case 6: More than one parameter is unknown
    with pytest.raises(ValueError):
        Helmholtz_free_energy(None, None,50,2)

def test_ideal_gas_law():
    # Case 1 P is unknown
    assert ideal_gas_law(None,10,1,300,8.314) == 249.42
    # Case 2 V is unknown
    assert ideal_gas_law(2494.2,None,1,300,8.314) == 1
    # Case 3 n is unknown
    assert ideal_gas_law(2494.2,10,None,300,8.314) == 10
    # Case 4 T is unknown
    assert ideal_gas_law(2494.2,10,1,None,8.314) == 3000
    # Case 5 R is unknown
    assert ideal_gas_law(2494.2,10,1,3000,None) == 8.314
    # Case 6: More than one parameter is unknown
    with pytest.raises(ValueError):
        ideal_gas_law(None, None,1,300,8.314)

def test_latent_heat():
    # Case 1 : Q is unknown
    assert Latent_Heat(None,2,334000) == 668000
    # Case 2 : m is unknown
    assert Latent_Heat(668000,None,334000) == 2
    # Case 3 : L is unknown
    assert Latent_Heat(668000,2,None) == 334000 
    # Case 4 : More than one parameter is unknown
    with pytest.raises(ValueError):
        Latent_Heat(None, None, 334000)

