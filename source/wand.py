from activity import activity_calc
import numpy as np
from tex_single_foil import write_single_foil
from foil import Foil
from reaction import foils


class Wand(object):
    '''
    This is a wand.
    '''
    def __init__(self, name, mat, cd, masses, t_i, t_w, counting_time, P, experimentname):
        self.name = name
        self.mat = mat
        self.cd = cd
        self.masses = masses
        self.t_i = t_i
        self.t_w = t_w
        self.counting_time = counting_time
        self.P = P
        self.experimentname = experimentname
        self.t_f = self.calc_t_f()

    def calc_t_f(self):
        return self.t_i + self.t_w + (4 * self.counting_time) + 1

    def irradiate(self, write):
        print('\n')
        print(self.name.capitalize() + ' w/ Cadmium' if self.cd else self.name.capitalize())
        self.removal_activity = 0
        self.counting_activities = np.zeros(4)
        self.counts = np.zeros(4)
        for i, m in enumerate(self.masses):
            t_ci = self.t_w + (i * self.counting_time)
            t_cf = self.t_w + ((i + 1) * self.counting_time)
            count, act_rem, act_count = activity_calc(foils[self.mat], m, self.P,
                                                      self.t_i, t_ci, t_cf, self.t_f, self.cd,
                                                      plotname='plot/{}{}_activity.png'.format(self.mat.lower(), i + 1),
                                                      node=i+1, experimentname=self.experimentname)
            self.removal_activity += act_rem
            self.counting_activities[i] = act_count
            self.counts[i] = count
        print('Removal Activity:  {:4.2e}  uCi'.format(self.removal_activity))
        if write:
            write_single_foil(self.name, self.P, self.t_i, self.t_w, self.counting_time,
                              self.removal_activity, self.counting_activities, self.masses,
                              self.mat, self.counts)

    def package_data(self):
        data = {}
        cd_str = ''
        if self.cd:
            cd_str = '_cd'
        for i in range(1, 5):
            data[self.mat.lower() + cd_str + str(i)] = Foil(self.counts[i-1], np.sqrt(self.counts[i-1]),
                                                            self.counting_activities[i-1], 0, self.counting_time)
        return data


if __name__ == '__main__':
    pass
'''
    ###############################################################################
    #                                gold
    ###############################################################################
    if 0 in cases:
        wand = Wand()
        wand.name = 'gold'
        wand.mat = 'Au'
        wand.cd = False
        wand.masses = np.array([2.5, 2.7, 3.2, 2.5])  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600*24*4  # s
        wand.counting_time = 60
        wand.P = 100  # kW(th)
        wand.irradiate()

    ###############################################################################
    #                                indium
    ###############################################################################
    if 1 in cases:
        wand = Wand()
        wand.name = 'indium'
        wand.mat = 'In'
        wand.cd = False
        wand.masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
        wand.t_i = 60  # s
        wand.t_w = 7*3600 + 20*60  # s
        wand.counting_time = 60
        wand.P = 100  # kW(th)
        wand.irradiate()

    ###############################################################################
    #                                gold (cd)
    ###############################################################################
    if 2 in cases:
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
    if 3 in cases:
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
    if 4 in cases:
        wand = Wand()
        wand.name = 'rhodium'
        wand.mat = 'Rh'
        wand.cd = False
        wand.masses = np.array([0.7, 0.55, .5, .55])  # mg
        wand.t_i = 60  # s
        wand.t_w = 3600*1  # s
        wand.counting_time = 600
        wand.P = 100  # kW(th)
        wand.irradiate()

    ###############################################################################
    #                              aluminum
    ###############################################################################
    if 5 in cases:
        wand = Wand()
        wand.name = 'aluminum'
        wand.mat = 'Al'
        wand.cd = False
        wand.masses = np.array([0.3, 0.2, 0.1, 0.2])  # mg
        wand.t_i = 3600  # s
        wand.t_w = 354870  # s
        wand.counting_time = 3600
        wand.P = 100  # kW(th)
        wand.irradiate()

    ###############################################################################
    #                              uranium
    ###############################################################################

    if 6 in cases:
        wand = Wand()
        wand.name = 'uranium'
        wand.mat = 'U'
        wand.cd = False
        wand.masses = np.array([5.0, 4.35, 4.30, 4.37])  # mg
        wand.t_i = 600  # s
        wand.t_w = 5600  # s
        wand.counting_time = 600
        wand.P = 100  # kW(th)
        wand.irradiate()
'''
