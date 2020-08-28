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
https://pythonhosted.org/Owlready2/

## SimPhoNy vs. AiiDA
[AiiDA](http://www.aiida.net/)


## SimPhoNy vs. Wikibase
[Wikibase](https://wikiba.se/)