'''
Houses the reaction object.
'''
from scipy.interpolate import interp1d
import numpy as np
from triga_spectrum import triga_spectrum

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
        self.roi = self.calc_roi()

    def extract(self):
        xs_erg, xs_vals = np.loadtxt('xs/' + self.xs_file, delimiter=',', skiprows=1, unpack=True)
        f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
        region = xs_erg[0], xs_erg[-1]
        return f, region

    def parse_text(self):
        reac, r_num = self.reactant.split('-')
        bypr, b_num = self.reactant.split('-')
        cd_s = ' Cd' if self.cd else ''
        label = '$^{{{}}}${}({})$^{{{}}}${}{}'.format(r_num, reac, self.reaction, b_num, reac, cd_s)
        cd_s = '_Cd' if self.cd else ''
        plotname = '{}({}){}{}'.format(self.reactant, self.reaction, self.byproduct, cd_s)
        return label, plotname

    def findroot(self, percentile, func):
        l, r = self.region
        c = np.geomspace(l, r, 3)[1]
        while abs(func(c) - percentile) > 1e-12:
            c = np.geomspace(l, r, 3)[1]
            if percentile < func(c):
                r = c
            else:
                l = c
        return c

    def calc_roi(self):
        edges = np.geomspace(*self.region, 1e6)
        midpoints = (edges[1:] + edges[:-1]) / 2
        widths = (edges[1:] - edges[:-1])
        rectangles = self.func(midpoints) * triga_spectrum(midpoints) * widths
        rectangles = rectangles / np.sum(rectangles)
        cdf_vals = np.cumsum(rectangles)
        cdf = interp1d(midpoints, cdf_vals, fill_value=(rectangles[0], rectangles[-1]))
        l, r = self.findroot(0.05, cdf), self.findroot(0.95, cdf)
        return l, r

foils['In'] = Reaction('In-115', 'n,gamma', 'In-116', False, 114.818, 7.31, '49-In-115(n,&gamma;).txt', 54*60, 0.9572, 1293, 0.8, -1)
foils['InCd'] = Reaction('In-115', 'n,gamma', 'In-116', True, 114.818, 7.31, '49-In-115(n,&gamma;).txt', 54*60, 0.9572, 1293, 0.8, -1)
foils['Mo'] = Reaction('Mo-98', 'n,gamma', 'Mo-98', False, 95.95, 10.28, '42-Mo-98(n,&gamma;).txt', 66*3600, 0.2429, 740, 0.12, -1)
foils['Zn'] = Reaction('Zn-64', 'n,p', 'Cu-64', False, 65.38, 7.14, '30-Zn-64(n,p).txt', 61.9*3600, 0.492, 1345.77, 0.00475, -1)
foils['Cu'] = Reaction('Cu-63', 'n,gamma', 'Cu-64', False, 63.546, 8.96, '29-Cu-63(n,&gamma;).txt', 61.9*3600, 0.6915, 1345.77, 0.00475, -1)
foils['Mg'] = Reaction('Cu-24', 'n,p', 'Na-24', False, 24.305, 1.738, '12-Mg-24(n,p).txt', 15.03*3600, 0.79, 1368.626, 0.999936, -1)
