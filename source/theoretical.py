'''
An object used to simulate a theoretical experiment.
'''
import subprocess
from wand import Wand
import pickle
from reaction import foils
from tex_experiment import experiment_template
from amalgamated_plot import amalgamate

dataname = 'theoretical_wisconsin.txt'


class Theoretical(object):
    def __init__(self, experimentname, irradiations, detector='ksu'):
        self.experimentname = experimentname
        self.dataname = 'theoretical_data/theoretical_' + experimentname + '.txt'
        self.detector = detector
        try:
            with open(dataname, 'rb') as F:
                self.data = pickle.load(F)
        except:
            self.data = {}

        self.foils_irradiated = []
        for data in irradiations:
            wand = Wand(*data, detector, experimentname)
            wand.irradiate(True)
            self.data.update(wand.package_data())
            self.foils_irradiated.append(data[1])

        amalgamate(self.experimentname, self.foils_irradiated)
        experiment_temp = experiment_template.split('SPLIT')
        foil_s = ''
        for f in self.foils_irradiated:
            foil_s += '\\include{{plot/{}}}\n'.format(foils[f].plotname + '_' + experimentname)
        plot_s = 'plot/amalgamated_' + self.experimentname
        experiment_tex = experiment_temp[0] + plot_s + experiment_temp[1] + foil_s + experiment_temp[2]
        experiment_filename = self.experimentname + '.tex'
        with open(experiment_filename, 'w+') as F:
            F.write(experiment_tex)

        # dump data
        with open(self.dataname, 'wb') as F:
            pickle.dump(self.data, F)

        subprocess.run(['pdflatex', experiment_filename])
        subprocess.run(['rm', '{}.log'.format(self.experimentname)])
        subprocess.run(['rm', '{}.aux'.format(self.experimentname)])
        subprocess.run(['rm', '{}.out'.format(self.experimentname)])
