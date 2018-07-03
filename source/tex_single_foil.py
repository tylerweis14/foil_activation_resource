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


def write_single_foil(title, power, t_irrad, t_wait, t_count, A_rem, A_count, masses, foilkey, counts, cd=False):
    '''
    Do something.
    '''

    foil = foils[foilkey]

    if cd:
        title_s = title.capitalize() + '  (Cd)'
    else:
        title_s = title.capitalize()
    irrad_s = ''
    for i in range(4):
        t = t_irrad + t_wait + t_count * i
        irrad_s += '\n {} & {} & {} & {} & {:4.2e} & {:4.2e}\\\\ \n'.format(i+1, masses[i], t, t_count, A_count[i], counts[i])
        irrad_s += '\\hline'

    cdplot_s = ''
    if cd:
        cdplot_s = 'cd'
    activity_plot_s = 'source/plot/{}1{}_activity'.format(foilkey.lower(), cdplot_s)

    reaction_s = ''
    for i, reaction in enumerate(foil['reactions'].values()):
        l, p = reaction['label'], 'source/plot/' + reaction['plotname']
        if cd:
            p += '_cd'
        quad = '\\\\'
        if i == 1:
            quad = '\\quad'
        reaction_s += '   \\subfloat[][ {} Reaction Rate]{{\\includegraphics[width=.4\\textwidth]{{{}}}}}{} \n'.format(l, p, quad)

    # reaction table
    reaction_table_s = ''
    for reaction in foil['reactions'].values():
        s0 = reaction['label']
        s1 = time_change(reaction['halflife'])
        s2 = '{:4.2e}, {:4.2e}'.format(*reaction['roi'])
        if cd:
            s2 = '{:4.2e}, {:4.2e}'.format(*reaction['roi_cd'])
        s3 = ''
        for lam, e in reaction['erg']:
            s3 += '{}({}), '.format(e, lam)
        s3 = s3[:-2]
        reaction_table_s += '\n {} & {} & {} & {} \\\\ \n'.format(s0, s1, s2, s3)
        reaction_table_s += '\\hline'

    # format the template with all of the strings
    blanks = [title_s, power, t_irrad, t_wait, A_rem, irrad_s, activity_plot_s, reaction_s, reaction_table_s]
    single_foil = tex_template.format(*blanks)
    if cd:
        filename = title.lower() + '_cd.tex'
    else:
        filename = title.lower() + '.tex'
    with open(filename, 'w+') as F:
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
