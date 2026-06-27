"""
Thermodynamics module for vectoriumPy.

This module provides functions and classes for thermodynamics calculations, including:
- First Law of Thermodynamics
- Entropy
- Enthalpy
- Gibbs free energy
- Helmholtz Free Energy 
- Ideal Gas Law
"""
def first_law_thermodynamics(U, Q, W):
   """Calculate the change in internal energy (ΔU) using the first law.

   ΔU = Q - W

   Parameters
   ----------
   U : float or str
      Internal energy 
   Q : float or str
      Heat added to the system
   W : float or str
      Work done by the system

   Returns
   -------
   float
      The computed unknown value.
   """
   known = [U, Q, W].count(None)
   if known > 1:
      raise ValueError("At least two parameters must be provided.")

   if U is None:
      U = Q - W
      return U
   if Q is None:
      Q = U + W
      return Q
   if W is None:
      W = Q - U
      return W
 
def entropy(Q, T, ΔS):
   """Compute entropy change ΔS = Q / T.

   Parameters
   ----------
   Q : float or str
      Heat added (use None for unknown)
   T : float or str
      Absolute temperature in K
   ΔS : float or str
      Entropy change

   Returns
   -------
   float
      Computed unknown value.
   """
   known_missing = [Q, T, ΔS].count(None)
   if known_missing > 1:
      raise ValueError("At least two parameters must be provided.")

   if T != None and T <= 0:
      raise ValueError("Temperature must be greater than zero.")

   if ΔS is None:
      ΔS = Q / T
      return ΔS
   if Q is None:
      Q = ΔS * T
      return Q
   if T is None:
      T = Q / ΔS
      return T

def enthalpy(H, U, P, V):
   """Compute enthalpy H = U + P*V.

   Parameters
   ----------
   H : float or str
      Enthalpy (use None for unknown)
   U : float or str
      Internal energy
   P : float or str
      Pressure
   V : float or str
      Volume

   Returns
   -------
   float
      Computed unknown value.
   """
   known = [H, U, P, V].count(None)
   if known > 1:
      raise ValueError("At least two parameters must be provided.")

   if H is None:
      H = U + P * V
      return H
   if U is None:
      U = H - P * V
      return U
   if P is None:
      P = (H - U) / V
      return P
   if V is None:
      V = (H - U) / P
      return V
 
def Gibbs_free_energy(G, H, T, S):
      """Compute Gibbs free energy G = H - T*S.

      Parameters
      ----------
      G : float or str
            Gibbs free energy
      H : float or str
            Enthalpy
      T : float or str
            Temperature (K)
      S : float or str
            Entropy

      Returns
      -------
      float
            Computed unknown value.
      """
      known = [G, H, T, S].count(None)
      if known > 1:
            raise ValueError("At least two parameters must be provided.")
      if T != None and T <= 0:
            raise ValueError("Temperature must be greater than zero.")

      if G is None:
            G = H - T * S
            return G
      if H is None:
            H = G + T * S
            return H
      if T is None:
            T = (H - G) / S
            return T
      if S is None:
            S = (H - G) / T
            return S

def Helmholtz_free_energy(A, U, T, S):
   """Compute Helmholtz free energy A = U - T*S.

   Parameters
   ----------
   A : float or str
      Helmholtz free energy
   U : float or str
      Internal energy
   T : float or str
      Temperature (K)
   S : float or str
      Entropy

   Returns
   -------
   float
      Computed unknown value.
   """
   known = [A, U, T, S].count(None)
   if known > 1:
      raise ValueError("At least two parameters must be provided.")
   if T !=None and T <= 0:
      raise ValueError("Temperature must be greater than zero.")

   if A is None:
      A = U - T * S
      return A
   if U is None:
      U = A + T * S
      return U
   if T is None:
      T = (U - A) / S
      return T
   if S is None:
      S = (U - A) / T
      return S

def ideal_gas_law(P, V, n, T, R):
   """Ideal gas law PV = nRT; solve for the unknown marked with None.

   Parameters
   ----------
   P, V, n, T, R : float or str
      Use None for the unknown parameter.

   Returns
   -------
   float
      Computed unknown value.
   """
   known = [P, V, n, T, R].count(None)
   if known > 1:
      raise ValueError("At least two parameters must be provided.")

   if T != None and T <= 0:
      raise ValueError("Temperature must be greater than zero.")

   if P is None:
      P = n * R * T / V
      return P
   if V is None:
      V = n * R * T / P
      return V
   if n is None:
      n = P * V / (R * T)
      return n
   if R is None:
      R = P * V / (n * T)
      return R
   if T is None:
      T = P * V / (n * R)
      return T
def Latent_Heat(Q,m,L):
   """
   calculates the total thermal energy absorbed or released during a phase change at a constant temperature.
   Q = m*L
   """
   knows=[Q,m,L].count(None)
   if knows >1:
      raise ValueError('Provide at least 2 values ')
   
   if Q is None:
       Q = m*L
       return Q   
   elif m ==None:
      m = Q/L
      return m
   elif L is None:
      L = Q/m
      return L
  
# More functions will be added in the future.