experiment_template='''\\documentclass[a4paper, 11pt]{article}
\\usepackage{comment} % enables the use of multi-line comments (\ifx \fi) 
\\usepackage{fullpage} % changes the margin
\\usepackage{graphicx}
\\usepackage{amsmath}
\\usepackage{hyperref}
\\usepackage{caption}
\\usepackage{subcaption}
\\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
}

\\begin{document}
\\thispagestyle{empty}
%Header-Make sure you update this information!!!!
\\noindent
\\large\\textbf{MPFD Foil Activation Experiment Resource} \\\\
\\hfill John Boyington \\\\
\\hfill Kansas State University \\\\

\\vspace{0.005\\textheight}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                       Principle Reactions
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\section*{Plot}


\\begin{figure}[!ht]
   \\centering
   \\includegraphics[width=1.0\\textwidth]{SPLIT}
   \\label{fig:amalgamated}
\\end{figure}



\\newpage


SPLIT

\\end{document}
'''
