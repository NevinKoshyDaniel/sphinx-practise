# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Nevin's Sphinx Profile"
copyright = '2023, Nevin K Daniel'
author = 'Nevin K Daniel'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

project = "Sphinx Engine Practise"
extensions = ['myst_parser', 'sphinx_rtd_theme', 'notfound.extension']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','.venv']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Enable numref
numfig = True
