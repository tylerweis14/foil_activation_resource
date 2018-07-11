import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

from scipy.integrate import quad
from scipy.optimize import fsolve

from cross_sections import foils, Cd
from triga_spectrum import triga_spectrum

###############################################################################
#                               nice plotting
###############################################################################

rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})

###############################################################################
#                               flux
###############################################################################
# flux
phi = triga_spectrum


#
total_phi = 0
e = np.logspace(-5, 9, 100)
for i in range(len(e) - 1):
    total_phi += quad(phi, e[i], e[i+1])[0]


fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_xlabel('Energy (eV)')
ax.set_ylabel('$\Phi$ $cm^{-2}s{-1}$')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1E-5, 1E9)
ax.set_ylim(1E-12, 1E1)
x = np.logspace(-5, 9, 1000)
y = phi(x)
ax.plot(x, y, 'k')
plt.savefig('plot/flux.png', dpi=300)
plt.close(fig)

###############################################################################
#                               cadmium
###############################################################################


# cadmium factor
def no_cd(e):
    return 1


def ya_cd(e):
    # facts of life
    Na = 6.0221409E23  # atoms / mol
    cd_thickness = 0.05

    term = ((Cd['rho'] * Na) / Cd['M']) * cd_thickness * 1E-24
    cd_xs = Cd['reactions']['n,tot']['func']
    factor = np.exp(-term * cd_xs(e) * 5)
    return factor

###############################################################################
#                               roi
###############################################################################


def roi(sigma, phi, cd, cd_cov=False, recalculate=False):
    region = sigma['region']
    roi = sigma['roi']
    xs = sigma['func']
    plotname = sigma['plotname']

    if cd_cov:
        roi = sigma['roi_cd']
        plotname += '_cd'

    def reaction_rate(e, phi, sigma, cd_fun):
        return sigma(e) * phi(e) * cd_fun(e)

    def fold(l, r):
        R = 0
        e = np.geomspace(l, r, 1000)
        for i in range(len(e) - 1):
            R += quad(reaction_rate, e[i], e[i+1], args=(phi, xs, cd))[0]
        return R

    R_tot = fold(region[0], region[1])
    R95 = R_tot * 0.95

    def fold_l(l, r, r95):
        R = fold(l, r)
        return R - r95

    def fold_r(r, l, r95):
        R = fold(l, r)
        return R - r95

    if recalculate:
        left = fsolve(fold_l, roi[0], args=(region[1], R95))[0]
        right = fsolve(fold_r, roi[1], args=(region[0], R95))[0]
    else:
        left = roi[0]
        right = roi[1]

    print('{:6.4f}'.format(fold(left, region[1]) / R_tot))
    print('{:6.4f}'.format(fold(region[0], right) / R_tot))
    print('{:6.4f}'.format(fold(left, right) / R_tot))

    # plot
    e = np.geomspace(region[0], region[1], 1000)
    xss = reaction_rate(e, phi, xs, cd)

    # roi_e = np.geomspace(left, right, 1000)
    # roi_xss = reaction_rate(roi_e, phi, xs, cd)

    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Energy $eV$')
    ax.set_ylabel('Reaction Rate (Arbitrary Units)')
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.plot(e, xss, color='black', linewidth=0.5)

    # roi stuff
    line_height = min(reaction_rate(left, phi, xs, cd) * 0.2, reaction_rate(right, phi, xs, cd) * 0.2)
    ax.plot([left, right], [line_height, line_height], color='black', linewidth=0.8)

    ax.set_xlim(*region)
    y_upper_lim = np.max(xss) * 7
    if np.log(np.max(xss)) - np.log(np.min(xss)) > 28:
        ax.set_ylim(y_upper_lim * 1e-12, y_upper_lim)
    else:
        ax.set_ylim(np.min(xss), y_upper_lim)
    plt.savefig('plot/{}.png'.format(plotname), dpi=300)
    plt.close(fig)

    return left, right


# test individual case
test = False
if test:
    xs = foils['Au']['reactions']['n,gamma']
    left, right = roi(xs, phi, ya_cd, False, False)


# run full simulation using each foil
run_all = False
# gold
if False or run_all:
    for xs in foils['Au']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# indium
if False or run_all:
    for xs in foils['In']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# rhodium
if False or run_all:
    for xs in foils['Rh']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# aluminum
if False or run_all:
    for xs in foils['Al']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# gold (Cd)
if False or run_all:
    for xs in foils['Au']['reactions'].values():
        print('\n' + xs['plotname'] + '  (Cd)')
        left, right = roi(xs, phi, ya_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# indium (Cd)
if False or run_all:
    for xs in foils['In']['reactions'].values():
        print('\n' + xs['plotname'] + '  (Cd)')
        left, right = roi(xs, phi, ya_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# uranium
if False or run_all:
    for xs in foils['U']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
        
# copper
if True or run_all:
    for xs in foils['Cu']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# titanium
if True or run_all:
    for xs in foils['Ti']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
        
# zinc
if True or run_all:
    for xs in foils['Zn']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# zirconium
if True or run_all:
    for xs in foils['Zr']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# iron
if True or run_all:
    for xs in foils['Fe']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# scandium
if True or run_all:
    for xs in foils['Sc']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# nickel
if True or run_all:
    for xs in foils['Ni']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# magnesium
if True or run_all:
    for xs in foils['Mg']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
'''
# tungsten
if True or run_all:
    for xs in foils['W']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
'''
# magnanese
if True or run_all:
    for xs in foils['Mn']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
        
# molybdenum
if True or run_all:
    for xs in foils['Mo']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# europium
if True or run_all:
    for xs in foils['Eu']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# iridium
if True or run_all:
    for xs in foils['Ir']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# dyspropium
if True or run_all:
    for xs in foils['Dy']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))

# lutetium
if True or run_all:
    for xs in foils['Lu']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
        
# chromium
if True or run_all:
    for xs in foils['Cr']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))
        
# calcium
if True or run_all:
    for xs in foils['Ca']['reactions'].values():
        print('\n' + xs['plotname'])
        left, right = roi(xs, phi, no_cd, True, True)
        print('Left: {:6.4e}'.format(left))
        print('Right: {:6.4e}'.format(right))