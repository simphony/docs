# Welcome to the SimPhoNy documentation!

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

   ```{link-button} usage/ontologies/index.html
      :text: To the usage guides
      :classes: btn-outline-primary stretched-link

   ---
   **API Reference**

   Python API of CUDS, the *Session* classes, and other utilities

   ```{link-button} api_reference.html
      :text: To the API reference
      :classes: btn-outline-primary stretched-link

   ---
   **Developer's documentation**

   Wrapper development, SimPhoNy operations

   ```{link-button} developers/wrappers.html
      :text: To the developer's documentation
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

usage/ontologies/index

usage/terminological_knowledge
usage/assertional_knowledge

usage/sessions/index

usage/wrappers/index

usage/visualization
```

```{toctree}
:hidden: true
:caption: Developer's documentation
:maxdepth: 2

developers/wrappers
developers/operations
```

```{toctree}
:hidden: true
:caption: Additional Info
:maxdepth: 2

api_reference
contribute
links
license
Data protection <https://www.simphony-project.eu/en/data_protection.html>
Imprint <https://www.simphony-project.eu/en/publishing-notes.html>
contact
```
