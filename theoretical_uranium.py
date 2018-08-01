'''
Theoretical Results for the Uranium irradiation.
'''
import numpy as np
from wand import Wand
import pickle

dataname = 'theoretical_uranium.txt'


def run(rerun_all):

    try:
        with open(dataname, 'rb') as F:
            data = pickle.load(F)
    except:
        data = {}
    ###############################################################################
    #                                rhodium
    ###############################################################################

    if True or rerun_all:
        wand = Wand()
        wand.name = 'uranium'
        wand.mat = 'U'
        wand.cd = False
        wand.masses = np.array([0.5, 0.5, 0.5, 0.5])  # mg
        wand.t_i = 3600  # s
        wand.t_w = 3600*24*2  # s
        wand.counting_time = 3600
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    # dump data
    with open(dataname, 'wb') as F:
        pickle.dump(data, F)

if __name__ == '__main__':
    run(True)

    with open(dataname, 'rb') as F:
        data = pickle.load(F)

    for key, val in data.items():
        counts = val.peak_area
        print('{:>6}  {:4.2e}  {:5.4f}'.format(key, counts, np.sqrt(counts) / counts))
