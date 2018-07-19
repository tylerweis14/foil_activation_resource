'''
Theoretical Results for the wisconsin irradiation.
'''
import numpy as np
from theoretical import Theoretical


irradiation_data = []
irradiation_data.append(['indium', 'In', False, np.array([2.0, 2.1, 2.1, 2.1]), 60, 3600*5, 120, 100])
irradiation_data.append(['indium', 'InCd', True, np.array([2.2, 2.2, 2.2, 2.3]), 60, 3600*4, 120, 100])
irradiation_data.append(['gold', 'Au', False, np.array([4.1, 4.1, 4.1, 4.1]), 60, 3600*2, 120, 100])
irradiation_data.append(['gold', 'AuCd', True, np.array([4.1, 4.2, 4.3, 4.3]), 60, 3600*2, 120, 100])
irradiation_data.append(['molybdenum', 'Mo', False, 'estimate', 3600, 3600*24*1, 600, 100])
irradiation_data.append(['molybdenum', 'MoCd', True, 'estimate', 3600, 3600*24*1, 600, 100])
irradiation_data.append(['rhodium', 'Rh', False, np.array([5.1, 5.1, 5.3, 5.5]), 3600, 3600*1, 1800, 100])
irradiation_data.append(['aluminum', 'Al', False, 3.5, 3600, 3600*24*1, 3600, 100])

Theoretical('wisconsin', irradiation_data)
