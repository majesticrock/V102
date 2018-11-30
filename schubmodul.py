import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

T = ufloat(18.28210, 0.00009)
m_k = ufloat(0.5883, 0.0235 * 10**(-3))
r_k = ufloat(51.03 * 10**(-3), 0.0204 * 10**(-3)) / 2
L = 0.665
R = (170 / 2) * 10**(-6)

G = (16/5) * ((np.pi * m_k * (r_k**2) * L) / ((T**2) * (R**4)))

print(G)

E = ufloat(21 * 10**10, 0.05 * 10**10)

mu = E/(2*G) - 1

print(mu)

Q = (E*G)/(9*G - 3*E)

print(Q)