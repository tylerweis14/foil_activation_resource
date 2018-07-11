'''
Houses the reaction object.
'''


class Reaction(object):
    '''
    Docstring goes here.
    '''
    def __init__(self, reactant, reaction, byproduct, M, rho, xs_file, halflife, abundance, erg, BR, cost):
        self.reactant = reactant
        self.reaction = reaction
        self.byproduct = byproduct
        self.M = M
        self.rho = rho
        self.xs_file = xs_file
        self.halflife = halflife
        self.abundance = abundance
        self.erg = erg
        self.BR = BR
        self.cost = cost
