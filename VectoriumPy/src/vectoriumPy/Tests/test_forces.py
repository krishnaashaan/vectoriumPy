import pytest
from vectoriumPy.Force  import gravitational_force,Frictional_force,centripetal_force,Torque,electrostatic_force,escape_velocity,Hookes_law,Stress,Tension,buoyant_force,Archimedes_principle,Lorentz_force,Lift
def test_gravitational_force():
    # Test case 1: Calculate gravitational force given two masses and distance
    assert gravitational_force(1e50, 2e15, 5e5, '?') == pytest.approx(5.33944e43, rel=1e-6)

    # Test case 2: Calculate mass of the first object given gravitational force, second mass, and distance
    assert gravitational_force('?', 7.348e22, 384400000, 1.982e20) == pytest.approx(5.972e24, rel=1e-4)

    # Test case 3: Calculate mass of the second object given gravitational force, first mass, and distance
    assert gravitational_force(5.972e24, '?', 384400000, 1.982e20) == pytest.approx(7.348e22, rel=1e-4)

    # Test case 4: Calculate distance given gravitational force and two masses
    assert gravitational_force(5.972e24, 7.348e22, '?', 1.982e20) == pytest.approx(384400000, rel=1e-4)

    # Test case 5: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        gravitational_force('?', '?', 384400000, 1.982e20)
        
def test_Torque():
    # Test case 1: Calculate torque given force,radius and angle
    assert Torque('?',10,3,30) == pytest.approx(15, rel=1e-6)
    # Test case 2: Calculate force given torque, radius and angle
    assert Torque(20,'?',2,30) == pytest.approx(20, rel=1e-6)
    # Test case 3: Calculate radius given torque, force and angle
    assert Torque(30,10,'?',30) == pytest.approx(6, rel=1e-6)
    # Test case 4: calculate θ given torque,force,radius
    # angle returned in radians; allow small tolerance for rounding
    assert Torque(50,20,10,'?') == pytest.approx(0.252680255, rel=2e-2)
    # Test case 5: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        Torque('?', '?', 384400000, 1.982e20)

def test_friction():
    # Frictional_force tests: F = μ * N
    assert Frictional_force('?', 0.5, 100) == pytest.approx(50, rel=1e-6)
    assert Frictional_force(50, '?', 100) == pytest.approx(0.5, rel=1e-6)
    assert Frictional_force(50, 0.5, '?') == pytest.approx(100, rel=1e-6)
    with pytest.raises(ValueError):
        Frictional_force('?', '?', 100)
def test_cemtripetal():
    # Centripetal force tests: F = m * v^2 / r
    assert centripetal_force('?', 3, 1, 18) == pytest.approx(2, rel=1e-6)
    assert centripetal_force(2, '?', 1, 18) == pytest.approx(3, rel=1e-6)
    assert centripetal_force(2, 3, '?', 18) == pytest.approx(1, rel=1e-6)
    assert centripetal_force(2, 3, 1, '?') == pytest.approx(18, rel=1e-6)
    with pytest.raises(ValueError):
        centripetal_force('?', '?', 1, 10)
def test_electrostatic_force():
    # Electrostatic force tests: F = k * (q1 * q2) / r^2
    assert electrostatic_force('?', 1e-6, 0.01,8.9875517923e-5) == pytest.approx( 1e-12, rel=1e-6)
    assert electrostatic_force(8.9875517923e-5, '?', 0.01,8.9875517923e-5 ) == pytest.approx(1.112e-14)
    assert electrostatic_force(8.9875517923e-5, 1e-6, '?', 8.9875517923e-5) == pytest.approx(94.8, rel=0.0001)
    assert electrostatic_force('?', 1e-6, 0.01, 8.9875517923e-5) == pytest.approx(1e-12)
    with pytest.raises(ValueError):
        electrostatic_force('?', '?', 0.01, 10)
def test_escape_velocity():
    # Escape velocity tests: v = sqrt(2 * G * M / r)
    assert escape_velocity('?', 5.972e24, 6371000) == pytest.approx(11186, rel=1e-4)
    assert escape_velocity(11186, '?', 6371000) == pytest.approx(5.972e24, rel=1e-4)
    assert escape_velocity(11186, 5.972e24, '?') == pytest.approx(6371000, rel=1e-4)

    with pytest.raises(ValueError):
        escape_velocity('?', '?', 6371000)

def test_hookes_law():
    # Hooke's law tests: F = -k * x
    assert Hookes_law('?', 100, 0.5) == pytest.approx(-50, rel=1e-6)
    # Test case 2: Calculate spring constant given force and displacement
    assert Hookes_law(50, '?', 0.5) == pytest.approx(-100, rel=1e-6)
    # Test case 3: Calculate displacement given force and spring constant   
    assert Hookes_law(50, 100, '?') == pytest.approx(-0.5, rel=1e-6)
    # ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        Hookes_law('?', '?', 0.5)
def test_stress():
    # Stress tests: σ = F / A
    assert Stress('?', 100, 10) == 10
    assert Stress(100, '?', 10) == 1000
    assert Stress(100, 100, '?') == 1
    with pytest.raises(ValueError):
        Stress('?', '?', 10)
def test_tension():
    # Tension tests: T = m * g * sin(θ)
    assert Tension('?', 10,9.8 ,30) == 15.116642088983237
    assert Tension(49.03325, '?', 9.8, 30) == 32.43660180043201
    with pytest.raises(ValueError):
        Tension('?', '?', 9.8, 30)
def test_buoyant_force():
    # Buoyant force tests: F_b = ρ * V * g
    assert buoyant_force('?', 1000, 0.1, 9.8) == pytest.approx(980, rel=1e-6)
    assert buoyant_force(980, '?', 0.1, 9.8) == 0.001
    assert buoyant_force(980, 1000, '?', 9.8) == 10
    assert buoyant_force(980, 1000, 0.1, '?') == 9.8
    with pytest.raises(ValueError):
        buoyant_force('?', '?', 0.1, 9.8)
def test_archimedes_principle():
    # Archimedes' priniciple tests: F = m*g
    assert Archimedes_principle('?',10,9.8) == 98
    assert Archimedes_principle(98,'?',9.8) == 10
    assert Archimedes_principle(98,10,'?') == 9.8
    with pytest.raises(ValueError):
        Archimedes_principle('?', '?', 9.8)

def test_Lorentz_force():
    # Lorentz force tests: F = q * (E + v x B)
    assert Lorentz_force('?', 1e-6, 0.01, 5,0.05) ==  5.0005e-06
    assert Lorentz_force(5.005e-06, '?', 0.01, 5,0.05) == 1e-6
    assert Lorentz_force( 5.005e-06,1e-6, '?', 5,0.05) == 0.1
    assert Lorentz_force(5.005e-06, 1e-6, 0.01, '?',0.05) == 5.0045
    with pytest.raises(ValueError):
        Lorentz_force('?', '?', 0.01, 5,0.05)
def test_Lift():
    assert Lift('?', 1.225, 10, 0.5,0.5) == pytest.approx(15.3125,rel=1e-2)
    assert Lift(306.25, '?', 10, 0.5,0.5) == 24.5
    assert Lift(306.25, 1.225, '?', 0.5,0.5) == pytest.approx(44.721,rel=1e-2)
    assert Lift(306.25, 1.225, 10, '?',0.5) == 10
    with pytest.raises(ValueError):
        Lift('?', '?', 10, 0.5,0.5)


