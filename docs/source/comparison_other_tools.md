# SimPhoNy vs. other tools and technologies
In this section we will try to point out the similarities and differences between
the SimPhoNy framework and other available tools, namely:
 - [RDF](#simphony-vs-rdf)
 - [Neo4j + Neosemantics plugin](#simphony-vs-neo4j)
 - [Owlready2](#simphony-vs-owlready)
 - [AiiDA](#simphony-vs-aiida)
 - [Wikibase](#simphony-vs-wikibase)

## SimPhoNy vs. RDF
[RDF](https://www.w3.org/RDF/) (Resource Description Framework) is an standard data model
for exchanging information.
It does not define an API or a way to interact with the data.

Internally, we use RDF (through [RDFlib](https://rdflib.readthedocs.io/en/stable/)) to store
the classes loaded from the ontology files (previously kept in a pickle file).

## SimPhoNy vs. Neo4j
[Neo4j](https://neo4j.com/) is graph database that with the [neosemantics](https://neo4j.com/labs/neosemantics/4.0/)
plugin is able to work with RDF structures.
This creates an ontology-compatible database.

As a database, Neo4j fits more as potential backend for SimPhoNy than an alternative.
Especially considering the core goal of SimPhoNy is to offer interoperability between different tools,
something that is not easily achieved with Neo4j on its own.

## SimPhoNy vs. Owlready2
[Owlready2](https://pythonhosted.org/Owlready2/) is a tool for creation and manipulation
of ontologies in Python.
It has a built-in reasoner, and can store data in sqlite.

One difference with SimPhoNy is that Owlready2 allows you to edit dynamically ontologies.
While Owlready2 allows you to edit dynamically ontologies, the ontology installed in OSP-core cannot be modified on the fly.

Another difference is the interoperable design on SimPhoNy.
It is designed to connect to other tools via wrappers, and make the development of said wrappers as easy as possible.
This is not something so easily achieved with Owlready2.

## SimPhoNy vs. AiiDA
[AiiDA](http://www.aiida.net/) stands for _Automated Interactive Infrastructure and Database for Computational Science_.
It is an infrastructure also developed in Python that focusses on handling and sharing workflows.

In some aspects, AiiDA and SimPhoNy are very similar. 
AiiDA uses _plugins_, whereas SimPhoNy uses _wrappers_
They both have access to databases for storage, with AiiDA using PostgreSQL internally.

AiiDA is very useful for managing workflows and following data provenance in an efficient way.
However, it is not as tightly coupled with an ontology as SimPhoNy 
(where everything stems from the ontology and its semantics) is.

## SimPhoNy vs. Wikibase
[Wikibase](https://wikiba.se/)