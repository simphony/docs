# Installation

For the installation and usage of the framework Python 3.6 or higher is
needed. We _highly_ encourage the use of a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
or a [conda](https://docs.conda.io/en/latest/) environment.

```shell
# virtual environment
python3 -m venv SimPhoNy
source SimPhoNy/bin/activate
```

```shell
# conda
conda create -n <env_name>
conda activate <env_name>
```

OSP-core is available on PyPI, so it can be installed using `pip`:

```shell
pip install osp-core
```

For an installation from source, see [here](#installing-osp-core-from-source).

After installing OSP-core, you can install your ontology namespaces.
We provide the [`pico`](utils.md#pico) tool for that purpose.

```sh
pico install <path/to/ontology.yml>

# If you have issues using pico directly, you can use
python -m osp.core.pico install <path/to/ontology.yml>
```

## Wrapper installation

Wrappers are currently not available on PyPI, so they must be installed
from source. First, the repository is cloned:

```shell
git clone https://github.com/simphony/<some-wrapper>.git
cd some-wrapper
```

### Local wrapper installation

With OSP-core installed, if the wrapper has its own ontology, it _must_ be installed:

```shell
pico install <path/to/ontology.yml>
```

For the wrappers that require the installation of a backend, a `install_engine.sh` script is usually provided.
It will automatically call `install_engine_requirements.sh`, where the engine specific requirements are installed.

```shell
./install_engine.sh
```

Now, the wrapper can be installed:

```shell
pip install .
```

### Wrapper Docker image

Some wrappers also provided a [Dockerfile](https://docs.docker.com/engine/reference/builder/)
for an automatic installation in a container.
The dockerfile should contain the information needed to run it inside.

## Installing OSP-core from source

If you are a developer or an advanced user, you might be interested in
installing OSP-core from source.

To do so, first the repository must be cloned:

```shell
git clone https://github.com/simphony/osp-core.git
cd osp-core
```

The installation is based on setuptools:

```sh
# build and install (recommended)
pip install .

# alternative
python3 setup.py install
```

or:

```sh
# build for in-place development (recommended)
pip install -e .

# alternative
python3 setup.py develop
```
