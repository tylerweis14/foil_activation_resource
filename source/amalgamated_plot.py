import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

from cross_sections import foils, Cd
from flux_spectrum import Flux

# nice plotting
rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.0
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})


# set up environment
fig = plt.figure(101, figsize=(8, 4.5))
ax1 = fig.add_subplot(111)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlim(1E-5, 1E8)
ax1.set_ylim(1E1, 1E13)
ax1.set_xlabel('Energy (eV)')
ax1.set_ylabel('$\Phi$ ($cm^{-2}s^{-1}$)')

ax2 = ax1.twinx()
ax2.set_yscale('log')
ax2.set_xlim(1E-5, 1E8)
ax2.set_ylim(1E-4, 1E5)
ax2.set_ylabel('$\sigma$ ($barns$)')

# flux
flux = Flux(1/0.833)
phi = flux.evaluate
x = np.logspace(-5, 8, 1000)
powerscaling = (1/100) * 4E12 * (1 + 1/0.833) * 100  # flux 100 kW(th)
y = phi(x) * powerscaling
ax1.plot(x, y, 'k', label='$\Phi$')

reactions = [foils['Au']['reactions']['n,gamma'],
             foils['In']['reactions']['n,gamma'],
             foils['Al']['reactions']['n,alpha'],
             foils['Rh']['reactions']['n,inelastic'],
             foils['U']['reactions']['n,total_fission']]

foilnames = ['$^{197}$Au', '$^{115}$In', '$^{27}$Al', '$^{103}$Rh', '$^{235}$U']

colors = ['green', 'orange', 'red', 'blue', 'indigo']
linestyles = [':', '--', '-', ':', '-.']
heights = np.array([1e-7, 1e-8, 1e-4, 1e-3, 1e-9]) * powerscaling

for i, reaction in enumerate(reactions):
    # region
    roi = reaction['roi']
    l = reaction['label']
    f = foilnames[i]
    ax1.plot(roi, [heights[i]]*2, color=colors[i], linewidth=2.0)
    ax1.text(roi[0]*0.4, heights[i]*2, f+' '+l)

    # cross section
    xs = reaction['func']
    region = reaction['region']
    reg = np.geomspace(*region, 1000)[:-1]
    ax2.plot(reg, xs(reg), color=colors[i], label=f+' '+l, linestyle=linestyles[i])

fig.savefig('plot/amalgamated.png', dpi=500)
