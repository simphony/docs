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
# import osp.core.cuds
from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'SimPhoNy docs'
copyright = '2020, Materials Data Science and Informatics team at Fraunhofer IWM'
author = 'Materials Data Science and Informatics team at Fraunhofer IWM'

# The full version, including alpha/beta/rc tags
release = '2.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',  # md
    'sphinx.ext.autodoc',  # API ref
    'sphinx.ext.napoleon', # API ref Google and NumPy style
    'sphinx.ext.graphviz',  # Graphviz
    'sphinxcontrib.plantuml',  # PlantUml
    'nbsphinx',  # Jupyter
    'sphinx_copybutton',  # Jupyter - Copy button
    'IPython.sphinxext.ipython_console_highlighting',  # Jupyter - Syntax highlight workaround
    'sphinx.ext.autosectionlabel',  # Auto-generate section labels.
]

plantuml = 'java -jar lib/plantuml.jar'

# -- Options for LaTeX output -------------------------------------------------
latex_documents = [('index',
                    'SimPhoNy_docs.tex',
                    'SimPhoNy documentation',
                    'Materials Data Science and Informatics team at Fraunhofer IWM',
                    "manual",
                    "false",
                    ),]
latex_logo = '_static/img/simphony_logo_dark.png' 

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'
html_theme_options = {
    "stickysidebar": "true", 
    # "bgcolor": "#11303D", 
    } 
html_favicon = '_static/img/simphony_favicon.png'
html_logo = '_static/img/simphony_logo_light.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    # Configuration for recommonmark
    app.add_config_value('recommonmark_config', {
        # 'auto_toc_tree_section': 'Contents',
        # 'enable_math': False,
        # 'enable_inline_math': False,
        'auto_toc_maxdepth': 2,
        'enable_eval_rst': True,
        # 'enable_auto_doc_ref': True,
    }, True)
    app.add_transform(AutoStructify)
