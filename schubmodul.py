import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

T = ufloat(18.28210, 0.00009)
m_k = ufloat(0.5833, 23.5 * 10**(-3))
r_k = ufloat(51.03/2 * 10**(-3), 2.04/2 * 10**(-3))
L = 0.665
R = (170 / 2) * 10**(-6)

G = (16/5) * np.pi * (m_k * (r_k**2) * L) / ((T**2) * (R**4))

print(G)