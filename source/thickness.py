'''
Simple script used to calculate desired foil thicknesses.
'''
from numpy import pi
from reaction import foils


def calc_thickness(rho, thickness):
    r = 0.11  # cm
    return rho * (pi * r**2) * thickness * 1000


mass = calc_thickness(foils['Mo'].rho, 0.01)
print(mass)
