import numpy as np
from scipy.integrate import odeint, quad
from scipy.interpolate import interp1d
from plotting import plot_activities, plot_xs
from flux import select_flux_spectrum
from hpge import hpge_efficiency


def activity_calc(foil, m, P, t_i, t_ci, t_cf, t_f, detector, source,
                  plotname='decay.png', node=1, experimentname='theoretical'):
    '''
    Stuff.
    '''
    # facts of life
    Na = 6.0221409E23  # atoms / mol

    # set up N_i
    N_i = np.zeros(2)
    N_i[0] = ((m * 1E-3 * Na) / foil.M) * foil.abundance

    # calculate decay constants with halflifes
    decay_constants = np.array([0, foil.decay_constant])

    # load in spectrum
    phi = select_flux_spectrum(source, P)[node]

    def reaction_rate(e, phi, sigma):
        return (sigma(e) * 1E-24) * phi(e)

    R = np.zeros(2)
    R[0] = 1
    total_phi = 0
    e = np.logspace(-5, 9, 100)
    for i in range(len(e) - 1):
        total_phi += quad(phi, e[i], e[i+1])[0]
        R[1] += quad(reaction_rate, e[i], e[i+1], args=(phi, foil.func))[0]
    R[0] = 0

    plot_xs(foil, phi)

    def decay(N, t, lam, t_i, R, P):
        '''
        Radioactive decay.
        '''
        phi_i = 1  # flux at a certain power

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
    N = odeint(decay, N_i, times, args=(decay_constants, t_i, R, P))
    activities = decay_constants * N

    # counting
    act_fun = interp1d(times, activities[:, 1], bounds_error=False, fill_value=0)
    raw = quad(act_fun, t_ci, t_cf)[0]
    detected = raw * foil.BR
    detected *= hpge_efficiency[detector](foil.erg)
    counts = detected

    # Bq to uCi
    activities *= (1/3.7E10) * 1E6
    total_activity = np.sum(activities, axis=1)

    # print some info
    total_act_fun = interp1d(times, total_activity, bounds_error=False, fill_value=0)

    scram_act = total_act_fun(t_i)
    count_act = total_act_fun(t_ci)
    print('Counting Activity:  {:4.2e} uCi'.format(float(count_act)))

    if plotname:
        plot_activities(foil, times, activities, experimentname, node)

    return counts, scram_act, count_act
