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
import os
import sys
import matplotlib as mpl
sys.path.insert(0, os.path.abspath('../smps/'))

mpl.use("Agg")

# -- Project information -----------------------------------------------------

project = 'py-smps'
author = 'QuantAQ, Inc.'

import time
if time.strftime("%Y") != "2020":
    copyright = '2020-{}, {}'.format(time.strftime("%Y"), author)
else:
    copyright = '{}, {}'.format(time.strftime("%Y"), author)

# The full version, including alpha/beta/rc tags
import toml
f = toml.load("../pyproject.toml")
version = f['tool']['poetry']['version']
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    "sphinx_copybutton",
    "matplotlib.sphinxext.plot_directive",
    "myst_parser",
    "numpydoc",
    # 'recommonmark',
]

autosummary_generate = True
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints', 'usage/.ipynb_checkpoints']


pygments_style = 'sphinx'

# We need headers to be linkable to so ask MyST-Parser to autogenerate anchor IDs for
# headers up to and including level 3.
myst_heading_anchors = 3

# Prettier support formatting some MyST syntax but not all, so let's disable the
# unsupported yet still enabled by default ones.
myst_disable_syntax = [
    "myst_block_break",
    "myst_line_comment",
    "math_block",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
