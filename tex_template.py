tex_template = '''\\newpage

\\section*{{Aluminum}}

Power Level: 250.0 kW(th) \\\\
Time at Power: 3600 s \\\\
Wait Time: 1800 s \\\\
Total Activity at Removal: 9.62e+02 $\\mu Ci$

\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ |c|c|c|c|c|c|c| }}
 \\hline
 Position & Mass $mg$ & Start Counting $s$ & Counting Time $s$ & Counting Activity $\\mu Ci$ \\\\
 \\hline
 1 & 0.3 & 10800 & 1800 & 1.92e-01\\\\
 \\hline
 2 & 0.2 & 12600 & 1800 & 1.75e-02\\\\
 \\hline
 3 & 0.1 & 14400 & 1800 & 3.83e-03\\\\
 \\hline
 4 & 0.2 & 16200 & 1800 & 6.44e-03\\\\
 \\hline
\\end{{tabular}}
\\end{{table*}}

\\begin{{figure}}[!ht]
   \\centering
   \\subfloat[][Position \\#1]{{\\includegraphics[width=.4\\textwidth]{{al1_activity}}}}\\quad
   \\subfloat[][(n,$\\gamma$) Reaction Rate]{{\\includegraphics[width=.4\\textwidth]{{al_n_gamma}}}}\\\\
   \\subfloat[][(n,$\\alpha$) Reaction Rate]{{\\includegraphics[width=.4\\textwidth]{{al_n_alpha}}}}\\quad
   \\subfloat[][(n,p) Reaction Rate]{{\\includegraphics[width=.4\\textwidth]{{al_n_p}}}}
   \\label{{fig:aluminum}}
\\end{{figure}}

\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ |c|c|c|c|c|c|c| }}
 \\hline
 Reaction & T$_{{1/2}}$ & ROI (eV) & Important Gammas (keV) \\\\
 \\hline
 $^{{27}}$Al(n,$\\gamma$)$^{{28}}$Al & 2.246 m & 2.8233e-03, 4.1509e-01 & 1780(1.0) \\\\
 \\hline
 $^{{27}}$Al(n,$\\alpha$)$^{{24}}$Na & 15.03 h & 6.4564e+06, 1.1695e+07 & 1369(1.0), 2754(1.0) \\\\
 \\hline
 $^{{27}}$Al(n,p)$^{{27}}$Mg & 9.458 m & 3.4248e+06, 9.1383e+06 & 180(0.007), 840(0.7), 1013(0.3) \\\\
 \\hline
\\end{{tabular}}
\\end{{table*}}
'''
