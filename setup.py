import os
import subprocess
from setuptools import setup

from packageinfo import VERSION, NAME


def generate_pdf(self):
    path = os.path.join('docs', 'build', 'latex')
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
    keywords='simphony, documentation, sphinx, Fraunhofer IWM',
    long_description=README_TEXT,
)
