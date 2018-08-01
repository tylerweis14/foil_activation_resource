import theoretical_6_25_18
import experimental_6_25_18


def compare_set(theo, exp, area=True, activity=False):
    # grab the keys for the foils that have data
    good_data = []
    for key, value in exp.items():
        if value.peak_area != -1:
            good_data.append(key)

    # do it
    for name in good_data:
        if name in theo:
            print('\n {}'.format(name))
            print('    Theo      Exp     Ratio')
            if area:
                t = int(theo[name].peak_area)
                e = int(exp[name].peak_area)
                r = e / t
                print('{:8} {:8} {:8.4f}'.format(t, e, r))


compare_set(theoretical_6_25_18.data, experimental_6_25_18.data)
