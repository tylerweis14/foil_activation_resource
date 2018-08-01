'''
Theoretical Results for the 7_11_18 irradiation.
'''
import numpy as np
from wand import Wand
import pickle

dataname = 'theoretical_7_11_18.txt'


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
        wand.name = 'rhodium'
        wand.mat = 'Rh'
        wand.cd = False
        stack_height = 6
        wand.masses = np.array([1.1, 1.1, 1.1, 1.1]) * stack_height  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600*2  # s
        wand.counting_time = 600
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    ###############################################################################
    #                              aluminum
    ###############################################################################
    if False or rerun_all:
        wand = Wand()
        wand.name = 'aluminum'
        wand.mat = 'Al'
        wand.cd = False
        stack_height = 5
        masses = np.array([0.6, 0.6, 0.6, 0.6]) * stack_height
        wand.masses = masses  # mg
        wand.t_i = 3600 * 1  # s
        wand.t_w = 3600*24*2  # s
        wand.counting_time = 3600
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    ###############################################################################
    #                                indium (cd)
    ###############################################################################
    if False or rerun_all:
        wand = Wand()
        wand.name = 'indium'
        wand.mat = 'In'
        wand.cd = True
        wand.masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
        wand.t_i = 30  # s
        wand.t_w = 8*3600 + 40*60  # s
        wand.counting_time = 300
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
