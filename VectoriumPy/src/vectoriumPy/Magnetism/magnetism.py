"""
This module contains the  calculations related to magnetism  for vectoriumPy
"""
import numpy as np 

def magnetic_force(F,q,v,B,θ):
    """
    Calculates the magnetic force(F) acting on a charged particle moving through a magnetic field
    formula: F = q*v*B*sinθ

    parameters:
    F(float): Force acting on a charged particle moving through a magnetic field(N)
    q(float): charge of the particle(C)
    v(float): velocity of the particle(m/s)
    B(float): magnetic field strength(T)
    θ(float): the angle between velocity and the field.
    """
    unknowns = [F,q,v,B,θ].count(None)
    θ_rad = np.deg2rad(θ)
    if unknowns >1:
        raise ValueError("Please provide values for all but one parameter")
    if F is None:
        F = q*v*B*np.sin(θ_rad)
        return F
    elif q is None:
        q = F/(v*B*np.sin(θ_rad))
        return q
    elif v is None:
        v = F/(q*B*np.sin(θ_rad))
        return v
    elif B is None:
        B = F/(q*v*np.sin(θ_rad))
        return B
def magnetic_flux(Φ,B,A,θ):
    """
    Calculates magnetic flux(measures the quantity of magnetic field lines penetrating a surface)
    formula Φ = B*A*cosθ
    parameters:
    Φ(float): Magnetic Flux (SI unit: Weber, Wb)
    B(float): Magnetic Field Strength (Tesla, T)
    A(float): Area of the surface (m²)
    θ(float):Angle between the magnetic field B and the normal vector to the surface
    """
    unknows = [Φ,B,A,θ].count(None)
    θ_rad = np.deg2rad(θ)
    if unknows>1:
        raise ValueError("Please provide values for all but one parameter")
    elif Φ is None:
       Φ =B*A*np.cos(θ_rad).round(2)
       return Φ
    elif B is None:
        B = Φ/(A*np.cos(θ_rad))
        B= B.round(2)
        return B
    elif A is None:
        A = Φ/(B*np.cos(θ_rad))
        A= A.round(2)
        return A 
    

        

    