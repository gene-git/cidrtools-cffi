# 
# Docs/conf.py
#
import os
import sys
import subprocess

def read_version() -> str:
    """ load the version.txt file"""
    file = '../../version.txt'
    if os.path.exists(file):
        with open(file, 'r') as fob:
            proj_vers = fob.readlines()[0]
    else:
        proj_vers = '0.1.0-unknown'
    return proj_vers

sys.path.insert(0, os.path.abspath("../../"))

project = "cidrtools-cffi"
author = 'Gene C'

release = read_version()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.imgconverter',
]


#
# latex
#
#pygments_style = 'sphinx'
latex_use_xindy = True
latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',

    'fvset': r'\fvset{fontsize=\scriptsize}',

    'fontpkg': r'''
        \usepackage{fontspec}

        \setmainfont{Source Sans 3}[Ligatures=TeX]
        \setsansfont{Source Sans 3}[Ligatures=TeX]
        \setmonofont{Source Code Pro}
    ''',


    'preamble': r'''
        \usepackage{parskip}

        \setlength{\headheight}{14pt}
        \addtolength{\topmargin}{-2pt}

        \usepackage{enumitem}
        \setlist[itemize]{
            noitemsep,
            topsep=6pt,
            parsep=0pt,
            partopsep=0pt,
            after=\vspace{0pt}
        }
        \setlist[enumerate]{
            noitemsep,
            topsep=6pt,
            parsep=0pt,
            partopsep=0pt,
            after=\vspace{0pt}
        }

        \usepackage{newunicodechar}
        \newunicodechar{␣}{\textvisiblespace}
        \tracinglostchars=0

        ''',
}

# Grouping the document tree into a single LaTeX document manual volume.
# Tuple structure: (source start file, target name, title, author, documentclass)
latex_documents = [
    (
        'index',
        'cidrtools-cffi.tex',
        'cidrtools-cffi API Reference',
        'Gene C',
        'manual'
    ),
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [ 'custom.css',]

