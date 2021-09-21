# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'SimPhoNy'
# Version is given in setuptools
copyright = ('2021, Materials Data Science and '
             'Informatics Team at Fraunhofer IWM')
author = 'Materials Data Science and Informatics team at Fraunhofer IWM'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',  # markdown source support
    'sphinx.ext.autodoc',  # API ref
    'sphinx.ext.napoleon',  # API ref Google and NumPy style
    'sphinx.ext.viewcode',  # API link to source
    'sphinx.ext.graphviz',  # Graphviz
    'sphinxcontrib.plantuml',  # PlantUml
    'sphinx_copybutton',  # Copy button for codeblocks
    'nbsphinx',  # Jupyter
    'IPython.sphinxext.ipython_console_highlighting',  # nb syntax highlight
    'sphinx.ext.autosectionlabel',  # Auto-generate section labels.
    'sphinx_panels'  # Create panels in a grid layout or as drop-downs
]

master_doc = 'index'

plantuml = 'java -jar lib/plantuml.jar'
plantuml_output_format = 'svg_img'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_favicon = '_static/img/simphony_favicon.png'
html_logo = '_static/img/simphony_logo_light.png'
html_static_path = ['_static']


# -- Options for LaTeX output -------------------------------------------------
latex_documents = [('index',
                    'SimPhoNy_docs.tex',
                    'SimPhoNy documentation',
                    ('Materials Data Science and '
                     'Informatics team at Fraunhofer IWM'),
                    "manual",
                    "false",)]
latex_logo = '_static/img/simphony_logo_dark.png'
latex_elements = {'figure_align': 'H'}

nbsphinx_allow_errors = True
