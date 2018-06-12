import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint, quad
from scipy.interpolate import interp1d

from cross_sections import foils, Cd
from plotting import plot_activities, plot_xs
from flux_spectrum import Flux


def activity_calc(foil, m, P, t_i, t_ci, t_cf, t_f, cd_covered=False, cd_thickness=0.05, plotname='decay.png'):
    '''
    Stuff.
    '''
    reaction_list = list(foil['reactions'].values())
    reaction_names = list(foil['reactions'].keys())
    num_reactions = len(reaction_list)

    # facts of life
    Na = 6.0221409E23  # atoms / mol

    # set up N_i
    N_i = np.zeros(num_reactions + 1)
    N_i[0] = (m * 1E-3 * Na) / foil['M']

    # calculate decay constants with halflifes
    half_lives = np.ones(num_reactions + 1)
    for i, reaction in enumerate(reaction_list):
        half_lives[i+1] = reaction['halflife']
    decay_constants = np.log(2) / half_lives
    decay_constants[0] = 0

    # find normalized reaction rates
    # load in spectrum
    phi = Flux(1/0.833)

    def reaction_rate(e, phi, sigma, cd_fun):
        return (sigma(e) * 1E-24) * phi.evaluate(e) * cd_fun(e)

    if cd_covered:
        def cd(e):
            term = ((Cd['rho'] * Na) / Cd['M']) * cd_thickness * 1E-24
            cd_xs = Cd['reactions']['n,tot']['func']
            factor = np.exp(-term * cd_xs(e) * 5)
            return factor
    else:
        def cd(e):
            return 1

    R = np.zeros(num_reactions + 1)
    R[0] = 1
    total_phi = 0
    e = np.logspace(-5, 9, 100)
    for i in range(len(e) - 1):
        total_phi += quad(phi.evaluate, e[i], e[i+1])[0]
        for j, reaction in enumerate(reaction_list):
            R[j+1] += quad(reaction_rate, e[i], e[i+1], args=(phi, reaction['func'], cd))[0]
    R = R / total_phi
    R[0] = 0

    # plot xs
    plot_xs(reaction_names, reaction_list, phi.evaluate, cd)

    def decay(N, t, lam, t_i, R, P, num_reactions):
        '''
        Radioactive decay.
        '''
        phi_i = (1/100) * 4E12 * (1 + 1/0.833) * P  # flux at a certain power

        # flux info
        if t < t_i:
            phi_0 = phi_i
        else:
            phi_0 = 0

        A = np.diag(-lam)
        A[:, 0] = R * phi_0
        return A.dot(N)

    # solve
    times = np.linspace(0, t_f, 10000)
    N = odeint(decay, N_i, times, args=(decay_constants, t_i, R, P, num_reactions))
    activities = decay_constants * N

    # counting
    counts = list(np.zeros(num_reactions))  # fix this this is garbage wow
    for i, reaction in enumerate(reaction_list):
        act_fun = interp1d(times, activities[:, i+1], bounds_error=False, fill_value=0)
        counts[i] = (reaction['erg'], quad(act_fun, t_ci, t_cf)[0])

    # Bq to uCi
    activities *= (1/3.7E10) * 1E6
    total_activity = np.sum(activities, axis=1)

    # print some info
    total_act_fun = interp1d(times, total_activity, bounds_error=False, fill_value=0)
    scram_act = total_act_fun(t_i)
    count_act = total_act_fun(t_ci)
    print('Counting Activity:  {:4.2e} uCi'.format(float(count_act)))

    # plotting
    if plotname:
        plot_activities(plotname, reaction_list, times, activities, total_activity, t_i, t_ci, t_cf, False)

    return counts, scram_act, count_act


if __name__ == '__main__':
    # user defined parameters
    foil = foils['Al']
    m = 0.2  # mg
    t_s = 300  # s
    t_i = 600  # s
    t_c = 3000  # s
    t_f = 3600  # s
    P = 100  # kW(th)
    activity_calc(foil, m, P, t_s, t_i, t_c, t_f)
