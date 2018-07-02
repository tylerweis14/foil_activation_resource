from scipy.interpolate import interp1d
import numpy as np


def extract(xs_string):
    xs_erg, xs_vals = np.loadtxt('xs/' + xs_string, delimiter=',', skiprows=1, unpack=True)
    f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
    region = xs_erg[0], xs_erg[-1]
    return f, region


# cadmium
Cd = {}
Cd['M'] = 112.411  # g/mol
Cd['rho'] = 8.69  # g/cm3
Cd['reactions'] = {}

cd_xs_data = [extract('48-Cd-106(n,total).txt')[0],
              extract('48-Cd-108(n,total).txt')[0],
              extract('48-Cd-110(n,total).txt')[0],
              extract('48-Cd-111(n,total).txt')[0],
              extract('48-Cd-112(n,total).txt')[0],
              extract('48-Cd-113(n,total).txt')[0],
              extract('48-Cd-114(n,total).txt')[0],
              extract('48-Cd-116(n,total).txt')[0]]

cd_weights = [0.0125, 0.0089, 0.1249, 0.1280, 0.2413, 0.1222, 0.2873, 0.0749]


def cd_xs_weighted(e):
    xs = 0
    for isotope in range(len(cd_weights)):
        xs += cd_weights[isotope] * cd_xs_data[isotope](e)
    return xs


Cd['reactions']['n,tot'] = {}
Cd['reactions']['n,tot']['func'] = cd_xs_weighted
Cd['reactions']['n,tot']['halflife'] = 0  # s
Cd['reactions']['n,tot']['label'] = r'($n,tot$)'

# magnesium
Mg = {}
Mg['M'] = 24.3050  # g/mol
Mg['rho'] = 1.738  # g/cm3
Mg['reactions'] = {}

# Mg24(n,p)Na24
Mg['reactions']['n,p'] = {}
f, r = extract('12-Mg-24(n,p)')
Mg['reactions']['n,p']['func'] = f
Mg['reactions']['n,p']['region'] = r
Mg['reactions']['n,p']['roi'] = 6.4162e+06,1.1257e+07  # computed
Mg['reactions']['n,p']['roi_cd'] = r  # initial guess
Mg['reactions']['n,p']['halflife'] = 14.9590 * 60 * 60 # s
Mg['reactions']['n,p']['label'] = r'($n,p$)'
Mg['reactions']['n,p']['erg'] = [-1,1]  # keV (placeholder)
Mg['reactions']['n,p']['plotname'] = 'mg_n,p'

# aluminum
Al = {}
Al['M'] = 26.9815385  # g/mol
Al['rho'] = 2.7  # g/cm3
Al['reactions'] = {}

# Al27(n,p)Mg27
Al['reactions']['n,p'] = {}
f, r = extract('13-Al-27(n,p)')
Al['reactions']['n,p']['func'] = f
Al['reactions']['n,p']['region'] = r
Al['reactions']['n,p']['roi'] = 3.4248e+06, 9.1383e+06  # computed
Al['reactions']['n,p']['roi_cd'] = 3.4248e+06, 9.1383e+06  # initial guess
Al['reactions']['n,p']['halflife'] = 9.458 * 60  # s
Al['reactions']['n,p']['label'] = r'($n,p$)'
Al['reactions']['n,p']['erg'] = [(.007, 180), (.7, 840), (.3, 1013)]  # keV (placeholder)
Al['reactions']['n,p']['plotname'] = 'al_n,p'

# Al27(n,a)Na24
Al['reactions']['n,alpha'] = {}
f, r = extract('13-Al-27(n,&alpha;)')
Al['reactions']['n,alpha']['func'] = f
Al['reactions']['n,alpha']['region'] = r
Al['reactions']['n,alpha']['roi'] = 6.4564e+06, 1.1695e+07  # computed
Al['reactions']['n,alpha']['roi_cd'] = 6.4564e+06, 1.1695e+07  # initial guess
Al['reactions']['n,alpha']['halflife'] = 15.03 * 60 * 60  # s
Al['reactions']['n,alpha']['label'] = r'($n,\alpha$)'
Al['reactions']['n,alpha']['erg'] = [(1, 1369), (1, 2754)]  # keV
Al['reactions']['n,alpha']['plotname'] = 'al_n,alpha'

