'''
Theoretical Results for the wisconsin irradiation.
'''
import numpy as np
from wand import Wand
import pickle
from reaction import foils
from tex_experiment import experiment_template

dataname = 'theoretical_wisconsin.txt'


def run(rerun_all, dataname):

    dataname = 'theoretical_data/' + dataname
    experimentname = 'wisconsin'
    try:
        with open(dataname, 'rb') as F:
            data = pickle.load(F)
    except:
        data = {}

    # indium
    stack_height = 6
    wand = Wand('indium', 'In', False, np.array([1.1, 1.1, 1.1, 1.1]) * stack_height, 30, 3600*2, 60, 100, experimentname)
    wand.irradiate(True)
    data.update(wand.package_data())

    # molybdenum
    wand = Wand('molybdenum', 'Mo', False, 'estimate', 3600, 3600*24*2, 600, 100, experimentname)
    wand.irradiate(True)
    data.update(wand.package_data())

    '''
    # zinc
    wand = Wand('zinc', 'Zn', False, 'estimate', 3600*2, 3600*24*2, 3600, 100, experimentname)
    wand.irradiate(True)
    data.update(wand.package_data())

    # copper
    wand = Wand('copper', 'Cu', False, 'estimate', 3600*1, 3600*24*2, 3600, 100, experimentname)
    wand.irradiate(True)
    data.update(wand.package_data())

    # magnesium
    wand = Wand('magnesium', 'Mg', False, 'estimate', 3600*1, 3600*24*2, 3600, 100, experimentname)
    wand.irradiate(True)
    data.update(wand.package_data())
    '''

    foils_irradiated = ['In', 'Mo']
    experiment_temp = experiment_template.split('SPLIT')
    foil_s = ''
    for f in foils_irradiated:
        foil_s += '\\include{{tex/{}}}\n'.format(foils[f].plotname + '_' + experimentname + '.tex')
    experiment_tex = experiment_temp[0] + foil_s + experiment_temp[1]
    with open(experimentname + '.tex', 'w+') as F:
        F.write(experiment_tex)
    
    # dump data
    with open(dataname, 'wb') as F:
        pickle.dump(data, F)

if __name__ == '__main__':
    run(True, dataname)

    with open('theoretical_data/' + dataname, 'rb') as F:
        data = pickle.load(F)

    for key, val in data.items():
        counts = val.peak_area
        print('{:>6}  {:4.2e}  {:5.4f}'.format(key, counts, np.sqrt(counts) / counts))
