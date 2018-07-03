tex_template = '''\\newpage

\\section*{{ {} }}

Power Level: {} kW(th) \\\\
Time at Power: {} s \\\\
Wait Time: {} s \\\\
Total Activity at Removal: {:4.2e} $\\mu Ci$

\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ |c|c|c|c|c|c|c| }}
 \\hline
 Position & Mass $mg$ & Start Counting $s$ & Counting Time $s$ & Counting Activity $\\mu Ci$ & Expected Area (Counts) \\\\
 \\hline {}
\\end{{tabular}}
\\end{{table*}}

\\begin{{figure}}[!ht]
   \\centering
   \\subfloat[][Position \\#1]{{\\includegraphics[width=.4\\textwidth]{{{}}}}}\\quad
{}
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
