# How to work with owl ontologies

To install owl ontologies in OSP-core, you have to create a configuration yaml file similar
to the following one:

```yaml
identifier: emmo
ontology_file: https://raw.githubusercontent.com/emmo-repo/EMMO/master/emmo-inferred.owl
format: turtle
reference_by_label: True
namespaces:
    mereotopology: http://emmo.info/emmo/top/mereotopology
    physical: http://emmo.info/emmo/top/physical
    top: http://emmo.info/emmo/top
    semiotics: http://emmo.info/emmo/top/semiotics
    perceptual: http://emmo.info/emmo/middle/perceptual
    reductionistic: http://emmo.info/emmo/middle/reductionistic
    holistic: http://emmo.info/emmo/middle/holistic
    physicalistic: http://emmo.info/emmo/middle/physicalistic
    math: http://emmo.info/emmo/middle/math
    properties: http://emmo.info/emmo/middle/properties
    materials: http://emmo.info/emmo/middle/materials
    metrology: http://emmo.info/emmo/middle/metrology
    models: http://emmo.info/emmo/middle/models
    manufacturing: http://emmo.info/emmo/middle/manufacturing
    isq: http://emmo.info/emmo/middle/isq
    siunits: http://emmo.info/emmo/middle/siunits
active_relationships:
    - http://emmo.info/emmo/top/mereotopology#EMMO_8c898653_1118_4682_9bbf_6cc334d16a99
    - http://emmo.info/emmo/top/semiotics#EMMO_60577dea_9019_4537_ac41_80b0fb563d41
default_relationship: http://emmo.info/emmo/top/mereotopology#EMMO_17e27c22_37e1_468c_9dd7_95e137f73e7f
```

## Keywords

**identifier**: Can be any alphanumerical string. It is the name of the package
that contains multiple namespaces. Will be used for uninstallation: `pico uninstall emmo`.
(In YAML ontologies this package name or identifier is the same as the namespace name).

**ontology_file**: Path to the inferred owl ontology. That means you should
have executed a reasoner on your ontology, e.g. by using the `Export inferred axioms`
functionality of [Protégé](https://protege.stanford.edu/).

**format**: File format of the ontology file to be parsed. We support all the
formats that
[RDFLib](https://rdflib.readthedocs.io/en/stable/plugin_parsers.html) supports:
RDF/XML (`rdf+xml`), N3 (`n3`), NTriples (`nt`), N-Quads (`nquads`),
Turtle (`turtle`), TriX (`trix`), RDFa (`rdfa`, `rdfa1.0`, `rdfa1.1`)
and Microdata (`mdata`).

**reference_by_label** (default False): Whether the label should be used or the IRI suffix to reference
entity from within OSP-core. In case of EMMO it is true, because IRI suffixes are not
human friendly. In this case all labels should be unique and not contain whitespaces.
If False, use dot notation to get by IRI square brackets (`__getitem__`) to get by label.
The latter will return a list of all entities with the same label.

**namespaces**: mapping from namespace name (used to import the namespace) to iri prefix.
If IRI doesn't end with "/" or "#", "#" will be added.

**active relationships**:
List of iris of active relationships.

**default relationship**:
The default relationship.

## Installation

Name the yaml file as you would any yaml file `<name>.yml`, where `<name>` should be replaced by a user defined name.

Then you can use pico to install the tool [Pico](utils.md#pico-installs-cuds-ontologies)
to install the ontology:

```sh
pico install </path/to/my_owl_ontology.yml>
```

## Limitations

At the moment, only the most basic predicates of owl ontologies are used:

- `RDF.type` to determine the type of the entities.
- `RDFS.label` to get the entities by label.
- `RDFS.isDefinedBy` to get a descriptions for the entities.
- `RDFS.subClassOf` / `RDFS.subPropertyOf` for subclasses.
- `OWL.inverseOf` for inverse relationships.
- `RDFS.range` to determine the datatype of `DataProperties`. These are the supported
  datatypes:
  - `XSD.boolean`
  - `XSD.integer`
  - `XSD.float`
  - `XSD.string`
- To get the attributes of an owl class, we use
  - The `RDFS.domain` of the `DatatypeProperties`, if it is a simple class.
  - Restrictions on the ontology classes.
  - Furthermore, all DataProperties are considered functional, see [this issue](https://github.com/simphony/osp-core/issues/416).

No reasoner is included. We plan to include a reasoner in the
future.

We try to extend this list over time and support more of the
OWL DL standard.
