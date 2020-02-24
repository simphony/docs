from setuptools import setup

from packageinfo import VERSION, NAME, OSP_CORE_MIN, OSP_CORE_MAX

# Read description
with open('README.md', 'r') as readme:
    README_TEXT = readme.read()


# main setup configuration class
setup(
    name=NAME,
    version=VERSION,
    author='Material Informatics Team, Fraunhofer IWM.',
    url='www.simphony-project.eu',
    description='The SimPhoNy documentation',
    keywords='simphony, documentation, sphinx, cuds, Fraunhofer IWM',
    long_description=README_TEXT,
    install_requires=[
        'osp-core>=' + OSP_CORE_MIN + ', <' + OSP_CORE_MAX,
        'sphinx',
        'recommonmark',
        'sphinxcontrib-plantuml',
        'nbsphinx',
        'sphinx-copybutton',
        'ipython',
    ],
    setup_requires=[
        'sphinx',
    ],
)