# Al27(n,g)Al28
Al['reactions']['n,gamma'] = {}
f, r = extract('13-Al-27(n,&gamma;)')
Al['reactions']['n,gamma']['func'] = f
Al['reactions']['n,gamma']['region'] = r
Al['reactions']['n,gamma']['roi'] = 2.8233e-03, 4.1509e-01  # computed
Al['reactions']['n,gamma']['roi_cd'] = 2.8233e-02, 4.1509e+00  # initial guess
Al['reactions']['n,gamma']['halflife'] = 2.246 * 60  # s
Al['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Al['reactions']['n,gamma']['erg'] = [(1, 1780)]  # keV (placeholder)
Al['reactions']['n,gamma']['plotname'] = 'al_n,gamma'

# scandium
Sc = {}
Sc['M'] = 44.955910  # g/mol
Sc['rho'] = 2.985  # g/cm3
Sc['reactions'] = {}

# Sc45(n,g)Sc46
Sc['reactions']['n,gamma'] = {}
f, r = extract('21-Sc-45(n,&gamma;)')
Sc['reactions']['n,gamma']['func'] = f
Sc['reactions']['n,gamma']['region'] = r
Sc['reactions']['n,gamma']['roi'] = 2.7970e-03, 2.7942e-01 # computed
Sc['reactions']['n,gamma']['roi_cd'] = r # initial guess
Sc['reactions']['n,gamma']['halflife'] = 43.72 *60 * 60  # s
Sc['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Sc['reactions']['n,gamma']['erg'] = [(1, 1780)]  # keV (placeholder)
Sc['reactions']['n,gamma']['plotname'] = 'sc_n,gamma'


# titanium
Ti = {}
Ti['M'] = 47.867  # g/mol
Ti['rho'] = 4.506  # g/cm3
Ti['reactions'] = {}

# Ti48(n,p)Sc48
Ti['reactions']['n,p'] = {}
f, r = extract('22-Ti-48(n,p)')
Ti['reactions']['n,p']['func'] = f
Ti['reactions']['n,p']['region'] = r
Ti['reactions']['n,p']['roi'] = 5.6369e+06, 1.1541e+07 # computed
Ti['reactions']['n,p']['roi_cd'] = r  # initial guess
Ti['reactions']['n,p']['halflife'] = 43.7 * 60 * 60 #s
Ti['reactions']['n,p']['label'] = r'($n,p$)'
Ti['reactions']['n,p']['erg'] = [-1,1]#KeV (placeholder)
Ti['reactions']['n,p']['plotname'] = 'ti_n,p'

#TODO Ti46,47

# manganese
Mn = {}
Mn['M'] = 54.938044  # g/mol
Mn['rho'] = 7.21  # g/cm3
Mn['reactions'] = {}

# Mn55(n,g)Mn56
Mn['reactions']['n,gamma'] = {}
f, r = extract('25-Mn-55(n,&gamma;)')
Mn['reactions']['n,gamma']['func'] = f
Mn['reactions']['n,gamma']['region'] = r
Mn['reactions']['n,gamma']['roi'] = 2.9364e-03, 2.3816e+01 # computed
Mn['reactions']['n,gamma']['roi_cd'] = r # initial guess
Mn['reactions']['n,gamma']['halflife'] = 2.5789 *60 * 60  # s
Mn['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Mn['reactions']['n,gamma']['erg'] = [(1, 1780)]  # keV (placeholder)
Mn['reactions']['n,gamma']['plotname'] = 'mn_n,gamma'

# iron
Fe = {}
Fe['M'] = 55.845  # g/mol
Fe['rho'] = 7.874  # g/cm3
Fe['reactions'] = {}

# Fe56(n,p)Mn56
Fe['reactions']['n,p'] = {}
f, r = extract('26-Fe-56(n,p)')
Fe['reactions']['n,p']['func'] = f
Fe['reactions']['n,p']['region'] = r
Fe['reactions']['n,p']['roi'] = 7.4169e+06,1.1013e+07 # computed
Fe['reactions']['n,p']['roi_cd'] = r  # initial guess
Fe['reactions']['n,p']['halflife'] = 2.5789 * 60 * 60 #s
Fe['reactions']['n,p']['label'] = r'($n,p$)'
Fe['reactions']['n,p']['erg'] = [-1,1]#KeV (placeholder)
Fe['reactions']['n,p']['plotname'] = 'fe_n,p'

# Fe58(n,g)Fe59
Fe['reactions']['n,gamma'] = {}
f, r = extract('26-Fe-58(n,&gamma;)')
Fe['reactions']['n,gamma']['func'] = f
Fe['reactions']['n,gamma']['region'] = r
Fe['reactions']['n,gamma']['roi'] = 2.9877e-03, 3.5809e+02 # computed
Fe['reactions']['n,gamma']['roi_cd'] = r # initial guess
Fe['reactions']['n,gamma']['halflife'] = 44.6 * 24 * 60 * 60 # s
Fe['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Fe['reactions']['n,gamma']['erg'] = [(1,1)]  # keV (placeholder)
Fe['reactions']['n,gamma']['plotname'] = 'fe_n,gamma'

#TODO Fe54

# nickel
Ni = {}
Ni['M'] = 58.6934  # g/mol
Ni['rho'] = 8.908  # g/cm3
Ni['reactions'] = {}

# Ni58(n,p)Co58
Ni['reactions']['n,p'] = {}
f, r = extract('28-Ni-58(n,p)')
Ni['reactions']['n,p']['func'] = f
Ni['reactions']['n,p']['region'] = r
Ni['reactions']['n,p']['roi'] = 2.0215e+06, 7.4169e+06 # computed
Ni['reactions']['n,p']['roi_cd'] = r  # initial guess
Ni['reactions']['n,p']['halflife'] = 70.86 * 24 * 60 * 60 #s
Ni['reactions']['n,p']['label'] = r'($n,p$)'
Ni['reactions']['n,p']['erg'] = [-1,1]#KeV (placeholder)
Ni['reactions']['n,p']['plotname'] = 'ni_n,p'


# copper
Cu = {}
Cu['M'] = 63.546  # g/mol
Cu['rho'] = 8.96  # g/cm3
Cu['reactions'] = {}

# Cu63(n,g)Cu64
Cu['reactions']['n,gamma'] = {}
f, r = extract('29-Cu-63(n,&gamma;)')
Cu['reactions']['n,gamma']['func'] = f
Cu['reactions']['n,gamma']['region'] = r
Cu['reactions']['n,gamma']['roi'] = 2.9583e-03, 5.7752e+02 # computed
Cu['reactions']['n,gamma']['roi_cd'] = r # initial guess
Cu['reactions']['n,gamma']['halflife'] = 12.70 * 60 * 60 # s
Cu['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Cu['reactions']['n,gamma']['erg'] = [(1,1)]  # keV (placeholder)
Cu['reactions']['n,gamma']['plotname'] = 'cu_n,gamma'

# zinc
Zn = {}
Zn['M'] = 65.38  # g/mol
Zn['rho'] = 7.14  # g/cm3
Zn['reactions'] = {}

# Zn64(n,p)Cu64
Zn['reactions']['n,p'] = {}
f, r = extract('30-Zn-64(n,p)')
Zn['reactions']['n,p']['func'] = f
Zn['reactions']['n,p']['region'] = r
Zn['reactions']['n,p']['roi'] = 2.4856e+06, 7.6116e+06 # computed
Zn['reactions']['n,p']['roi_cd'] = r  # initial guess
Zn['reactions']['n,p']['halflife'] = 12.70 * 60 * 60 # s
Zn['reactions']['n,p']['label'] = r'($n,p$)'
Zn['reactions']['n,p']['erg'] = [-1,1]#KeV (placeholder)
Zn['reactions']['n,p']['plotname'] = 'zn_n,p'

# zirconium
Zr = {}
Zr['M'] = 91.224  # g/mol
Zr['rho'] = 6.52  # g/cm3
Zr['reactions'] = {}

# Zr90(n,2n)Zr89
Zr['reactions']['n,2n'] = {}
f, r = extract('40-Zr-90(n,2n)')
Zr['reactions']['n,2n']['func'] = f
Zr['reactions']['n,2n']['region'] = r
Zr['reactions']['n,2n']['roi'] = 1.2637e+07, 1.7072e+07 # computed
Zr['reactions']['n,2n']['roi_cd'] = r # initial guess
Zr['reactions']['n,2n']['halflife'] = 78.41 *60 * 60  # s
Zr['reactions']['n,2n']['label'] = r'($n,2n$)'
Zr['reactions']['n,2n']['erg'] = [(1, 1780)]  # keV (placeholder)
Zr['reactions']['n,2n']['plotname'] = 'zr_n,2n'

# molybdenum
Mo = {}
Mo['M'] = 95.95 # g/mol
Mo['rho'] = 10.28  # g/cm3
Mo['reactions'] = {}

# Mo98(n,g)Mo99
Mo['reactions']['n,gamma'] = {}
f, r = extract('42-Mo-98(n,&gamma;)')
Mo['reactions']['n,gamma']['func'] = f
Mo['reactions']['n,gamma']['region'] = r
Mo['reactions']['n,gamma']['roi'] = 1.6333e-02,7.6131e+03 # computed
Mo['reactions']['n,gamma']['roi_cd'] = r # initial guess
Mo['reactions']['n,gamma']['halflife'] =  	65.94 * 60 * 60  # s
Mo['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Mo['reactions']['n,gamma']['erg'] = [(1, 1)]  # keV (placeholder)
Mo['reactions']['n,gamma']['plotname'] = 'mo_n,gamma'

# rhodium
Rh = {}
Rh['M'] = 102.90550  # g/mol
Rh['rho'] = 12.41  # g/cm3
Rh['reactions'] = {}

Rh['reactions']['n,gamma'] = {}
f, r = extract('45-Rh-103(n,&gamma;).txt')
Rh['reactions']['n,gamma']['func'] = f
Rh['reactions']['n,gamma']['region'] = r
Rh['reactions']['n,gamma']['roi'] = 4.6704e-03, 1.3929e+00  # computed
Rh['reactions']['n,gamma']['roi_cd'] = 4.6704e-03, 1.3929e+00  # initial guess
Rh['reactions']['n,gamma']['halflife'] = 4.4 * 60  # s
Rh['reactions']['n,gamma']['label'] = r"($n,\gamma$)"
Rh['reactions']['n,gamma']['erg'] = [(0.47, 51), (0.025, 78), (0.026, 560), (0.0018, 770)]  # intensity, keV
Rh['reactions']['n,gamma']['plotname'] = 'rh_n,gamma'

Rh['reactions']['n,inelastic'] = {}
f, r = extract('45-Rh-103(n,inelastic).txt')
Rh['reactions']['n,inelastic']['func'] = f
Rh['reactions']['n,inelastic']['region'] = r
Rh['reactions']['n,inelastic']['roi'] = 4.4469e+05, 5.1947e+06  # computed
Rh['reactions']['n,inelastic']['roi_cd'] = 4.4469e+05, 5.1947e+06  # initial guess
Rh['reactions']['n,inelastic']['halflife'] = 56.12 * 60  # s
Rh['reactions']['n,inelastic']['label'] = r"($n,n'$)"
Rh['reactions']['n,inelastic']['erg'] = [(0.004, 40)]  # intensity, keV
Rh['reactions']['n,inelastic']['plotname'] = 'rh_n,inelastic'

# Rh['reactions']['n,2n'] = {}
# Rh['reactions']['n,2n']['func'] = extract('45-Rh-103(n,2n).txt')
# Rh['reactions']['n,2n']['halflife'] = 35.4 * 60 * 60  # s
# Rh['reactions']['n,2n']['label'] = r"($n,2n$)"
# Rh['reactions']['n,inelastic']['erg'] = [(0.004, 40)]  # intensity, keV

# Rh['reactions']['n,p'] = {}
# Rh['reactions']['n,p']['func'] = extract('45-Rh-103(n,inelastic).txt')
# Rh['reactions']['n,p']['halflife'] = 39.35 * 60 * 60 * 24  # s
# Rh['reactions']['n,p']['label'] = r"($n,p$)"


# indium
In = {}
In['M'] = 114.818  # g/mol
In['rho'] = 7.31  # g/cm3
In['reactions'] = {}

In['reactions']['n,gamma'] = {}
f, r = extract('49-In-115(n,&gamma;).txt')
In['reactions']['n,gamma']['func'] = f
In['reactions']['n,gamma']['region'] = r
In['reactions']['n,gamma']['roi'] = 7.0021e-03, 1.6130e+00  # computed
In['reactions']['n,gamma']['roi_cd'] = 1.1955e+00, 1.9916e+00  # computed
In['reactions']['n,gamma']['halflife'] = 54 * 60  # s
In['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
In['reactions']['n,gamma']['erg'] = [(0.03, 138), (0.36, 417), (0.17, 819), (0.53, 1090),
                                     (0.8, 1293), (0.11, 1508), (0.2, 2111)]  # intensity, keV
In['reactions']['n,gamma']['plotname'] = 'in_n,gamma'

In['reactions']['n,inelastic'] = {}
f, r = extract('49-In-115(n,inelastic).txt')
In['reactions']['n,inelastic']['func'] = f
In['reactions']['n,inelastic']['region'] = r
In['reactions']['n,inelastic']['roi'] = 1.3314e+06, 5.9607e+06  # computed
In['reactions']['n,inelastic']['roi_cd'] = 1.3368e+06, 5.9704e+06  # computed
In['reactions']['n,inelastic']['halflife'] = 4.36 * 60 * 60  # s
In['reactions']['n,inelastic']['label'] = r"($n,n'$)"
In['reactions']['n,inelastic']['erg'] = [(0.5, 335)]  # intensity, keV
In['reactions']['n,inelastic']['plotname'] = 'in_n,inelastic'

# Europium
Eu = {}
Eu['M'] = 151.964  # g/mol
Eu['rho'] = 5.264  # g/cm3
Eu['reactions'] = {}

# Eu151(n,g)Eu152
Eu['reactions']['n,gamma'] = {}
f, r = extract('63-Eu-151(n,&gamma;)')
Eu['reactions']['n,gamma']['func'] = f
Eu['reactions']['n,gamma']['region'] = r
Eu['reactions']['n,gamma']['roi'] = 1.8403e-03,4.5379e-01 # computed
Eu['reactions']['n,gamma']['roi_cd'] = r # initial guess
Eu['reactions']['n,gamma']['halflife'] = 13.537 * 365 * 24 * 60 * 60  # s
Eu['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Eu['reactions']['n,gamma']['erg'] = [(1, 1)]  # keV (placeholder)
Eu['reactions']['n,gamma']['plotname'] = 'Eu_n,gamma'

# dysprosium
Dy = {}
Dy['M'] = 162.5  # g/mol
Dy['rho'] = 8.54  # g/cm3
Dy['reactions'] = {}

# Dy164(n,g)Dy165
Dy['reactions']['n,gamma'] = {}
f, r = extract('66-Dy-164(n,&gamma;)')
Dy['reactions']['n,gamma']['func'] = f
Dy['reactions']['n,gamma']['region'] = r
Dy['reactions']['n,gamma']['roi'] = 2.5806e-03, 1.6797e-01 # computed
Dy['reactions']['n,gamma']['roi_cd'] = r # initial guess
Dy['reactions']['n,gamma']['halflife'] =  	2.334 * 60 * 60  # s
Dy['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Dy['reactions']['n,gamma']['erg'] = [(1, 1)]  # keV (placeholder)
Dy['reactions']['n,gamma']['plotname'] = 'dy_n,gamma'

# lutetium
Lu = {}
Lu['M'] = 174.9668  # g/mol
Lu['rho'] = 9.841  # g/cm3
Lu['reactions'] = {}

# Lu176(n,g)Lu177
Lu['reactions']['n,gamma'] = {}
f, r = extract('71-Lu-176(n,&gamma;)')
Lu['reactions']['n,gamma']['func'] = f
Lu['reactions']['n,gamma']['region'] = r
Lu['reactions']['n,gamma']['roi'] = 9.4803e-03,1.7852e-01 # initial guess
Lu['reactions']['n,gamma']['roi_cd'] = r # initial guess
Lu['reactions']['n,gamma']['halflife'] = 6.6475 * 24 * 60 * 60  # s
Lu['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Lu['reactions']['n,gamma']['erg'] = [(1, 1)]  # keV (placeholder)
Lu['reactions']['n,gamma']['plotname'] = 'lu_n,gamma'

# iridium
Ir = {}
Ir['M'] = 174.9668  # g/mol
Ir['rho'] = 9.841  # g/cm3
Ir['reactions'] = {}

# Ir191(n,g)Ir192
Ir['reactions']['n,gamma'] = {}
f, r = extract('71-Lu-176(n,&gamma;)')
Ir['reactions']['n,gamma']['func'] = f
Ir['reactions']['n,gamma']['region'] = r
Ir['reactions']['n,gamma']['roi'] = 9.4803e-03,1.7852e-01 # computed
Ir['reactions']['n,gamma']['roi_cd'] = r # initial guess
Ir['reactions']['n,gamma']['halflife'] = 73.827 * 24 * 60 * 60  # s
Ir['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Ir['reactions']['n,gamma']['erg'] = [(1, 1)]  # keV (placeholder)
Ir['reactions']['n,gamma']['plotname'] = 'ir_n,gamma'

# tungsten
W = {}
W['M'] = 183.84  # g/mol
W['rho'] = 19.3  # g/cm3
W['reactions'] = {}

# W186(n,g)W187
W['reactions']['n,gamma'] = {}
f, r = extract('74-W-186(n,&gamma;)')
W['reactions']['n,gamma']['func'] = f
W['reactions']['n,gamma']['region'] = r
W['reactions']['n,gamma']['roi'] = 5.8359e-03,1.9497e+01 # computed
W['reactions']['n,gamma']['roi_cd'] = r # initial guess
W['reactions']['n,gamma']['halflife'] = 23.72 * 60 * 60  # s
W['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
W['reactions']['n,gamma']['erg'] = [(1, 1)]  # keV (placeholder)
W['reactions']['n,gamma']['plotname'] = 'w_n,gamma'


# gold
Au = {}
Au['M'] = 196.96657  # g/mol
Au['rho'] = 19.32  # g/cm3
Au['reactions'] = {}

Au['reactions']['n,gamma'] = {}
f, r = extract('79-Au-197(n,&gamma;).txt')
Au['reactions']['n,gamma']['func'] = f
Au['reactions']['n,gamma']['region'] = r
Au['reactions']['n,gamma']['roi'] = 6.7266e-03, 5.2684e+00  # computed
Au['reactions']['n,gamma']['roi_cd'] = 4.0752e+00, 7.1730e+00  # computed
Au['reactions']['n,gamma']['halflife'] = 2.7 * 60 * 60 * 24  # s
Au['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Au['reactions']['n,gamma']['erg'] = [(0.95, 412), (0.01, 676), (0.002, 1088)]  # intensity, keV
Au['reactions']['n,gamma']['plotname'] = 'au_n,gamma'

Au['reactions']['n,2n'] = {}
f, r = extract('79-Au-197(n,2n).txt')
Au['reactions']['n,2n']['func'] = f
Au['reactions']['n,2n']['region'] = r
Au['reactions']['n,2n']['roi'] = 8.8259e+06, 1.3510e+07  # computed
Au['reactions']['n,2n']['roi_cd'] = 8.8254e+06, 1.3512e+07  # computed
Au['reactions']['n,2n']['halflife'] = 6.18 * 60 * 60 * 24  # s
Au['reactions']['n,2n']['label'] = r'($n,2n$)'
Au['reactions']['n,2n']['erg'] = [(0.25, 333), (0.94, 356), (0.06, 426), (0.002, 1091)]  # intensity, keV
Au['reactions']['n,2n']['plotname'] = 'au_n,2n'

Au['reactions']['n,inelastic'] = {}
f, r = extract('79-Au-197(n,inelastic).txt')
Au['reactions']['n,inelastic']['func'] = f
Au['reactions']['n,inelastic']['region'] = r
Au['reactions']['n,inelastic']['roi'] = 3.2404e+05, 5.2532e+06  # computed
Au['reactions']['n,inelastic']['roi_cd'] = 3.2797e+05, 5.2760e+06  # computed
Au['reactions']['n,inelastic']['halflife'] = 7.8  # s
Au['reactions']['n,inelastic']['label'] = r"($n,n'$)"
Au['reactions']['n,inelastic']['erg'] = [(0.08, 130), (0.75, 279)]  # intensity, keV
Au['reactions']['n,inelastic']['plotname'] = 'au_n,inelastic'

# uranium
U = {}
U['M'] = 235.044  # g/mol
U['rho'] = 19.1  # g/cm3
U['reactions'] = {}

U['reactions']['n,total_fission'] = {}
f, r = extract('92-U-235(n,total_fission).txt')
U['reactions']['n,total_fission']['func'] = f
U['reactions']['n,total_fission']['region'] = r
U['reactions']['n,total_fission']['roi'] = 2.5315e-03, 3.0442e-01  # unknown
U['reactions']['n,total_fission']['roi_cd'] = -1, -1  # unknown
U['reactions']['n,total_fission']['halflife'] = -1  # unknown
U['reactions']['n,total_fission']['label'] = r'($n,fission$)'
U['reactions']['n,total_fission']['erg'] = -1  # unknown
U['reactions']['n,total_fission']['plotname'] = 'u_n,total_fission'


# all foils
foils = {}
foils['Al'] = Al
foils['Rh'] = Rh
foils['In'] = In
foils['Au'] = Au
foils['U'] = U
foils['Sc'] = Sc
foils['Ti'] = Ti
foils['Fe'] = Fe
foils['Ni'] = Ni
foils['Cu'] = Cu
foils['Zn'] = Zn
foils['Zr'] = Zr
foils['Mg'] = Mg
foils['W'] = W
foils['Mn'] = Mn
foils['Lu'] = Lu
foils['Eu'] = Eu
foils['Dy'] = Dy
foils['Ir'] = Ir
foils['Mo'] = Mo