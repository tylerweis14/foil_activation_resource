from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import numpy as np


def plot_activities(foil, t, activity, experimentname, node):
    rc('font', **{'family': 'serif'})
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    rcParams['xtick.labelsize'] = 18
    rcParams['ytick.labelsize'] = 18
    rcParams['lines.linewidth'] = 1.85
    rcParams['axes.labelsize'] = 20
    rcParams.update({'figure.autolayout': True})

    fig = plt.figure(node)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Activity ($\mu$Ci)')
    ax.set_yscale('log')
    ax.set_ylim(1E-5, np.max(activity) * 1.3)

    # plot individual activities
    ax.plot(t, activity, 'k', label=foil.label)

    plt.legend()
    plt.savefig('plot/' + foil.plotname + '_' + experimentname + str(node) + '.pdf')
    plt.close(fig)
    return


def plot_xs(foil, phi):

    fig = plt.figure(11)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('$\sigma$ ($b$)')
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_xlim(1E-5, 1E9)

    # plot total activity
    x = np.logspace(-5, 9, 1000)
    xs = foil.func
    y = xs(x)

    ax.set_ylim(1E-8 * max(y), 10 * max(y))

    ax.plot(x, y, 'k')

    plt.legend()
    figname = 'plot/' + foil.plotname + '.pdf'
    plt.savefig(figname)
    plt.close(fig)
    return
