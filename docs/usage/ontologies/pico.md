# Installing ontologies (pico)

SimPhoNy works with data that is based on ontologies. In particular, all
information is represented in terms of ontology individuals that belong to
specific ontology classes, have specific attributes and can be connected to
other individuals through relationships. Classes, attributes and relationships
are defined in the ontologies. Therefore, in order for SimPhoNy to be able to
properly interpret the data, such ontologies need to be made available to it.
For that purpose, SimPhoNy includes an ontology management tool called `pico`.

Ontologies can be added to SimPhoNy by installing
[_ontology packages_](packages.md), which are
[YAML configuration files](https://en.wikipedia.org/wiki/YAML) that, in
addition to pointing to the actual ontology files, also define extra metadata.
A list of supported ontology languages is available
[here](supported_formats.md#supported-languages).

We [bundle a few of these files with SimPhoNy](ontologies_included.md)
to enable rapid installation of common, well-known ontologies. If the ontology
you wish to install is not among these, and the ontology author does not
provide such a file, then you may just simply
[create one yourself](packages.md).

There are three main operations that can be done with pico:

- [Install](#pico-install) ontologies.
- [List](#pico-list) the installed ontologies.
- [Remove](#pico-uninstall) installed ontologies.

`pico` can be used both from the [command-line](#using-pico-from-the-command-line)
and
[as a Python module within the Python shell](#using-pico-as-a-python-module).

## Using pico from the command line

There are different possible logging levels available, and they can be set via
`--log-level <ERROR|WARNING|INFO|DEBUG>`. The default value is `INFO`.

### pico install

_Usage:_

- `pico install <path/to/ontology_package.yml>`
- `pico install <path/to/ontology_package1.yml> <path/to/ontology_package2.yml> ...`
- `pico install city foaf emmo dcat` (ontology packages that are
  [bundled with SimPhoNy](ontologies_included.md) can be installed using this
  shortcut)

_Behaviour:_

- The ontology file is parsed, and the entities mapped to Python objects.
- The Python objects can be imported via their namespace `from osp.core.namespaces import namespace`.

_Example:_

```console
(venv) user@PC:~$ pico install city
INFO [simphony_osp.utils.pico]: Will install the following packages: city.
INFO [simphony_osp.utils.pico]: Will install the following namespaces: city.
INFO [simphony_osp.utils.pico]: Installation successful
```

### pico list

_Usage:_ `pico list`

_Behaviour:_

- The installed namespaces and packages are printed out. A package can be
  uninstalled and can contain many namespaces. A namespace can be imported
  within the Python shell.

_Example:_

```console
Packages:
        - qe
        - city
Namespaces:
        - xml
        - rdf
        - rdfs
        - xsd
        - cuba
        - owl
        - qe
        - city
```

### pico uninstall

_Usage:_

- `pico uninstall <package>`
- `pico uninstall all`

_Behaviour:_

- The specified packages are uninstalled.
- All packages except the uninstalled ones are re-installed.

_Example:_

```console
(venv) user@PC:~$ pico uninstall city
INFO [osp.core.ontology.installation]: Will install the following namespaces: ['qe']
INFO [osp.core.ontology.yml.yml_parser]: Parsing YAML ontology file /home/<username>/.osp_ontologies/qe.yml
INFO [osp.core.ontology.yml.yml_parser]: You can now use `from osp.core.namespaces import qe`.
INFO [osp.core.ontology.parser]: Loaded 205 ontology triples in total
INFO [osp.core.ontology.installation]: Uninstallation successful
```

### Conflicts with other "pico" installations

Some operating systems might have a pre-existing tool called _pico_.
In most cases, the previous commands should work, but if any problem arises,
you can use the following alternative:

```shell
python -m simphony_osp.tools.pico <command>
```

For example:

```shell
python -m simphony_osp.tools.pico install city
```

## Using pico as a Python module

`pico` can also be used within the Python shell. In particular, four
functions are available to be imported from the `simphony_osp.tools.pico`
module,

```python
from simphony_osp.tools.pico import install, namespaces, packages, uninstall
```

that cover the three main operations that pico is meant to perform: installing
ontologies (`install`), uninstalling ontologies (`uninstall`), and listing the
installed ontologies (`packages`, `namespaces`).

Each function is used in a similar way to its command-line counterpart.

- `install`: accepts _one or more_ positional arguments of string
  type, which can be either paths to `yml` ontology installation files or
  names of ontologies that can be installed via this shortcut. It is meant to
  clone the
  [behavior of its command-line counterpart](https://simphony.readthedocs.io/en/latest/utils.html#pico-installs).

- `uninstall`: accepts _one or more_ positional arguments of string type,
  which must be names of already installed ontology packages. It also
  clones the [behavior of its command-line counterpart](https://simphony.readthedocs.io/en/latest/utils.html#pico-uninstalls).

- `packages`: accepts no arguments and returns an [iterator](https://wiki.python.org/moin/Iterator)
  over the names of the installed packages.

- `namespaces`: accepts no arguments and returns an iterator yielding one
  [`OntologyNamespace` object](https://simphony.readthedocs.io/en/latest/api_ref.html#osp.core.ontology.namespace.OntologyNamespace) for each installed namespace.

Usage examples:

- `install('city', 'path/to/ontology_package.yml')`, `install('foaf', 'dcat2')`
- `uninstall('city', 'foaf')`
- `print(list(packages()))`
- `print(list(namespaces()))`

## Ontology installation folder

The installed ontologies are stored in the directory
`~/.simphony-osp/ontologies` by default. On Windows, `~` usually refers to the
path `C:\Users\<my username>`.

The installation directory can be changed by setting the
environment variable `SIMPHONY_ONTOLOGIES_DIR`.
