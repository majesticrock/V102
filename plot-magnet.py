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

#werte = csv_read("csv/mittelwerte-magnet.csv")
xdata = np.zeros(100)
ydata = np.zeros(100)

content = csv_read("csv/magnet0-5.csv")
for j in range(10):
    ydata[j] = float(content[j+1][0])
    xdata[j] = 0.5

for i in range(4):
    content = csv_read("csv/magnet" + str(i+1) + "-0.csv")
    for j in range(10):
        ydata[j + 10 + (i*20)] = float(content[j+1][0])
        xdata[j + 10 + (i*20)] = i+1
    content = csv_read("csv/magnet" + str(i+1) + "-5.csv")
    for j in range(10):
        ydata[j + 20 + (i*20)] = float(content[j+1][0])
        xdata[j + 20 + (i*20)] = i+1 + 0.5

content = csv_read("csv/magnet5-0.csv")
for j in range(10):
    ydata[j + (4*20) + 10] = float(content[j+1][0])
    xdata[j + (4*20) + 10] = 5


x_line = (np.linspace(0.5, 5))
ydata = 1 / (ydata**2)
mu_0 = 4 * np.pi * 10**(-7)
xdata = (4/5)**(3/2) * (mu_0 * 80 * xdata)/(72*10**(-3))
x_line = (4/5)**(3/2) * (mu_0 * 80 * x_line)/(72*10**(-3))


plt.plot(xdata, ydata, ".", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "r-", label="Fit")

print(popt)
print(np.sqrt(pcov[0][0]))
print(np.sqrt(pcov[1][1]))

plt.xlabel(r"$B_H$ / T")
plt.ylabel(r"$\frac{1}{T^2}$ / $\frac{1}{\symup{s}^2}")

plt.legend()
plt.tight_layout()
plt.savefig("build/plot-magnet.pdf")

#for i in range(10):
#    xdata[i] = float(werte[i+1][1])
#    ydata[i] = 1/(float(werte[i+1][2])**2)
#
#x_line = (np.linspace(0.0005, 0.005))
#plt.plot(xdata, ydata, ".", label="Messwerte")
#popt, pcov = curve_fit(func, xdata, ydata)
#plt.plot(x_line, func(x_line, *popt), "r-", label="Fit")
#
#print(popt)
#print(np.sqrt(pcov[0][0]))
#print(np.sqrt(pcov[1][1]))
#
#plt.xlabel(r"$B$ / T")
#plt.ylabel(r"$\Gamma$ / $\frac{\symup{kg} \symup{m}^2}{\symup{s}^2}")
#
#plt.legend()
#plt.tight_layout()
#plt.savefig("build/plot-magnet.pdf")