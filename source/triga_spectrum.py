import numpy as np
from scipy.interpolate import interp1d

# script reads nodal data and produces input spectrum

port = 'C'

data = np.load('mpfd_nodal_data.npy')[()]

power = 100  # kW(th)


# for general spectrum
node_data = data[port + '2']
erg, values, err = node_data.T
midpoints = (erg[1:] + erg[:-1]) / 2
widths = erg[1:] - erg[:-1]
values = (values[1:] / widths) * power

triga_spectrum = interp1d(midpoints, values, bounds_error=False, fill_value=0)

# for ndal spectra
nodal_spectra = [-1]
for i in range(1, 5):
    node_data = data[port + str(i)]
    erg, values, err = node_data.T
    midpoints = (erg[1:] + erg[:-1]) / 2
    widths = erg[1:] - erg[:-1]
    values = (values[1:] / widths) * power
    nodal_spectra.append(interp1d(midpoints, values, bounds_error=False, fill_value=0))
