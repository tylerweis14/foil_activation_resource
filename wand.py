from activity import activity_calc
from cross_sections import foils
import numpy as np


cases = [0]
###############################################################################
#                                gold
###############################################################################
if 0 in cases:
    print('\n')
    print('Gold')
    mat = 'Au'
    cd_cov = False
    masses = np.array([5.0, 4.35, 4.30, 4.37])  # mg
    t_i = 45  # s
    t_w = 345  # s
    counting_time = 300
    t_f = 3600  # s
    P = 100  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                                indium
###############################################################################
if 1 in cases:
    print('\n')
    print('Indium')
    mat = 'In'
    cd_cov = False
    masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
    t_i = 60  # s
    t_w = 460  # s
    counting_time = 300
    t_f = 5000  # s
    P = 1.0  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                                gold (cd)
###############################################################################
if 2 in cases:
    print('\n')
    print('Gold w/ Cadmium')
    mat = 'Au'
    cd_cov = True
    masses = np.array([5.0, 4.35, 4.30, 4.37])  # mg
    t_i = 45  # s
    t_w = 345  # s
    counting_time = 300
    t_f = 3600  # s
    P = 100  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}cd_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                                indium (cd)
###############################################################################
if 3 in cases:
    print('\n')
    print('Indium w/ Cadmium')
    mat = 'In'
    cd_cov = True
    masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
    t_i = 60  # s
    t_w = 460  # s
    counting_time = 300
    t_f = 5000  # s
    P = 1.0  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}cd_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                               rhodium
###############################################################################
if 4 in cases:
    print('\n')
    print('Rhodium')
    mat = 'Rh'
    cd_cov = False
    masses = np.array([0.7, 0.55, 0.5, 0.55])  # mg
    t_i = 600  # s
    t_w = 5600  # s
    counting_time = 600
    t_f = 10000  # s
    P = 100  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                              aluminum
###############################################################################
if 5 in cases:
    print('\n')
    print('Aluminum')
    mat = 'Al'
    cd_cov = False
    masses = np.array([0.3, 0.2, 0.1, 0.2])  # mg
    t_i = 3600  # s
    t_w = 5400  # s
    counting_time = 1800
    t_f = 13000  # s
    P = 250  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                              uranium
###############################################################################
if 6 in cases:
    print('\n')
    print('Uranium')
    mat = 'U'
    cd_cov = False
    masses = np.array([5.0, 4.35, 4.30, 4.37])  # assumed the same as au for now
    t_i = 600  # s
    t_w = 5600  # s
    counting_time = 600
    t_f = 10000  # s
    P = 100  # kW(th)

    removal_activity = 0
    for i, m in enumerate(masses):
        t_ci = t_w + (i * counting_time)
        t_cf = t_w + ((i + 1) * counting_time)
        counts, act_rem = activity_calc(foils[mat], m, P, t_i, t_ci, t_cf, t_f,
                                        cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
        removal_activity += act_rem
    print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))
