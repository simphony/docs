# Welcome to the SimPhoNy documentation!

```{note}
⚠️ You are reading the documentation of a release candidate version of
SimPhoNy. This version has not yet been thoroughly tested, and its
functionality is not yet fully documented. The documentation for the latest
stable version of SimPhoNy can be found
[here](https://simphony.readthedocs.io/en/latest/).
```

The SimPhoNy Open Simulation Platform is a framework that aims to achieve
interoperability between software such as simulation engines, databases and
data repositories using a knowledge graph as the common language. It is focused
on the domain of materials science.

SimPhoNy enables:

- Visualization and exploration of OWL ontologies and RDFS Vocabularies
- Wrappers: interfaces between ontologies and software products or digital objects
- Manipulation of ontology-based data: work with ontology individuals, transfer them among different software products using the wrappers, and query the knowledge graph

````{panels}
   :body: text-center

   ---
   **Getting Started**

   Overview, installation guide and quickstart

   ```{link-button} introduction/overview.html
      :text: To the getting started guides
      :classes: btn-outline-primary stretched-link

   ---
   **Usage Guide**

   Core functionalities, wrappers and advanced utilities

   ```{link-button} jupyter/cuds_api.ipynb
      :text: To the usage guides
      :classes: btn-outline-primary stretched-link

   ---

   **Working with Ontologies**

   Ontology overview, included ontologies, YAML ontologies and ontology querying

   ```{link-button} ontology_intro.html
      :text: To the ontology guides
      :classes: btn-outline-primary stretched-link
   ---

   **Wrapper Development**

   A deep dive into the wrapper mechanism for developing new wrappers

   ```{link-button} wrapper_development.html
      :text: To the wrapper development guides
      :classes: btn-outline-primary stretched-link
   ---

   **API Reference**

   Python API of CUDS, the *Session* classes, and other utilities

   ```{link-button} api_ref.html
      :text: To the API reference
      :classes: btn-outline-primary stretched-link

   ---
   **Additional Information**

   License, acknowledgements, data protection, contact info and more

   ```{link-button} contribute.html
      :text: To get more information
      :classes: btn-outline-primary stretched-link
````

```{toctree}
:hidden: true
:caption: Getting Started
:maxdepth: 2

introduction/overview
introduction/installation
introduction/quickstart
```

```{toctree}
:hidden: true
:caption: Usage Guide
:maxdepth: 2

usage/utils
usage/cuds_api
usage/sessions_and_vars
usage/multiple_wrappers
usage/import_export
usage/simlammps
usage/quantum_espresso
```

```{toctree}
:hidden: true
:caption: Working with Ontologies
:maxdepth: 2

ontologies/ontology_intro
ontologies/working_with_ontologies
ontologies/ontologies_included
ontologies/ontology_interface
```

```{toctree}
:hidden: true
:caption: Wrapper Development
:maxdepth: 2

wrappers/wrapper_development_tutorial
wrappers/wrapper_development
```

```{toctree}
:hidden: true
:caption: API Reference
:maxdepth: 2

api_reference
```

```{toctree}
:hidden: true
:caption: Additional Information
:maxdepth: 2

contribute
detailed_design
links
license
Data protection <https://www.simphony-project.eu/en/data_protection.html>
Imprint <https://www.simphony-project.eu/en/publishing-notes.html>
contact
```
