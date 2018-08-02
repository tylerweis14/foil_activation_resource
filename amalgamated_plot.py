import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from flux import select_flux_spectrum


def amalgamate(experimentname, element_names, foil_library, source, P):
    source_sf = 1
    if source == 'triga_nebp':
        source_sf = 1e-4

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
    ax1.set_xlim(1E-5, 1E9)
    ax1.set_ylim(1E2 * source_sf, 1E18 * source_sf)
    ax1.set_xlabel('Energy (eV)')
    ax1.set_ylabel('$\Phi$ ($cm^{-2}s^{-1}$)')

    ax2 = ax1.twinx()
    ax2.set_yscale('log')
    ax2.set_xlim(1E-5, 1E9)
    ax2.set_ylim(1E-6, 1E8)
    ax2.set_ylabel('$\sigma$ ($barns$)')

    # flux
    x = np.logspace(-5, 8, 1000)
    flux = select_flux_spectrum(source, P)[2]
    y = flux(x)
    ax1.plot(x, y, 'k', label='$\Phi$')

    colors = ['green', 'gold', 'red', 'blue', 'indigo', 'fuchsia', 'black',
              'coral', 'slategrey', 'darkcyan', 'blueviolet', 'lawngreen',
              'lightsalmon', 'maroon', 'cyan', 'papayawhip', 'chocolate',
              'darkkhaki']
    linestyles = [':', '--', '-', ':', '-.', ':', '--', '-', ':', '-.', '-', ':', '--',
                  '-.', ':', '--', '-.', ':']

    resonance = []
    threshold = []
    for key, foil in foil_library.items():
        if key in element_names:
            if foil.classification == 'resonance':
                resonance.append(foil)
            else:
                threshold.append(foil)
    resonance = sorted(resonance, key=lambda x: -(np.log(x.roi[1]) - np.log(x.roi[0])))
    threshold = sorted(threshold, key=lambda x: np.log(x.roi[1]) - np.log(x.roi[0]))

    res_heights = np.array([1e3, 1e4, 1e5, 1e6, 1e7, 1e14, 1e15, 1e16, 1e17]) * 0.5 * source_sf
    thresh_heights = np.geomspace(1e10, 1e17, 8) * source_sf

    i = 0
    new_resonance = []
    for r in range(len(resonance)):
        new_resonance.append(res_heights[i])
        if (r+1) % 2:
            i += 1
        i *= -1
    res_heights = np.sort(new_resonance)

    for i, foil in enumerate(resonance):
        # cross section
        xs = foil.func
        region = foil.region
        reg = np.geomspace(*region, 1000)[:-1]
        ax2.plot(reg, xs(reg), color=colors[i], label=foil.label, linestyle=linestyles[i])

        # region
        ax1.plot(foil.roi, [res_heights[i]]*2, color=colors[i], linewidth=2.0)
        ax1.text(foil.roi[0]*0.4, res_heights[i]*2, foil.label)

    for i, foil in enumerate(threshold):
        l = len(resonance)
        # region
        ax1.plot(foil.roi, [thresh_heights[i]]*2, color=colors[i+l], linewidth=2.0)
        ax1.text(foil.roi[0]*0.1, thresh_heights[i]*2, foil.label)

        # cross section
        xs = foil.func
        region = foil.region
        reg = np.geomspace(*region, 1000)[:-1]
        ax2.plot(reg, xs(reg), color=colors[i+l], label=foil.label, linestyle=linestyles[i+l])

    fig.savefig('plot/amalgamated_{}.png'.format(experimentname), dpi=500)
