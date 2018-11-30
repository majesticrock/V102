import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

thetah = 22.5 * 10**(-7)
m_k = ufloat(0.5883, 0.0235 * 10**(-3))
r_k = (ufloat(51.03, 0.0204) * 10**(-3)) / 2

thetak = (2 * m_k * r_k**2)/5

print(thetak)
theta = thetah + thetak
print(theta)