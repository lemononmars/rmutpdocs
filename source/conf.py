# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ภาระงานบุคลากรสายวิชาการ'
copyright = '2020, Sakulbuth Ekvittayaniphon'
author = 'คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชมงคลพระนคร'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme
extensions = ['recommonmark','sphinx_rtd_theme']
# , 'sphinx_togglebutton' to be added back later.....

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'th'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
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

\AtBeginDocument\captionsthai % Force the caption to Thai
    ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
}
latex_show_urls = 'footnote'

