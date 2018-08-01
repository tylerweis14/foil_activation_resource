'''
Theoretical Results for the 6_25_18 irradiation.
'''
import numpy as np
from wand import Wand
import pickle


def run(rerun_all):

    try:
        with open('theoretical_6_25_18.txt', 'rb') as F:
            data = pickle.load(F)
    except:
        data = {}
    ###############################################################################
    #                                gold
    ###############################################################################

    if False or rerun_all:
        wand = Wand()
        wand.name = 'gold'
        wand.mat = 'Au'
        wand.cd = False
        wand.masses = np.array([2.5, 2.7, 3.2, 2.5])  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600*24*4  # s
        wand.counting_time = 60
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    ###############################################################################
    #                                indium
    ###############################################################################
    if True or rerun_all:
        wand = Wand()
        wand.name = 'indium'
        wand.mat = 'In'
        wand.cd = False
        abundance = 0.9572
        masses = np.array([1.7, 1.5, 1.4, 1.6]) * abundance
        wand.masses = masses  # mg
        wand.t_i = 60  # s
        wand.t_w = 8*3600 + 40*60  # s
        wand.counting_time = 60
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    ###############################################################################
    #                                gold (cd)
    ###############################################################################
    if False or rerun_all:
        wand = Wand()
        wand.name = 'gold'
        wand.mat = 'Au'
        wand.cd = True
        wand.masses = np.array([3.9, 3.3, 3.4, 3.9])  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600*2 + 40*60  # s
        wand.counting_time = 300
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
        wand.masses = np.array([0.3, 0.2, 0.1, 0.2])  # mg
        wand.t_i = 3600  # s
        wand.t_w = 354870  # s
        wand.counting_time = 3600
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    # dump data
    with open('theoretical_6_25_18.txt', 'wb') as F:
        pickle.dump(data, F)

if __name__ == '__main__':
    run(True)

with open('theoretical_6_25_18.txt', 'rb') as F:
    data = pickle.load(F)
