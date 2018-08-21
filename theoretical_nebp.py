'''
Theoretical Results for the wisconsin irradiation.
'''
import numpy as np
from theoretical import Theoretical


irradiation_data = []
P = 250
irradiation_data.append(['indium', 'In', np.array([50, 75, 50, 25]), 3600, 3600, 300, P])
irradiation_data.append(['indium', 'InCd', np.array([50, 75, 50, 25]), 3600, 3600, 300, P])
irradiation_data.append(['aluminum', 'Al', np.array([100, 150, 100, 75]), 3600*2, 3600*3, 3600*6, P])
irradiation_data.append(['molybdenum', 'Mo', np.array([200, 200, 150, 100]), 3600, 3600, 3600, P])
irradiation_data.append(['molybdenum', 'MoCd', np.array([200, 200, 175, 150]), 3600, 3600, 3600, P])
irradiation_data.append(['titanium', 'Ti1', np.array([250, 400, 300, 200]), 3600*2, 3600, 3600*6, P])
irradiation_data.append(['titanium', 'Ti2', np.array([250, 400, 300, 200]), 3600*2, 3600, 3600*6, P])
irradiation_data.append(['copper', 'Cu', np.array([200, 375, 350, 325]), 3600*2, 3600, 3600*6, P])
irradiation_data.append(['copper', 'CuCd', np.array([350, 375, 350, 325]), 3600*2, 3600, 3600*6, P])
irradiation_data.append(['nickel', 'Ni', np.array([100, 375, 350, 325]), 3600*2, 3600, 3600*6, P])
irradiation_data.append(['iron', 'Fe', np.array([100, 375, 350, 325]), 3600*2, 3600, 3600*6, P])


Theoretical('nebp', irradiation_data, 'ksu', 'triga_nebp')