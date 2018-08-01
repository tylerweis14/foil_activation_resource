'''
Theoretical Results for the wisconsin irradiation.
'''
import numpy as np
from theoretical import Theoretical


irradiation_data = []
irradiation_data.append(['indium', 'In', False, np.array([2.1, 2.1, 2.1, 2.2]), 60, 3600*5, 120, 100])
irradiation_data.append(['indium', 'InCd', True, np.array([2.2, 2.2, 2.0, 2.2]), 60, 3600*4, 120, 100])
irradiation_data.append(['gold', 'Au', False, np.array([4.1, 4.1, 4.3, 4.2]), 60, 3600*2, 120, 100])
irradiation_data.append(['gold', 'AuCd', True, np.array([4.1, 4.3, 4.1, 4.1]), 60, 3600*2, 120, 100])
irradiation_data.append(['molybdenum', 'Mo', False, np.array([2.9, 2.9, 2.9, 2.8]), 3600, 3600*24*1, 600, 100])
irradiation_data.append(['molybdenum', 'MoCd', True, np.array([2.7, 2.5, 2.7, 2.7]), 3600, 3600*24*1, 600, 100])
irradiation_data.append(['rhodium', 'Rh', False, np.array([5.5, 5.1, 5.1, 5.3]), 3600, 3600*1, 1800, 100])
irradiation_data.append(['aluminum', 'Al', False, np.array([3.5, 3.5, 3.5, 3.5]), 3600, 3600*24*1, 3600, 100])

irradiation_data.append(['titanium', 'Ti1', False, np.array([5.5, 5.1, 5.1, 5.3]), 3600, 3600*1, 1800, 100])
irradiation_data.append(['titanium', 'Ti2', False, np.array([5.5, 5.1, 5.1, 5.3]), 3600, 3600*1, 1800, 100])

Theoretical('wisconsin', irradiation_data, 'ksu')
