import os
import subprocess
from setuptools import setup
from sphinx.setup_command import BuildDoc

from packageinfo import VERSION, NAME, OSP_CORE_MIN, OSP_CORE_MAX


source_dir = os.path.join('docs', 'source')
build_dir = os.path.join('docs', 'build')

# Create custom build that also compiles the LaTeX
class CustomBuild(BuildDoc):
    def run(self):
        super().run()
        path = os.path.join(build_dir, 'latex')
        subprocess.check_call(["make", "-C", path])


# Read description
with open('README.md', 'r') as readme:
    README_TEXT = readme.read()

# main setup configuration class
setup(
    name=NAME,
    version=VERSION,
    author='Materials Data Science and Informatics team at Fraunhofer IWM',
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
    cmdclass={'install': CustomBuild},
    command_options={
        'install': {
            'version': ('setup.py', VERSION),
            'release': ('setup.py', VERSION),
            'source_dir': ('setup.py', source_dir),
            'build_dir': ('setup.py', build_dir),
            'builder': ('setup.py', 'html, latex'),
            },
        },
)
