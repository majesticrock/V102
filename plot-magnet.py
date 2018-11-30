import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b

werte = csv_read("csv/mittelwerte-magnet.csv")
xdata = np.zeros(10)
ydata = np.zeros(10)


thetah = 22.5 * (10**(-7))
m_k = 0.5883
r_k = (51.03 * (10**(-3))) / 2

thetak = (2 * m_k * (r_k**2))/5
theta = thetah + thetak

for i in range(10):
    xdata[i] = float(werte[i+1][1])
    ydata[i] = (4 * np.pi**2 * theta)/(float(werte[i+1][2])**2)

x_line = (np.linspace(0.0005, 0.005))
plt.plot(xdata, ydata, ".", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "r-", label="Fit")

print(popt)
print(np.sqrt(pcov[0][0]))
print(np.sqrt(pcov[1][1]))

plt.xlabel(r"$B$ / T")
plt.ylabel(r"$\Gamma$ / $\frac{\symup{kg} \symup{m}^2}{\symup{s}^2}")

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-magnet.pdf")