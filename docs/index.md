# Welcome to the SimPhoNy docs!

SimPhoNy is an ontology-based [open-source](license.md) Python framework that promotes and enables interoperability between any 3rd-party software tool. Here you can learn more about it.

````{panels}
   :body: text-center

   ---
   **Getting Started**

   Overview, main concepts, and installation guide

   ```{link-button} overview.html
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
introduction/fundamentals
introduction/general_architecture
introduction/installation
```

```{toctree}
:hidden: true
:caption: Usage Guide
:maxdepth: 2

usage/ontologies/index

usage/ontology_interface
usage/cuds_api

usage/sessions_and_vars
usage/multiple_wrappers
usage/import_export
usage/simlammps
usage/quantum_espresso

usage/utils
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
:caption: Additional Info
:maxdepth: 2

contribute
detailed_design
links
license
Data protection <https://www.simphony-project.eu/en/data_protection.html>
Imprint <https://www.simphony-project.eu/en/publishing-notes.html>
contact
```
