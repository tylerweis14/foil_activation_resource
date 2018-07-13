'''
Theoretical Results for the all possible irradiations.
'''
from theoretical import Theoretical


irradiation_data = []
irradiation_data.append(['indium', 'In', False, 'estimate', 30, 3600*2, 60, 100])
irradiation_data.append(['molybdenum', 'Mo', False, 'estimate', 3600, 3600*24*2, 600, 100])
irradiation_data.append(['zinc', 'Zn', False, 'estimate', 3600*2, 3600*24*2, 3600, 100])
irradiation_data.append(['copper', 'Cu', False, 'estimate', 3600, 3600*24*2, 3600, 100])
irradiation_data.append(['magnesium', 'Mg', False, 'estimate', 60, 3600*2, 3600, 100])
irradiation_data.append(['aluminum', 'Al', False, 'estimate', 3600, 3600*24*2, 3600, 100])
irradiation_data.append(['calcium', 'Ca', False, 'estimate', 3600, 3600*24*2, 3600, 100])
irradiation_data.append(['scandium', 'Sc', False, 'estimate', 3600, 3600*24*2, 3600, 100])
irradiation_data.append(['manganese', 'Mn', False, 'estimate', 60, 3600*2, 600, 100])
irradiation_data.append(['iron', 'Fe', False, 'estimate', 60, 3600*2, 3600, 100])
irradiation_data.append(['nickel', 'Ni', False, 'estimate', 3600, 3600*24*2, 3600, 100])
irradiation_data.append(['zirconium', 'Zr', False, 'estimate', 3600, 3600*24*2, 3600, 100])
irradiation_data.append(['rhodium', 'Rh', False, 0.6, 60, 3600*2, 3600, 100])
irradiation_data.append(['dysprosium', 'Dy', False, 'estimate', 60, 3600*2, 120, 100])
irradiation_data.append(['iridium', 'Ir', False, 'estimate', 60, 3600*2, 600, 100])
irradiation_data.append(['gold', 'Au', False, 'estimate', 60, 3600*2, 60, 100])

Theoretical('library', irradiation_data)
