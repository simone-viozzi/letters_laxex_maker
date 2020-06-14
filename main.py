import string
import os

alphabeth = list(string.ascii_uppercase)

charlist = alphabeth*5 + ['A', 'E', 'I', 'O', 'U']*10 + list(string.digits)*3

wordlist = ['APE', 'UVA', 'OCA']

fontsize = "45"

latex = r"""
\RequirePackage{fix-cm}
\documentclass[fontsize=10pt,a3paper,landscape]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage[left=1cm,right=1cm,top=1.5cm,bottom=1.5cm]{geometry}
\usepackage{lmodern}
\usepackage{textcomp}

\usepackage{emerald}
\usepackage[T1]{fontenc}

\newcommand{\applyfont}{\ECFJD}


\begin{document}
\pagenumbering{gobble}
\hspace*{-6mm}
"""

i = 1
for l in charlist:
    latex += r"""\fbox{\begin{minipage}[h][5cm][c]{4.8cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
""" + l + r"""
\end{minipage}}\hspace*{-1mm}
"""
    if i % 8 == 0:
        latex += r"""\newline"""
    i += 1


latex += r"""\fbox{\begin{minipage}[h][5cm][c]{14.8cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
ISOLA
\end{minipage}}\hspace*{-1mm}
"""

eur = ['€']*3
for e in eur:
    latex += r"""\fbox{\begin{minipage}[h][5cm][c]{4.8cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
""" + e + r"""
\end{minipage}}\hspace*{-1mm}
"""

latex += r"\newline"

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{9.8cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
IERI
\end{minipage}}\hspace*{-1mm}
"""

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{14.75cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
MARIO
\end{minipage}}\hspace*{-1mm}
"""

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{12cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
OGGI
\end{minipage}}\hspace*{-1mm}
"""

latex += r"\newline"

for w in wordlist:
    latex += r"""\fbox{\begin{minipage}[h][5cm][c]{9.8cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
""" + w + r"""
\end{minipage}}\hspace*{-1mm}
"""

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{6.9cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
TU
\end{minipage}}\hspace*{-1mm}
"""

latex += r"\newline"

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{9.8cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
ETA
\end{minipage}}\hspace*{-1mm}
"""

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{20cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
DAVIDE
\end{minipage}}\hspace*{-1mm}
"""

latex += r"""\fbox{\begin{minipage}[h][5cm][c]{6cm}
\centering
\fontsize{""" + fontsize + r"""mm}{""" + fontsize + r"""mm}\selectfont
\applyfont
IO
\end{minipage}}\hspace*{-1mm}
"""


latex += r"\end{document}"

os.system("rm ./main.tex ./main.pdf ./main.aux ./main.log")

with open("main.tex", 'w') as f:
    f.write(latex)


os.system("pdflatex main.tex")
