'''
Theoretical Results for the wisconsin irradiation.
'''
import numpy as np
from theoretical import Theoretical


irradiation_data = []
irradiation_data.append(['indium', 'In', False, np.array([1.1, 1.1, 1.1, 1.1]), 30, 3600*2, 60, 100])
irradiation_data.append(['molybdenum', 'Mo', False, 'estimate', 3600, 3600*24*2, 600, 100])
irradiation_data.append(['zinc', 'Zn', False, 'estimate', 3600*2, 3600*24*2, 3600, 100])
irradiation_data.append(['copper', 'Cu', False, 'estimate', 3600*1, 3600*24*2, 3600, 100])
irradiation_data.append(['magnesium', 'Mg', False, 'estimate', 3600*1, 3600*24*2, 3600, 100])
irradiation_data.append(['rhodium', 'Rh', False, 0.6, 60, 3600*2, 600, 100])

Theoretical('wisconsin', irradiation_data)
