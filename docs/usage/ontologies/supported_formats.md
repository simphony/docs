# Supported formats

SimPhoNy supports ontologies in any of the following
[ontology languages](https://en.wikipedia.org/wiki/Ontology_language)

- [Web Ontology Language 2 (OWL 2)](https://www.w3.org/TR/owl2-primer/) (see [limitations](#owl-2-ontologies))
- [Resource Description Framework Schema (RDFS)](https://www.w3.org/TR/rdf-schema/)

that are serialized in any of the formats that the
[RDFLib](https://rdflib.readthedocs.io/en/stable/plugin_parsers.html) library
supports:

- XML (`xml`, `application/rdf+xml`, default),
- Turtle (`turtle`, `ttl`, `text/turtle`)
- N3 (`n3`,`text/n3`)
- NTriples (`nt`, `nt11`,`application/n-triples`)
- N-Quads (`nquads`, `application/n-quads`),
- TriX (`trix`, `application/trix`) and
- TriG (`trig`, `application/trig`).

## Limitations

At the moment, there are significant limitations on the supported features of
OWL 2 ontologies.

### OWL 2 ontologies

Not all features of OWL ontologies are taken into consideration. Among the used
ones are:

- `RDF.type` to determine the type of the entities.
- `RDFS.label` and `SKOS.prefLabel` to get the entities by label.
- `RDFS.subClassOf` / `RDFS.subPropertyOf` for subclasses and subproperties.
- `OWL.inverseOf` for inverse relationships.
- `RDFS.range` to determine the datatype of `DataProperties`.
- To get the attributes of an owl class, we use
  - The `RDFS.domain` of the `DatatypeProperties`, if it is a simple class.
  - Restrictions on the ontology classes.
- Restrictions and compositions are also supported. They can be consulted
  using the
  [`axioms` attribute of ontology classes](../terminological_knowledge.ipynb#Ontology-axioms).

We try to enlarge this list over time and support more of the OWL DL
specification.

No reasoner is included. We plan to include a reasoner in the
future.
