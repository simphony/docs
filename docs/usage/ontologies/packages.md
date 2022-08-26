# Ontology packages

Ontologies can be added to SimPhoNy by [installing](pico.md#pico-install)
ontology packages, which are
[YAML configuration files](https://en.wikipedia.org/wiki/YAML) that, in
addition to pointing to the actual ontology files, also define extra metadata.

An example of an ontology package file is shown below. A
[description of each keyword](#keywords) is provided right after the example.

```yaml
identifier: dcat
ontology_file: https://www.w3.org/ns/dcat2.rdf
format: "application/rdf+xml"
requirements:
  - dcterms
  - prov
  - foaf
namespaces:
  dcat: http://www.w3.org/ns/dcat#
  # another_namespace: http://www.w3.org/ns/example_namespace#
```

## Keywords

**identifier**: Can be any alphanumerical string. It is the name of the
ontology package. It is used for uninstallation (e.g. `pico uninstall dcat`)
and dependency verification.

**ontology_file**: Path to the (inferred if applicable) ontology file. That means you should
have executed a reasoner on your ontology, e.g. by using the
_"Export inferred axioms"_ functionality of
[Protégé](https://protege.stanford.edu/).

**format** (optional): File format of the ontology file. When not
provided, it will be guessed from the file extension, although such guess may
not always be correct. The supported ontology languages and serialization
formats are listed [here](supported_formats.md).

**requirements**: A list of identifiers of other ontology packages that this
one depends on. An ontology depends on another ontology if it references
classes, relationships or attributes from it (e.g. by defining a subclass
relationship).

**namespaces**: Mappings that give each IRI prefix in the ontology file a
namespace name, used to import the namespace within SimPhoNy.
If any of the provided IRIs do not end with "/" or "#", "#" will be
automatically added.
