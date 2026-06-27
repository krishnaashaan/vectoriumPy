"""
This module contains funtions for energy calculations in vectoriumPy.
"""
import numpy as np

def Kinetic_energy(KE,m,v):
    '''
    This function calculates the kinetic energy (KE) of an object given its mass (m) and velocity (v).
    KE = 0.5 * m * v^2
    parameters:
    KE(float):Kinetic energy (J)
    m(float):Mass of the object (kg)
    v(float):Velocity of the object (m/s)
    '''
    values = [KE,m,v].count(None)
    if values > 1:
        raise ValueError("Please provide values for both mass (m) and velocity (v).")
    if KE is None:
        KE = 0.5 * m * v**2
        return KE
    elif m is None:
        m = 2 * KE / v**2
        return m
    elif v is None:
        v = (2 * KE / m)**0.5
        return v
    
def Potential_energy(PE,m,g,h):
    """
    this function calculates the potential energy (PE) of an object given its mass (m), gravitational acceleration (g), and height (h).
    PE = m * g * h
    parameters:
    PE(float):Potential energy (J)
    m(float):Mass of the object (kg)
    g(float):Gravitational acceleration (m/s^2)
    h(float):Height of the object (m)
    """
    values = [PE,m,g,h].count(None)
    g = 9.8 
    if values > 1:
        raise ValueError("Please provide values for all parameters.")
    if PE is None:
        PE = m * g * h
        return PE
    elif m is None:
        m = PE / (g * h)
        return m
    elif g is None:
        g = PE / (m * h)
        return g
    elif h is None:
        h = PE / (m * g)
        return h
    
def Mechanical_energy(ME,KE,PE):
    """
    This function calculates the mechanical energy (ME) of an object given its kinetic energy (KE) and potential energy (PE).
    ME = KE + PE
    parameters:
    ME(float):Mechanical energy (J)
    KE(float):Kinetic energy (J)
    PE(float):Potential energy (J)
    """
    values = [ME,KE,PE].count(None)
    if values > 1:
        raise ValueError("Please provide values for both kinetic energy (KE) and potential energy (PE).")
    if ME is None:
        ME = KE + PE
        return ME
    elif KE is None:
        KE = ME - PE
        return KE
    elif PE is None:
        PE = ME - KE
        return PE
    
def Work(F,d,θ,W):
    """
    This function calculates work done (W) using Force(F), displacement(d) and angle of application(θ).
    W = F * d * cos(θ)"""
    
    values = [F,d,θ,W].count(None)
    if values > 1:
        raise ValueError("Please provide values for force (F), displacement (d), and angle of application (θ).")
    if W is None:
        W = F * d*np.cos(np.radians(θ))
        return W
    elif F is None:
        F = W/(d * np.cos(np.radians(θ)))
        return F
    elif d is None:
        d = W/(F * np.cos(np.radians(θ)))
        return d
    elif θ is None:
        θ = np.degrees(np.arccos(W/(F * d)))
        return θ
        
def Power(P,W,t):
    """
    This function calculates power (P) given work done (W) and time taken (t).
    P = W/t
    parameters:
    P(float):Power (W)
    W(float):Work done (J)
    t(float):Time taken (s)
    """
    values = [P,W,t].count(None)
    if values > 1:
        raise ValueError("Please provide values for both work done (W) and time taken (t).")
    if P is None:
        P = W/t
        return P
    elif W is None:
        W = P*t
        return W
    elif t is None:
        t = W/P
        return t

def Elastic_potential_energy(EPE,k,x):
    """
    This function calculates elastic potential energy stored in a spring.
    EPE = 0.5 * k * x^2
    parameters:
    EPE(float): Elastic potential energy (J)
    k(float): Spring constant (N/m)
    x(float): Extension or compression (m)
    """
    values = [EPE,k,x].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (EPE, k, x).")
    if EPE is None:
        return 0.5 * k * x**2
    elif k is None:
        return 2 * EPE / x**2
    elif x is None:
        return (2 * EPE / k)**0.5

def Efficiency(η,useful_energy,total_energy):
    """
    This function calculates efficiency as a percentage.
    η = (useful_energy / total_energy) * 100
    parameters:
    η(float): Efficiency (%)
    useful_energy(float): Useful output energy (J)
    total_energy(float): Total input energy (J)
    """
    values = [η,useful_energy,total_energy].count(None)
    if values > 1:
        raise ValueError("Please provide values for at least two of the parameters (η, useful_energy, total_energy).")
    if total_energy == 0:
        raise ZeroDivisionError("Total energy cannot be zero.")
    if η is None:
        return (useful_energy / total_energy) * 100
    elif useful_energy is None:
        return (η / 100) * total_energy
    elif total_energy is None:
        return (useful_energy * 100) / η

## More functions will be added in future updates.
