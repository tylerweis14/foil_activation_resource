import numpy as np
from wand import Wand


if True:
    wand = Wand()
    wand.name = 'titanium'
    wand.mat = 'Ti'
    wand.cd = False
    mass = 0.0744 * 0.291 * 71.41 * 1e3
    wand.masses = np.array([mass, mass, mass, mass])  # mg
    wand.t_i = 30*60  # s
    wand.t_w = 3600 * 24 * 7  # s
    wand.counting_time = 60
    wand.P = 100  # kW(th)
    wand.irradiate(False)
