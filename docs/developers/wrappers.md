# Wrapper development

SimPhoNy Wrappers are software components that transform data from the
assertional-knowledge form to the data structures of
other software and back. Wrappers are abstracted to users as
[sessions](../usage/sessions/introduction.ipynb), which may be viewed
as "boxes" where ontology individuals can be stored.

Sessions work in a way similar to databases. To start using them, one first
has to “open” or “connect” to them. After that, changes can be made on the
data they contain, but such changes are not permanent until a “commit” is
performed. When one finishes working with them, the connection should be
“closed”. Unconfirmed changes are lost when the connection is “closed”.

Therefore, developing a wrapper involves crafting:

- An abstraction of the concepts handled by the software as terminological
  knowledge, that can then be used to represent the information as assertional
  knowledge.
- A database-like interface that is used by SimPhoNy to communicate with the
  software.

For the latter, SimPhoNy defines the _Wrapper API_, that must be implemented by
the developer.

The static view on the SimPhoNy's wrapper API highlights the software
components that the user and wrapper developer interact with, and how they
are connected.

As shown in the diagram below, the user sees a SimPhoNy session object,
which abstracts all the complexity, appearing just as a simple "box"
that can store ontology individuals and where relevant
operations and queries can be run.

However, the session object is an interface to an
[RDFLib Graph](https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html).
As the user interacts with the session, triples from the underlying graph are
being queried, added or removed.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Static perspective](../_static/object_diagram.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

_[UML object diagram](https://www.uml-diagrams.org/class-diagrams-overview.html#object-diagram)
showing the objects involved in the SimPhoNy wrapper mechanism that are
relevant from a developer's perspective._

</figcaption>

</figure>

The [RDFLib](https://github.com/RDFLib/rdflib) library provides a further
abstraction, the
[store](https://rdflib.readthedocs.io/en/stable/_modules/rdflib/store.html).
Stores abstract [triplestores](https://en.wikipedia.org/wiki/Triplestore), a
kind of database that can store collections of RDF graphs in the form of
triples. SimPhoNy implements a special kind of store that is designed to
communicate with SimPhoNy wrapper objects, the final pieces of the chain.

The **wrapper object's interface is what the developer must implement** in
order to make the software interoperable with SimPhoNy. As pointed out in the
diagram, there are several RDF Graph objects, session objects and lists (of
[ontology individual objects](../usage/assertional_knowledge.ipynb#Ontology-individual-objects))
that are accessible from the wrapper object. Those offer several ways for the
developer to retrieve the inputs from the user and translate them into inputs
for the software, or conversely, reflect the outputs from the software into the
user's session.

Perhaps the most important of all is the **base graph**. The base graph is an
[RDFLib Graph](https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html)
that is accessible from the wrapper object, and must be kept in sync with the
software's data structures at all times, as it constitutes their
**RDF representation**.

```{note}
If an
[RDFLib store plug-in](https://rdflib.readthedocs.io/en/stable/plugin_stores.html)
already exists for a specific software, then it can be trivially reused to
implement a SimPhoNy wrapper. Just create a graph using the plug-in, and set it
as the base graph for the SimPhoNy wrapper object.
```

The goal of the SimPhoNy wrapper API is to facilitate this task to
the developer.

## Dynamic perspective

The dynamic view on the SimPhoNy's wrapper API offers an insight on how the
interactions between the user and the session object translate into calls to
the methods of the wrapper object. The diagram below illustrates the
**lifecycle** of a session connected to a wrapper object: from its creation
to the moment it is closed.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Wrapper session lifecycle](../_static/wrapper_lifecycle.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

_Flowchart showing the actions a user can perform and how they translate
to calls to the methods of the wrapper object, that the wrapper developer must
implement._

</figcaption>

</figure>

## API Specification

TODO

## Writing your own wrapper

This page is meant to offer a mid-level view on what is a SimPhoNy wrapper
and how do they work. If you are interested in developing one, please check the
[wrapper development repository](https://github.com/simphony/wrapper-development),
where a template for building and packaging a wrapper can be found.

```{warning}
You are reading the documentation of a release candidate version of
SimPhoNy. This version has not yet been fully documented.

In particular, the contents of the
[wrapper development repository](https://github.com/simphony/wrapper-development)
are still outdated. Consider using the
[SimLAMMPS wrapper code](https://github.com/simphony/simlammps) as
a template instead until the repository is updated.
```
