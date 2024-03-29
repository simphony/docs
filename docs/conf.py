"""Configuration file for the Sphinx documentation builder."""

# Project information
project = "SimPhoNy"
# Version is given in setuptools
copyright = "2022, Materials Informatics team at Fraunhofer IWM"
author = "Materials Informatics team at Fraunhofer IWM"

# General configuration
extensions = [
    "myst_parser",  # markdown source support
    "sphinx.ext.autodoc",  # API ref
    "sphinx.ext.napoleon",  # API ref Google and NumPy style
    "sphinx.ext.viewcode",  # API link to source
    "sphinx.ext.graphviz",  # Graphviz
    "sphinxcontrib.plantuml",  # PlantUml
    "sphinx_copybutton",  # Copy button for codeblocks
    "nbsphinx",  # Jupyter
    "IPython.sphinxext.ipython_console_highlighting",  # nb syntax highlight
    "sphinx.ext.autosectionlabel",  # Auto-generate section labels.
    "sphinx_panels",  # Create panels in a grid layout or as drop-downs
]

master_doc = "index"

myst_heading_anchors = 5

plantuml = "java -jar _static/plantuml.jar"
plantuml_output_format = "svg_img"

suppress_warnings = ["autosectionlabel.*"]
exclude_patterns = ["**.ipynb_checkpoints"]

# HTML output
html_theme = "sphinx_book_theme"
html_favicon = "_static/simphony_favicon.png"
html_logo = "_static/simphony_logo_dark.png"
html_theme_options = {
    "github_url": "https://github.com/simphony/docs",
    "repository_url": "https://github.com/simphony/docs",
    "use_repository_button": True,
    "repository_branch": "main",
    "path_to_docs": "docs",
    "logo_only": True,
    "show_navbar_depth": 1,
}


html_static_path = ["_static"]
html_css_files = ["custom.css"]


# LaTeX output
latex_documents = [
    (
        "index",
        "SimPhoNy_docs.tex",
        "SimPhoNy documentation",
        "Materials Data Science and Informatics team at Fraunhofer IWM",
        "manual",
        "false",
    )
]
latex_logo = "_static/simphony_logo_dark.png"
latex_elements = {"figure_align": "H"}

nbsphinx_allow_errors = True


def setup(app):
    import simphony_osp.development
    import simphony_osp.ontology
    import simphony_osp.session

    # Override names and modules of members of "simphony_osp.ontology" in the
    # API reference.
    for obj in simphony_osp.ontology.__all__:
        item = getattr(simphony_osp.ontology, obj)
        setattr(item, "__name__", obj)
        setattr(item, "__module__", simphony_osp.ontology.__name__)

    # Override names and modules of members of "simphony_osp.session" in the
    # API reference.
    for obj in simphony_osp.session.__all__:
        item = getattr(simphony_osp.session, obj)
        setattr(item, "__name__", obj)
        setattr(item, "__module__", simphony_osp.session.__name__)

    # Override names and modules of members of "simphony_osp.development" in
    # the API reference.
    for obj in simphony_osp.development.__all__:
        item = getattr(simphony_osp.development, obj)
        setattr(item, "__name__", obj)
        setattr(item, "__module__", simphony_osp.development.__name__)
