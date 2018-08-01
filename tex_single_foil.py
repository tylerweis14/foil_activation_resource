import numpy as np
from cross_sections import foils
from tex_template import tex_template


def time_change(t):
    '''
    Converts time to easily readable format.
    '''
    if t > 86400:
        return '{:4.1f} d'.format(t / 86400)
    elif t > 3600:
        return '{:4.1f} h'.format(t / 3600)
    elif t > 60:
        return '{:4.1f} m'.format(t / 60)
    else:
        return '{:4.1f} s'.format(t)


def write_single_foil(foil, power, t_irrad, t_wait, t_count, A_rem, A_count, masses, counts, experimentname='theoretical'):
    '''
    Do something.
    '''

    title_s = foil.label
    irrad_s = ''
    for i in range(4):
        err = (np.sqrt(counts[i]) / counts[i]) * 100
        irrad_s += '\n {} & {:4.2f} & {:4.2e} & {:4.2e} & {:6.4f} \\\\ \n'.format(i+1, masses[i], A_count[i], counts[i], err)
        irrad_s += '\\hline'

    activity_plot = 'plot/' + foil.plotname + '_' + experimentname + '1'

    p = 'plot/' + foil.plotname
    reaction_s = '   \\includegraphics[width=.8\\textwidth]{{{}}} \n'.format(p)
    activity_plot_s = '   \\includegraphics[width=.8\\textwidth]{{{}}} \n'.format(activity_plot)

    # reaction table
    reaction_table_s = ''
    s0 = foil.label
    s1 = time_change(foil.halflife)
    s2 = '{:4.2e}, {:4.2e}'.format(*foil.roi)
    s3 = '{}({})'.format(foil.erg, foil.BR)
    reaction_table_s += '\n {} & {} & {} & {} \\\\ \n'.format(s0, s1, s2, s3)
    reaction_table_s += '\\hline'

    # format the template with all of the strings
    blanks = [title_s, power, time_change(t_irrad), time_change(t_wait), time_change(t_count),
              A_rem, irrad_s, activity_plot_s, reaction_s, reaction_table_s]
    single_foil = tex_template.format(*blanks)
    filename = foil.plotname + '_{}.tex'.format(experimentname)
    with open('plot/' + filename, 'w+') as F:
        F.write(single_foil)
    return

if __name__ == '__main__':
    mat = 'Au'
    cd_cov = False
    masses = np.array([5.0, 4.35, 4.30, 4.37])  # mg
    t_i = 45  # s
    t_w = 345  # s
    counting_time = 300
    t_f = 3600  # s
    P = 100  # kW(th)
    A_r = 9.62e+02
    A_c = [9.62e+01, 9.72e+03, 9.62e+02, 5.62e+03]

    write_single_foil('indium', P, t_i, t_w, counting_time, A_r, A_c, masses, 'In')
