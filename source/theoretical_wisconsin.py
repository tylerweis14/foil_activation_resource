'''
Theoretical Results for the wisconsin irradiation.
'''
import numpy as np
from wand import Wand
import pickle

dataname = 'theoretical_wisconsin.txt'


def run(rerun_all, dataname):

    dataname = 'theoretical_data/' + dataname
    experimentname = 'wisconsin'
    try:
        with open(dataname, 'rb') as F:
            data = pickle.load(F)
    except:
        data = {}
    ###############################################################################
    #                                rhodium
    ###############################################################################

    if True or rerun_all:
        stack_height = 6
        wand = Wand('indium', 'In', False, np.array([1.1, 1.1, 1.1, 1.1]) * stack_height, 60, 3600*2, 600, 100, experimentname)
        wand.irradiate(False)
        data.update(wand.package_data())

    # dump data
    with open(dataname, 'wb') as F:
        pickle.dump(data, F)

if __name__ == '__main__':
    run(True, dataname)

    with open(dataname, 'rb') as F:
        data = pickle.load(F)

    for key, val in data.items():
        counts = val.peak_area
        print('{:>6}  {:4.2e}  {:5.4f}'.format(key, counts, np.sqrt(counts) / counts))
