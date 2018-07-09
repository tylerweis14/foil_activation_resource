import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def hpge_efficiency1(e):
    e = np.log(e)
    eff = (-143.191) + (91.147) * e + (-21.757) * e**2 + (2.279) * e**3 + (-0.089) * e**4
    return np.exp(eff)


def hpge_efficiency(e):
    erg = np.array([0, 60, 86.5, 105.3, 176.3, 427.90, 600.6, 834.8, 1173.2, 1332.5])
    eff = np.array([0, 2.39e-2, 7.5e-2, 9.27e-2, 9.35e-2, 4.77e-2, 3.51e-2, 2.64e-2, 1.87e-2, 1.69e-2])
    efficiency = interp1d(erg, eff, fill_value='extrapolate')
    return efficiency(e)


if __name__ == '__main__':
    x = np.linspace(0, 2000, 2000)
    y = hpge_efficiency(x)
    y1 = hpge_efficiency1(x)
    plt.plot(x, y, x, y1)
    plt.ylim(0)
