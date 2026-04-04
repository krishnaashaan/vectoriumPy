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
      Internal energy (use "?" for unknown)
   Q : float or str
      Heat added to the system
   W : float or str
      Work done by the system

   Returns
   -------
   float
      The computed unknown value.
   """
   known = [U, Q, W].count("?")
   if known > 1:
      raise ValueError("At least two parameters must be provided.")

   if U == "?":
      U = Q - W
      return U
   if Q == "?":
      Q = U + W
      return Q
   if W == "?":
      W = Q - U
      return W
 
def entropy(Q, T, ΔS):
   """Compute entropy change ΔS = Q / T.

   Parameters
   ----------
   Q : float or str
      Heat added (use "?" for unknown)
   T : float or str
      Absolute temperature in K
   ΔS : float or str
      Entropy change

   Returns
   -------
   float
      Computed unknown value.
   """
   known_missing = [Q, T, ΔS].count("?")
   if known_missing > 1:
      raise ValueError("At least two parameters must be provided.")

   if T != '?' and T <= 0:
      raise ValueError("Temperature must be greater than zero.")

   if ΔS == "?":
      ΔS = Q / T
      return ΔS
   if Q == "?":
      Q = ΔS * T
      return Q
   if T == "?":
      T = Q / ΔS
      return T

def enthalpy(H, U, P, V):
   """Compute enthalpy H = U + P*V.

   Parameters
   ----------
   H : float or str
      Enthalpy (use "?" for unknown)
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
   known = [H, U, P, V].count("?")
   if known > 1:
      raise ValueError("At least two parameters must be provided.")

   if H == "?":
      H = U + P * V
      return H
   if U == "?":
      U = H - P * V
      return U
   if P == "?":
      P = (H - U) / V
      return P
   if V == "?":
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
      known = [G, H, T, S].count("?")
      if known > 1:
            raise ValueError("At least two parameters must be provided.")
      if T != '?' and T <= 0:
            raise ValueError("Temperature must be greater than zero.")

      if G == "?":
            G = H - T * S
            return G
      if H == "?":
            H = G + T * S
            return H
      if T == "?":
            T = (H - G) / S
            return T
      if S == "?":
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
   known = [A, U, T, S].count("?")
   if known > 1:
      raise ValueError("At least two parameters must be provided.")
   if T !='?' and T <= 0:
      raise ValueError("Temperature must be greater than zero.")

   if A == "?":
      A = U - T * S
      return A
   if U == "?":
      U = A + T * S
      return U
   if T == "?":
      T = (U - A) / S
      return T
   if S == "?":
      S = (U - A) / T
      return S

def ideal_gas_law(P, V, n, T, R):
   """Ideal gas law PV = nRT; solve for the unknown marked with "?".

   Parameters
   ----------
   P, V, n, T, R : float or str
      Use "?" for the unknown parameter.

   Returns
   -------
   float
      Computed unknown value.
   """
   known = [P, V, n, T, R].count("?")
   if known > 1:
      raise ValueError("At least two parameters must be provided.")

   if T != '?' and T <= 0:
      raise ValueError("Temperature must be greater than zero.")

   if P == "?":
      P = n * R * T / V
      return P
   if V == "?":
      V = n * R * T / P
      return V
   if n == "?":
      n = P * V / (R * T)
      return n
   if R == "?":
      R = P * V / (n * T)
      return R
   if T == "?":
      T = P * V / (n * R)
      return T
def Latent_Heat(Q,m,L):
   """
   calculates the total thermal energy absorbed or released during a phase change at a constant temperature.
   Q = m*L
   """
   knows=[Q,m,L].count('?')
   if knows >1:
      raise ValueError('Provide at least 2 values ')
   
   if Q == '?':
       Q = m*L
       return Q   
   elif m =='?':
      m = Q/L
      return m
   elif L == '?':
      L = Q/m
      return L
  
# More functions will be added in the future.