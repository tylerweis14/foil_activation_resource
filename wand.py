from activity import activity_calc
import numpy as np
from tex_single_foil import write_single_foil
from foil import Foil


class Wand(object):
    '''
    This is a wand.
    '''
    def __init__(self, name, mat, masses, t_i, t_w, counting_time, P, detector, source, foil_library, experimentname):
        self.name = name
        self.mat = mat
        self.foil_library = foil_library
        self.foil = self.foil_library[self.mat]
        self.cd = True if mat[-2:] == 'Cd' else False
        if type(masses) in [float, int]:
            self.masses = np.repeat(masses, 4)
        elif masses == 'estimate':
            self.masses = self.estimate_masses()
        else:
            self.masses = masses
        self.t_i = t_i
        self.t_w = t_w
        self.counting_time = counting_time
        self.detector = detector
        self.source = source
        self.P = P
        self.experimentname = experimentname
        self.t_f = self.calc_t_f()

    def estimate_masses(self):
        return np.repeat((self.foil.rho / 7.31) * 2.1, 4)

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
            count, act_rem, act_count = activity_calc(self.foil, m, self.P,
                                                      self.t_i, t_ci, t_cf, self.t_f, self.detector, self.source,
                                                      plotname='plot/{}{}_activity.png'.format(self.mat.lower(), i + 1),
                                                      node=i+1, experimentname=self.experimentname)
            self.removal_activity += act_rem
            self.counting_activities[i] = act_count
            self.counts[i] = count
        print('Removal Activity:  {:4.2e}  uCi'.format(self.removal_activity))
        if write:
            write_single_foil(self.foil_library[self.mat], self.P, self.t_i, self.t_w, self.counting_time,
                              self.removal_activity, self.counting_activities, self.masses,
                              self.counts, self.experimentname)

    def package_data(self):
        data = {}
        cd_str = ''
        if self.cd:
            cd_str = '_cd'
        for i in range(1, 5):
            data[self.mat.lower() + cd_str + str(i)] = Foil(self.counts[i-1], np.sqrt(self.counts[i-1]),
                                                            self.counting_activities[i-1], 0, self.counting_time)
        return data
