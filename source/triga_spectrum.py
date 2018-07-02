import numpy as np
from scipy.interpolate import interp1d

# script reads nodal data and produces input spectrum

node = 'C2'

data = np.load('mpfd_nodal_data.npy')[()]

power = 100  # kW(th)


node_data = data[node]
erg, values, err = node_data.T
midpoints = (erg[1:] + erg[:-1]) / 2
widths = erg[1:] - erg[:-1]
values = (values[1:] / widths) * power

triga_spectrum = interp1d(midpoints, values, bounds_error=False, fill_value=0)
