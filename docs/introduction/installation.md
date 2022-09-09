# Installation

For the installation and usage of SimPhoNy,
[Python 3.7 or higher](https://www.python.org/downloads/) is
required. SimPhoNy is
[available on PyPI](https://pypi.org/project/simphony-osp/), so it can be
installed using the [`pip` package manager](https://pip.pypa.io/en/stable/).

```shell
pip install osp-core
```

## Wrapper installation

SimPhoNy Wrappers are distributed as separate Python packages. Typically,
installing them also involves just installing a package either from the Python
Package Index or a different source. However, sometimes it can be
more complicated than that. Head to each wrapper's website for specific installation
instructions.

[//]: # "TODO: link to list of wrappers somewhere in the documentation"

## Developers

If you are a developer or an advanced user, you might be interested in
installing OSP-core from source.

```shell
git clone https://github.com/simphony/simphony-osp.git
pip install ./simphony-osp

```

Note that it is also possible to install Python packages in
[_development mode_](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode),
meaning that their source code can be edited in-place without needing to
reinstall them to see the changes.

```sh
# development mode installation
pip install -e ./simphony-osp
```
