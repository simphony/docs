# SimPhoNy: interoperability powered by ontology

SimPhoNy is an ontology-based framework aimed at enabling interoperability between different simulation and data management tools, with a focus on materials science.



## What can SimPhoNy be used for?

### Manipulate ontology-based linked data, a format well suited for [FAIR data principles](https://en.wikipedia.org/wiki/FAIR_data)


[Linked data](https://en.wikipedia.org/wiki/Linked_data) is a format for structured data that facilitates the interoperability among different data sources. In particular, the data is structured as a directed graph, consistent of nodes and labeled arcs. With SimPhoNy, you can not only manipulate this linked data, **but also transform existing non-linked data into linked data**.

To better understand the idea of linked data, take a quick glance at the toy example below. It shows data about a city from three different data sources: the city's traffic authority, a map from a city guide, and the university registry. As some of the concepts are present in multiple datasets, the linked data representation naturally joins all of them into a single one. 

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Sample linked data](./_static/img/mergedlinkeddata.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

_Linked data about a city from three different sources: the city's traffic authority, a map from a city guide, and the university registry. Each data source is represented using a different color and column._

</figcaption>

</figure>


Moreover, in SimPhoNy, all linked data is based on [ontologies](https://en.wikipedia.org/wiki/Ontology_(information_science)), which give **meaning** to the data. Specifically, SimPhoNy works with ontologies based on the [Web Ontology Language](https://en.wikipedia.org/wiki/Web_Ontology_Language), making the data compatible with the [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web).

### Fetch data from a database, run a simulation and immediately store the results

Ontology-based linked data is not only well suited for the interoperability of data, but also of software tools. In SimPhoNy, one can instantiate individuals from special ontology classes called _wrappers_. These wrappers are both an ontology individual, and a software interface between the core of SimPhoNy (ontology based) and external software tools. We have already developed wrappers for a few database backends and popular simulation engines for materials science. You can have a look at the existing wrappers on our [GitHub organization](https://github.com/simphony). If needed, you may even consider [developing your own](./wrapper_development.md)!

As a SimPhoNy user, you can see the data stored in the external software tools transparently as ontology individuals through the wrappers. In this way, moving data between different software tools becomes as simple as moving or copying it from one wrapper to another.

For example, linked data stored in a SQLite database can be used to run a simulation just by adding the ontology individuals contained in the SQLite wrapper to the Simulation Engine wrapper. Similarly, the ontology individuals representing the results can be simply added back into the database wrapper.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![How wrappers work](./_static/img/wrappers.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center"></figcaption>

</figure>

At this point, the results could be fetched again and for example, visualized with the help of a plotting library.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Toy example of simulation results](./_static/img/trafficsim.svg)

<img src="./_static/img/overview_slider.png" width="350px">

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

<br>

_These results are just a toy example, they do not come from any real nor factually correct simulation._

</figcaption>

</figure>

### Couple simulation engines easily

Exactly in the same way that the data can be moved between a database and a simulation engine using their respective wrappers, it can also be moved between simulation engines. 

In such a way, the complex task of translating the input and output formats of both simulation engines becomes very simple! At the end of the coupling process, just add the results to a database wrapper to store them.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Coupling](./_static/img/wrappers_coupled.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

_Coupling of two simulation engines, one that handles free traffic and another that exclusively handles traffic lights._

</figcaption>

</figure>