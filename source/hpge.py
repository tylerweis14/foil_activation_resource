import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def hpge_efficiency1(e):
    e = np.log(e)
    eff = (-143.191) + (91.147) * e + (-21.757) * e**2 + (2.279) * e**3 + (-0.089) * e**4
    return np.exp(eff)


x = np.array([60, 86.5, 105.3, 176.3, 427.90, 600.6, 834.8, 1173.2, 1332.5])
y = np.array([2.39e-2, 7.5e-2, 9.27e-2, 9.35e-2, 4.77e-2, 3.51e-2, 2.64e-2, 1.87e-2, 1.69e-2])


def efficiency(erg, a, b, c, d, e):
    erg = np.log(erg)
    eff = a + b * erg + c * erg**2 + d * erg**3 + e * erg**4
    return np.exp(eff)

p0 = [-143.191, 91.147, -21.757, 2.279, -0.089]
coeffs = curve_fit(efficiency, x, y, p0)
print(coeffs[0])


def hpge_efficiency(erg):
    return efficiency(erg, -2.48945787e+02, 1.67284939e+02, -4.21090055e+01, 4.67244596e+00, -1.93763734e-01)

if __name__ == '__main__':
    x = np.linspace(0, 2000, 2000)
    y = hpge_efficiency(x)
    y1 = hpge_efficiency1(x)
    plt.plot(x, y, x, y1)
    plt.ylim(0)
