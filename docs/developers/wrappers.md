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

## `Wrapper` abstract class

The database-like interface used by SimPhoNy to communicate with the software,
called _Wrapper API_, is defined by the `simphony_osp.development.Wrapper`
abstract class. Objects belonging to the `Wrapper` class are indirectly
controlled by the interactions between the user and session objects, as the
diagram below shows.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Connection between sessions and wrappers](../_static/object_diagram.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

_[UML object diagram](https://www.uml-diagrams.org/class-diagrams-overview.html#object-diagram)
showing the objects involved in the SimPhoNy wrapper mechanism that are
relevant from a developer's perspective._

</figcaption>

</figure>

SimPhoNy makes use of the [RDFLib](https://github.com/RDFLib/rdflib) library to
handle [RDF](https://www.w3.org/TR/rdf-concepts/) data. Thus, the session is in
fact an interface to an
[RDFLib Graph](https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html).
As the user interacts with the session, triples from the underlying graph are
queried, added or removed.
The library also provides a further abstraction, the
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
**RDF representation**. The goal of the SimPhoNy Wrapper API is to facilitate
this task to the developer.

```{note}
If an
[RDFLib store plug-in](https://rdflib.readthedocs.io/en/stable/plugin_stores.html)
already exists for a specific software, then it can be trivially reused to
implement a SimPhoNy wrapper. Just create a graph using the plug-in, and set it
as the base graph for the SimPhoNy wrapper object.
```

## API Overview

The [flowchart](https://en.wikipedia.org/wiki/Flowchart) below illustrates the
**lifecycle** of a session connected to a wrapper object: from its creation to
the moment it is closed.

A sequence of method calls is executed as a
consequence of each possible action the user can take. Each sequence is
represented using a different color, and the action that triggers it is written
next to its accompanying arrow, that points to the first method call in the
sequence.

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![Wrapper session lifecycle](../_static/wrapper_lifecycle.svg)

<figcaption style="display: table-caption; caption-side: bottom; text-align:center">

_Flowchart showing the catalogue of possible user actions and how they
translate to calls to the methods of the wrapper class, that the wrapper
developer must implement._

</figcaption>

</figure>

The `Wrapper` object is spawned when the user opens the session. The `open` and
`populate` methods are then subsequently called in order to gain access to the
resources needed by the software and pre-populate the session with ontology
individuals if necessary. After that, the session is ready to be used. The user
may then access or modify the assertional knowledge (triggering the optional,
low-level RDF manipulation methods), access files associated to ontology
individuals belonging to the _File_ class (triggering the `load` method),
add or change files, commit the changes or request the software to compute new
results. When the user is done, the session is closed.

## API Specification

This section describes the expected behavior of all methods from the Wrapper
API.

### Main methods

#### `open`

Secure access to the resources used by your software. For example:

- spawn simulation engine objects
- open a connection to a database
- open files that need to be accessed

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.open
```

#### `populate`

Populate the base session so that it represents the initial state of the
software. For example:

- given a path to a simulation settings file,
  populate the session with entities
  descibing the contents of the file
- populate the session with dataset
  individuals after connecting to a data
  repository

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.populate
```

#### `commit`

Reflect user's changes on the session in the software's data structure. For
example:

- configure a simulation's settings
- update an SQL table
- modify a file

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.commit
```

The difference with respect to the `compute` method is that this method should
not update the content's of the session itself.

#### `close`

Release the resources used by your software. For example:

- terminate the running process
- close the connection to a database
- close files that are not needed

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.close
```

#### `compute` _(optional)_

Perform a computation using the data currently present on the software's data
structures and update the base session to reflect the changes afterwards.
For example:

- run a simulation

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.compute
```

#### `__init__` _(optional)_

The `__init__` method allows the user to provide extra
parameters in the form of JSON-serializable keyword arguments.

```{note}
This method does not appear on the flowchart for simplicity, but is executed
before the `open` method.
```

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.__init__
```

### File manipulation methods

#### `load` _(optional)_

Receive an identifier of a file individual and retrieve the corresponding file.

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.load
```

#### `save` _(optional)_

Receive an identifier of a file individual and a file handle and save the
contents somewhere.

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.save
```

#### `delete` _(optional)_

Receive the identifier of a file individual and delete the stored file.

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.delete
```

### RDF manipulation methods

These methods operate at the RDF triple level. When a triple (or pattern) is
added or removed, they can intercept the operation and decide whether the
triple should go to the base graph or not when a commit operation is executed.
The intercepted triples get stored in a buffer that is accessible during the
commit operation.

They are useful when one wants to prevent storing the same information twice
(in the base graph and in the software's data structure).

#### `add` _(optional)_

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.add
```

#### `remove` _(optional)_

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.remove
```

#### `triples` _(optional)_

```{eval-rst}
.. autofunction:: simphony_osp.development.Wrapper.triples
```

## Packaging template

This page is meant to offer a mid-level view on what SimPhoNy Wrappers are
and how do they work. If you are interested in developing one, you may find a
template for building and packaging a wrapper in the
[wrapper development repository](https://github.com/simphony/wrapper-development).

```{warning}
You are reading the documentation of a release candidate version of
SimPhoNy.

Some details have not yet been fully documented. In particular, the
contents of the
[wrapper development repository](https://github.com/simphony/wrapper-development)
are still outdated. Consider using the
[SimLAMMPS wrapper code](https://github.com/simphony/simlammps)
as a template instead until the repository is updated.
```
