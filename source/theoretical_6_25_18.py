'''
Theoretical Results for the 6_25_18 irradiation.
'''
from activity import activity_calc
from cross_sections import foils
import numpy as np
from tex_single_foil import write_single_foil
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
        wand.masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
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
        wand.masses = np.array([2.5, 2.7, 3.2, 2.5])  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600*1  # s
        wand.counting_time = 60
        wand.P = 100  # kW(th)
        wand.irradiate(False)
        data.update(wand.package_data())

    if False or rerun_all:
        print('\n')
        name = 'gold'
        print('{} w/ Cadmium'.format(name.capitalize()))
        mat = 'Au'
        cd_cov = True
        masses = np.array([5.0, 4.35, 4.30, 4.37])  # mg
        t_i = 60  # s
        t_w = 3600*1  # s
        counting_time = 300
        t_f = 3600*2  # s
        P = 100  # kW(th)

        removal_activity = 0
        counting_activities = np.zeros(4)
        for i, m in enumerate(masses):
            t_ci = t_w + (i * counting_time)
            t_cf = t_w + ((i + 1) * counting_time)
            counts, act_rem, act_count = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                                       cd_cov, plotname='plot/{}{}cd_activity.png'.format(mat.lower(), i + 1))
            removal_activity += act_rem
            counting_activities[i] = act_count
        print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))
        write_single_foil(name, P, t_i, t_w-t_i, counting_time, removal_activity, counting_activities, masses, mat, True)

    ###############################################################################
    #                                indium (cd)
    ###############################################################################
    if False or rerun_all:
        print('\n')
        name = 'indium'
        print('{} w/ Cadmium'.format(name.capitalize()))
        mat = 'In'
        cd_cov = True
        masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
        t_i = 60  # s
        t_w = 60 + 1*3600  # s
        counting_time = 300
        t_f = 2*3600  # s
        P = 100.0  # kW(th)

        removal_activity = 0
        counting_activities = np.zeros(4)
        for i, m in enumerate(masses):
            t_ci = t_w + (i * counting_time)
            t_cf = t_w + ((i + 1) * counting_time)
            counts, act_rem, act_count = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                                       cd_cov, plotname='plot/{}{}cd_activity.png'.format(mat.lower(), i + 1))
            removal_activity += act_rem
            counting_activities[i] = act_count
        print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))
        write_single_foil(name, P, t_i, t_w-t_i, counting_time, removal_activity, counting_activities, masses, mat, True)

    ###############################################################################
    #                               rhodium
    ###############################################################################
    if False or rerun_all:
        wand = Wand()
        wand.name = 'rhodium'
        wand.mat = 'Rh'
        wand.cd = False
        wand.masses = np.array([0.7, 0.55, .5, .55])  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600 * 1  # s
        wand.counting_time = 600
        wand.P = 100  # kW(th)
        wand.irradiate()

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
    run(False)

with open('theoretical_6_25_18.txt', 'rb') as F:
    data = pickle.load(F)
