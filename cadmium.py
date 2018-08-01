'''
Housed the cadmium function.
'''

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt


def extract(xs_string):
    xs_erg, xs_vals = np.loadtxt('xs/' + xs_string, delimiter=',', skiprows=1, unpack=True)
    f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
    return f


# cadmium
Na = 6.0221409E23  # atoms / mol
cd_thickness = 0.05
Cd = {}
Cd['M'] = 112.411  # g/mol
Cd['rho'] = 8.69  # g/cm3

cd_xs_data = [extract('48-Cd-106(n,total).txt'),
              extract('48-Cd-108(n,total).txt'),
              extract('48-Cd-110(n,total).txt'),
              extract('48-Cd-111(n,total).txt'),
              extract('48-Cd-112(n,total).txt'),
              extract('48-Cd-113(n,total).txt'),
              extract('48-Cd-114(n,total).txt'),
              extract('48-Cd-116(n,total).txt')]

cd_weights = [0.0125, 0.0089, 0.1249, 0.1280, 0.2413, 0.1222, 0.2873, 0.0749]


def cd(e):
    xs = 0
    for isotope in range(len(cd_weights)):
        xs += cd_weights[isotope] * cd_xs_data[isotope](e)
    return xs


def cadmium(e):
    term = ((Cd['rho'] * Na) / Cd['M']) * cd_thickness * 1E-24
    factor = np.exp(-term * cd(e) * 5)
    return factor

if __name__ == '__main__':
    plt.figure(95)
    x = np.logspace(-5, 9, 1000)
    y = cadmium(x)
    plt.plot(x, y)
    plt.xscale('log')
    plt.yscale('log')
