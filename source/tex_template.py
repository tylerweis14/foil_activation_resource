tex_template = '''\\newpage

\\section*{{ {} }}

Power Level: {} kW(th) \\\\
Time at Power: {} \\\\
Wait Time: {} \\\\
Counting Time: {} \\\\
Total Activity at Removal: {:4.2e} $\\mu Ci$

\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ |c|c|c|c|c|c| }}
 \\hline
 Position & Mass $mg$ & Counting Activity $\\mu Ci$ & Area (Counts) & Error \% \\\\
 \\hline {}
\\end{{tabular}}
\\end{{table*}}

\\begin{{figure}}[h]
\\centering
\\begin{{subfigure}}{{.5\\textwidth}}
  \\centering
  {}
  \\caption{{A subfigure}}
  \\label{{fig:sub1}}
\\end{{subfigure}}%
\\begin{{subfigure}}{{.5\\textwidth}}
  \\centering
  {}
  \\caption{{A subfigure}}
  \\label{{fig:sub2}}
\\end{{subfigure}}
\\caption{{A figure with two subfigures}}
\\label{{fig:test}}
\\end{{figure}}

\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ |c|c|c|c|c|c|c| }}
 \\hline
 Reaction & T$_{{1/2}}$ & ROI (eV) & Important Gammas (keV) \\\\
 \\hline {}
\\end{{tabular}}
\\end{{table*}}
'''
