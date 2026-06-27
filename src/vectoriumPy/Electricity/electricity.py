"""
Module for electricity in vectoriumPy
"""
import numpy as np

def ohms_law(V, I, R):
    """
    Function to calculate the relationship between voltage, current, and resistance in an electrical circuit.

    Parameters:
    V (float): Voltage (volts)
    I (float): Current (amperes)
    R (float): Resistance (ohms)

    Returns:
    float: The calculated value based on the provided parameters.
    """
    values = [V,I,R].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (V, I, R).")
    if V is None:
        V = I * R
        return V
    elif I is None:
        I = V / R
        return I
    elif R is None:
        R  = V / I
        return R 
def electric_power(P, V, I):
    """
    Function to calculate the relationship between power, voltage, and current in an electrical circuit.

    Parameters:
    P (float): Power (watts)
    V (float): Voltage (volts)
    I (float): Current (amperes)

    Returns:
    float: The calculated value based on the provided parameters.
    """
    values = [P,V,I].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (P, V, I).")
    if P is None:
        P = V * I
        return P
    elif V is None:
        V = P / I
        return V
    elif I is None:
        I = P / V
        return I
def electric_energy(E, P, t):
    """
    Function to calculate the relationship between energy, power, and time in an electrical circuit.

    Parameters:
    E (float): Energy (joules)
    P (float): Power (watts)
    t (float): Time (seconds)

    Returns:
    float: The calculated value based on the provided parameters.
    """
    values = [E,P,t].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (E, P, t).")
    if E is None:
        E = P * t
        return E
    elif P is None:
        P = E / t
        return P
    elif t is None:
        t = E / P
        return t
def electric_capacitance(C, Q, V):
    """
    Function to calculate the relationship between capacitance, charge, and voltage in an electrical circuit.

    Parameters:
    C (float): Capacitance (farads)
    Q (float): Charge (coulombs)
    V (float): Voltage (volts)

    Returns:
    float: The calculated value based on the provided parameters.
    """
    values = [C,Q,V].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (C, Q, V).")
    if C is None:
        C = Q / V
        return C
    elif Q is None:
        Q = C * V
        return Q
    elif V is None:
        V = Q / C
        return V
def electric_resonance(f, L, C):
    """
    Function to calculate the relationship between frequency, inductance, and capacitance in an electrical circuit.

    Parameters:
    f (float): Frequency (hertz)
    L (float): Inductance (henrys)
    C (float): Capacitance (farads)

    Returns:
    float: The calculated value based on the provided parameters.
    """
    values = [f,L,C].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (f, L, C).")
    if f is None:
        from decimal import Decimal, getcontext
        getcontext().prec = 50
        pi_dec = Decimal(str(np.pi))
        L_dec = Decimal(str(L))
        C_dec = Decimal(str(C))
        f_dec = Decimal(1) / (Decimal(2) * pi_dec * (L_dec * C_dec).sqrt())
        return float(str(f_dec))
    elif L is None:
        L = 1 / ((2 * np.pi * f) ** 2 * C)
        return float(L)
    elif C is None:
        C = 1 / ((2 * np.pi * f) ** 2 * L)
        return float(C)
def Joules_law_of_heating(I,R,T,H):
    """
    Statement: The heating effect of current is proportional to the resistance, the square of the current, and the duration of current flow.
    Formula: H = I^2 * R * T
    parameters:
 H (float): The heat produced in Joules (J).
 I (float): The electric current in Amperes (A).
 R (float): The resistance in Ohms (Ω).
 T (float): The time in seconds (s).
    """
    values = [H,I,R,T].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (H, I, R, T).")
    if H is None:
        H = I**2 * R * T
        return H
    elif I is None:
        I = (H / (R * T)) ** 0.5
        return I
    elif R is None:
        R = H / (I**2 * T)
        return R
    elif T is None:
        T = H / (I**2 * R)
        return T

## Additional functions will be added in future updates.