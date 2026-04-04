from vectoriumPy import ohms_law,electric_capacitance,electric_power,electric_resonance,electric_energy,Joules_law_of_heating
from vectoriumPy.Electricity.circuit import series_resistance,parallel_resistance,voltage_division,current_division
import pytest
def test_ohms_law():
    # Test case 1: Calculate voltage given current and resistance
    assert ohms_law('?', 2, 5) == 10

    # Test case 2: Calculate current given voltage and resistance
    assert ohms_law(10, '?', 5) == 2

    # Test case 3: Calculate resistance given voltage and current
    assert ohms_law(10, 2, '?') == 5

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        ohms_law('?', '?', 5)

def test_electric_power():
    # Test case 1: Calculate power given voltage and current
    assert electric_power('?', 10, 2) == 20

    # Test case 2: Calculate voltage given power and current
    assert electric_power(20, '?', 2) == 10

    # Test case 3: Calculate current given power and voltage
    assert electric_power(20, 10, '?') == 2

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        electric_power('?', '?', 2)
def test_EE():
    # Test case 1: Calculate energy given power and time
    assert electric_energy('?', 20, 5) == 100

    # Test case 2: Calculate power given energy and time
    assert electric_energy(100, '?', 5) == 20

    # Test case 3: Calculate time given energy and power
    assert electric_energy(100, 20, '?') == 5

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        electric_energy('?', '?', 5)
def test_electric_capacitance():
    # Test case 1: Calculate capacitance given charge and voltage
    assert electric_capacitance('?', 10, 5) == 2

    # Test case 2: Calculate charge given capacitance and voltage
    assert electric_capacitance(2, '?', 5) == 10

    # Test case 3: Calculate voltage given capacitance and charge
    assert electric_capacitance(2, 10, '?') == 5

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        electric_capacitance('?', '?', 5)
def test_electric_resonance():
    # Test case 1: Calculate resonant frequency given inductance and capacitance
    assert electric_resonance('?', 0.01, 0.0001) == 159.15494309189535

    # Test case 2: Calculate inductance given resonant frequency and capacitance
    assert electric_resonance(159.15494309189535, '?', 0.0001) == 0.01

    # Test case 3: Calculate capacitance given resonant frequency and inductance
    assert electric_resonance(159.15494309189535, 0.01, '?') == 0.0001

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        electric_resonance('?', '?', 0.0001)
def test_series_resistance():
    # Test case 1: Calculate total resistance for series resistors
    assert series_resistance(10, 20, 30) == 60

    # Test case 2: Calculate total resistance for series resistors with one resistor missing
    assert series_resistance('?', 20, 30) == 50    
    assert series_resistance(10, '?', 30) == 40
    assert series_resistance(10, 20, '?') == 30
    # Test case 3: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        series_resistance('?', '?', 30)
def test_parallel_resistance():
    # Test case 1: Calculate total resistance for parallel resistors
    assert parallel_resistance(10, 20, 30) == 12

    # Test case 2: Calculate total resistance for parallel resistors with one resistor missing
    assert parallel_resistance('?', 20, 30) == 12
    assert parallel_resistance(10, '?', 30) == 15
    assert parallel_resistance(10, 20, '?') == 20
    # Test case 3: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        parallel_resistance('?', '?', 30)

def test_voltage_division():
    # Test case 1: Calculate output voltage in a voltage divider circuit
    assert voltage_division('?', 10, 20, 30) == 6

    # Test case 2: Calculate output voltage in a voltage divider circuit with one parameter missing
    assert voltage_division('?', 2, 20, 30) == 1.2
    assert voltage_division('?', 10, 2, 30) == 9.375
    assert voltage_division('?', 10, 20, 2) == 0.9090909090909092

    # Test case 3: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        voltage_division('?', '?', '?', 30)
def test_current_division():
    # Test case 1: Calculate output current in a current divider circuit
    assert current_division('?', 10, 20, 30) == 4

    # Test case 2: Calculate output current in a current divider circuit with one parameter missing
    # Test case 3: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        current_division('?', '?', 20, 30)
    with pytest.raises(ValueError):
        current_division('?', 10, '?', 30)
    with pytest.raises(ValueError):
        current_division('?', 10, 20, '?')
    with pytest.raises(ValueError):
        current_division('?', '?', '?', 30)
def test_Joules_law_of_heating():
    # Test case 1: Calculate heat produced given current, resistance, time, and heat
    assert Joules_law_of_heating(2, 10, 5, '?') == 200

    # Test case 2: Calculate heat produced given current, resistance, time, and heat
    assert Joules_law_of_heating(2, 10, '?', 200) == 5

    # Test case 3: Calculate heat produced given current, resistance, time, and heat
    assert Joules_law_of_heating(2, '?', 5, 200) == 10

    # Test case 4: Calculate heat produced given current, resistance, time, and heat
    assert Joules_law_of_heating('?', 10, 5, 200) == 2

    # Test case 5: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        Joules_law_of_heating('?', '?', '?', 200)