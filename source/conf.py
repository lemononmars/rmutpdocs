# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'ภาระงานบุคลากรสายวิชาการ'
copyright = '2020, Sakulbuth Ekvittayaniphon'
author = 'คณะวิทยาศาสตร์และเทคโนโลยี \\ มหาวิทยาลัยราชมงคลพระนคร'


# -- General configuration ---------------------------------------------------

extensions = ['sphinx_rtd_theme']
# , 'sphinx_togglebutton' to be added back later.....

templates_path = ['_templates']
language = 'th'
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'fontpkg': r'''
\setmainfont{TeX Gyre Termes}
\setsansfont{TeX Gyre Heros}
\setmonofont{TeX Gyre Cursor}
    ''',
    'preamble': r'''

\setcounter{tocdepth}{1}

\usepackage{titlesec}
\usepackage{tocloft}
\renewcommand\numberline[1]{}

\renewcommand{\chaptername}{}
\renewcommand{\thechapter}{}

\titleformat{\section}
{\normalfont%
\vspace{6pt}%
\sffamily\bfseries\Large}
{}
{.5em}
{}

\titleformat{\subsection}
{\normalfont}
{}
{8pt}
{\Large\bfseries}

\XeTeXlinebreaklocale ”th”
\XeTeXlinebreakskip = 0pt plus 0pt

\usepackage{fontspec}
\defaultfontfeatures{Mapping=tex-text}

\newfontfamily{\thaifont}[Scale=MatchUppercase,Mapping=textext]{TH Sarabun New}
\newenvironment{thailang}{\thaifont}{}
\usepackage[Latin,Thai]{ucharclasses}

\setTransitionTo{Thai}{\begin{thailang}}
\setTransitionFrom{Thai}{\end{thailang}}

\usepackage{setspace}

\usepackage{polyglossia}
\setdefaultlanguage{english}
\setotherlanguage{thai}

\AtBeginDocument\captionsthai
    ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
}
latex_show_urls = 'footnote'

