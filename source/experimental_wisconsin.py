# storing the data from the wisconsin mpfd irradiation
from foil import Foil

data = {}
data['al1'] = Foil(60036, 317, 2.20E-02, 6.61E-03, -1)
data['al2'] = Foil(15467, 155, 3.47E-02, 5.48E-03, -1)
data['al3'] = Foil(17094, 171, 3.86E-02, 6.10E-03, -1)
data['al4'] = Foil(18031, 180, 3.08E-02, 4.87E-03, -1)
data['mo_cd1'] = Foil(15271, 150, 0.439, 4.58E-02, -1)
data['mo_cd2'] = Foil(28709, 213, 0.541, 9.57E-02, -1)
data['mo_cd3'] = Foil(14523, 148, 0.758, 7.90E-02, -1)
data['mo_cd4'] = Foil(32746, 230, 0.559, 9.88E-02, -1)

data['dum'] = Foil(0, 0, 0, 0, -1)

data['mo1'] = Foil(117208, 444, 0.365, 6.45E-02, -1)
data['mo2'] = Foil(15617, 156, 0.692, 7.21E-02, -1)
data['mo3'] = Foil(14896, 142, 0.805, 8.38E-02, -1)
data['mo4'] = Foil(30133, 224, 0.629, 0.111, -1)
