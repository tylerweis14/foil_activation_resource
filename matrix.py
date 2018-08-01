import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import quad
from triga_spectrum import triga_spectrum
from reaction import foils


class Response_Matrix(object):
    def __init__(self, reactions, bin_structure):
        self.reactions = reactions
        self.bin_structure = bin_structure
        self.response_matrix = self.calc_response_matrix()
        self.plot()

    def calc_response_matrix(self):
        response_matrix = np.zeros((len(self.reactions), len(self.bin_structure)-1))
        for i, mat in enumerate(self.reactions):
            foil = foils[mat]

            def rr(e):
                return foil.func(e) * triga_spectrum(e)

            for j in range(len(self.bin_structure)-1):
                num = quad(rr, self.bin_structure[j], self.bin_structure[j+1])[0]
                #den = quad(triga_spectrum, self.bin_structure[j], self.bin_structure[j+1])[0]
                #response_matrix[i, j] = (num / den) if num != 0 or den != 0 else 0
                response_matrix[i, j] = num if num != 0 else 0
        return response_matrix

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_ylim(1e5, 1e15)
        X = self.bin_structure[1:] + self.bin_structure[:-1]
        for Y in self.response_matrix:
            ax.step(X, Y)


if __name__ == '__main__':
    bins = np.logspace(-5, 8, 200)
    Response_Matrix(['In', 'InCd', 'Au', 'AuCd', 'Mo', 'MoCd', 'Rh', 'Al'], bins)
