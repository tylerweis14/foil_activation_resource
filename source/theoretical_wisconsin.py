'''
Theoretical Results for the wisconsin irradiation.
'''
from theoretical import Theoretical


irradiation_data = []
irradiation_data.append(['indium', 'In', False, 2.1, 30, 3600*2, 60, 100])
irradiation_data.append(['indium', 'InCd', True, 2.1, 30, 3600*2, 60, 100])
irradiation_data.append(['gold', 'Au', False, 4.1, 60, 3600*2, 120, 100])
irradiation_data.append(['gold', 'AuCd', True, 4.1, 60, 3600*2, 120, 100])
irradiation_data.append(['molybdenum', 'Mo', False, 3.9, 3600, 3600*24*2, 600, 100])
irradiation_data.append(['molybdenum', 'MoCd', True, 3.9, 3600, 3600*24*2, 600, 100])
irradiation_data.append(['rhodium', 'Rh', False, 7.4, 3600, 3600*1, 1800, 100])
irradiation_data.append(['aluminum', 'Al', False, 3.5, 3600, 3600*24*2, 3600, 100])

Theoretical('wisconsin', irradiation_data)
