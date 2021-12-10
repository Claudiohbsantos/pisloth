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
import sphinx_rtd_theme

project = 'Emakefun pisloth'
copyright = '2021, Emakefun'
author = 'Emakefun'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# SunFounder logo

# html_js_files = [
#     'https://ezblock.cc/readDocFile/topHead.js',
# ]
# html_css_files = [
#     'https://ezblock.cc/readDocFile/topHead.css',
# ]

#### RTD+

html_js_files = [
    'https://ezblock.cc/readDocFile/topHead.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
   'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',

]
html_css_files = [
   'https://ezblock.cc/readDocFile/topHead.css',
   'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
   'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.





latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
'preamble': r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK}{UTF8}{gbsn}
\AtEndDocument{\end{CJK}}
''',
}