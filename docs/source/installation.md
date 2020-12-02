# Installation
For the installation and usage of the framework Python 3.6 or higher is needed.
We *highly* encourage the use of a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

```shell
~/test$ python3 -m venv SimPhoNy
~/test$ source SimPhoNy/bin/activate
(SimPhoNy) ~/test$ 
```

## OSP-core installation
First, the repository must be cloned:

```shell
git clone git@github.com:simphony/osp-core.git
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

After installing OSP-core, you can install your ontology namespaces.
We provide the tool [`pico`](./utils.md#pico-installs-cuds-ontologies)
(**p**ico **i**nstalls **c**uds **o**ntologies) for that purpose.

```sh
pico install <path/to/ontology.yml>

# If you have issues using pico directly, you can use
python -m osp.core.pico install <path/to/ontology.yml>
```

## Wrapper installation
The installation of a wrapper is similar. First, the repository is cloned:

```shell
git clone git@github.com:simphony/<some-wrapper>.git
cd some-wrapper
```
### Local wrapper installation
With OSP-core installed, if the wrapper has its own ontology, it *must* be installed:

```shell
pico install <path/to/ontology.yml>
```

For the wrappers that require the installation of a backend, a `install_engine.sh` script is provided.
It will automatically call `install_engine_requirements.sh`, where the engine specific requirements are installed.

```shell
./install_engine.sh
```

Now the wrapper can be installed:

```shell
python3 setup.py install
```

### Wrapper Docker image
Some wrappers also provided a [Dockerfile](https://docs.docker.com/engine/reference/builder/)
for an automatic installation in a container.
Simply run the `docker_install.sh` script. There is no need to install OSP-core either.

```shell
./docker_install.sh
```
