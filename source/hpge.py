import numpy as np
import matplotlib.pyplot as plt


def hpge_efficiency(e):
    e = np.log(e)
    eff = (-143.191) + (91.147) * e + (-21.757) * e**2 + (2.279) * e**3 + (-0.089) * e**4
    return np.exp(eff)


if __name__ == '__main__':
    x = np.linspace(0, 2000)
    y = hpge_efficiency(x)
    plt.plot(x, y)
