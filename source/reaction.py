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
        bypr, b_num = self.byproduct.split('-')
        cd_s = ' Cd' if self.cd else ''
        reaction = self.reaction if self.reaction not in ['n,gamma', 'n,alpha'] else 'n,$\gamma$' if self.reaction != 'n,alpha' else 'n,$\\alpha$'
        label = '$^{{{}}}${}({})$^{{{}}}${}{}'.format(r_num, reac, reaction, b_num, bypr, cd_s)
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
# foils['InCd'] = Reaction('In-115', 'n,gamma', 'In-116', True, 114.818, 7.31, '49-In-115(n,&gamma;).txt', 54*60, 0.9572, 1293, 0.8, -1)
foils['Mo'] = Reaction('Mo-98', 'n,gamma', 'Mo-99', False, 95.95, 10.28, '42-Mo-98(n,&gamma;).txt', 66*3600, 0.2429, 740, 0.12, -1)
foils['Zn'] = Reaction('Zn-64', 'n,p', 'Cu-64', False, 65.38, 7.14, '30-Zn-64(n,p).txt', 61.9*3600, 0.492, 1345.77, 0.00475, -1)
foils['Cu'] = Reaction('Cu-63', 'n,gamma', 'Cu-64', False, 63.546, 8.96, '29-Cu-63(n,&gamma;).txt', 61.9*3600, 0.6915, 1345.77, 0.00475, -1)
foils['Mg'] = Reaction('Cu-24', 'n,p', 'Na-24', False, 24.305, 1.738, '12-Mg-24(n,p).txt', 15.03*3600, 0.79, 1368.626, 0.999936, -1)
foils['Al'] = Reaction('Al-27', 'n,alpha', 'Na-24', False, 26.9815385, 2.7, '13-Al-27(n,&alpha;).txt', 15.03*3600, 1.0, 1368.626, 0.999936, -1)
foils['Ca'] = Reaction('Ca-44', 'n,gamma', 'Ca-45', False, 40.078, 1.55, '20-Ca-44(n,&gamma;).txt', 165*24*3600, .02086, 12.47, 3e-8, -1)
foils['Sc'] = Reaction('Sc-45', 'n,gamma', 'Sc-46', False, 44.955910, 2.985, '21-Sc-45(n,&gamma;).txt', 84*24*3600, 1.0, 1120.545, 0.99987, -1)
foils['Mn'] = Reaction('Mn-55', 'n,gamma', 'Mn-56', False, 54.938044, 7.21, '25-Mn-55(n,&gamma;).txt', 2.58*3600, 1.0, 1810.726, 0.269, -1)
foils['Fe'] = Reaction('Fe-56', 'n,p', 'Mn-56', False, 55.845, 7.874, '26-Fe-56(n,p).txt', 2.58*3600, 0.9175, 1810.726, 0.269, -1)
foils['Ni'] = Reaction('Ni-58', 'n,p', 'Co-58', False, 58.6934, 8.908, '28-Ni-58(n,p).txt', 70.8*24*3600, 0.68077, 810.7593, 0.9945, -1)
foils['Zr'] = Reaction('Zr-90', 'n,2n', 'Zr-89', False, 91.224, 6.52, '40-Zr-90(n,2n).txt', 64*24*3600, 0.5145, 909.15, 0.9904, -1)
foils['Rh'] = Reaction('Rh-103', "n,n'", 'Rh-103m', False, 102.90550, 12.41, '45-Rh-103(n,inelastic).txt', 56.12*60, 1.0, 39.755, 0.00068, -1)
foils['Dy'] = Reaction('Dy-164', 'n,gamma', 'Dy-165', False, 162.5, 8.54, '66-Dy-164(n,&gamma;).txt', 2.35*3600, 0.2826, 108.160, 0.0301, -1)
foils['Ir'] = Reaction('Ir-191', 'n,gamma', 'Ir-192', False, 174.9668, 9.841, '77-Ir-191(n,&gamma;).txt', 74.2*24*3600, 0.373, 317, 0.81, -1)
foils['Au'] = Reaction('Au-197', 'n,gamma', 'Au-198', False, 196.96657, 19.32, '79-Au-197(n,&gamma;).txt', 2.7*3600*24 , 1.0, 412, 0.95, -1)
