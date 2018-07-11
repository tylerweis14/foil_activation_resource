'''
Houses the reaction object.
'''
from scipy.interpolate import interp1d
import numpy as np

foils = {}


class Reaction(object):
    '''
    Docstring goes here.
    '''
    def __init__(self, reactant, reaction, byproduct, cd, M, rho, xs_file, halflife, abundance, erg, BR, cost):
        self.reactant = reactant
        self.reaction = reaction
        self.byproduct = byproduct
        self.cd = cd
        self.M = M
        self.rho = rho
        self.xs_file = xs_file
        self.halflife = halflife
        self.decay_constant = np.log(2) / self.halflife
        self.abundance = abundance
        self.erg = erg
        self.BR = BR
        self.cost = cost
        self.func, self.region = self.extract()
        self.label, self.plotname = self.parse_text()
        self.classification = 'threshold' if self.region[0] > 1e4 else 'resonance'

    def extract(self):
        xs_erg, xs_vals = np.loadtxt('xs/' + self.xs_string, delimiter=',', skiprows=1, unpack=True)
        f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
        region = xs_erg[0], xs_erg[-1]
        return f, region

    def parse_text(self):
        reac, r_num = self.reactant.split('-')
        bypr, b_num = self.reactant.split('-')
        cd_s = ' Cd' if self.cd else ''
        label = '$^{}${}({})$^{}${}{}'.format(r_num, reac, self.reaction, b_num, reac, cd_s)
        cd_s = '_Cd' if self.cd else ''
        plotname = '{}({}){}{}'.format(self.reactant, self.reaction, self.byproduct, cd_s)
        return label, plotname

foils['In'] = Reaction('In-115', 'n,gamma', 'In-116', False, 114.818, 7.31, '49-In-115(n,&gamma;).txt', 54*60, 1.0, 1293, 0.8, -1)
foils['InCd'] = Reaction('In-115', 'n,gamma', 'In-116', True, 114.818, 7.31, '49-In-115(n,&gamma;).txt', 54*60, 1.0, 1293, 0.8, -1)
