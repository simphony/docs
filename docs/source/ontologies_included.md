# Included ontologies

As described on the [working with ontologies](../working_with_ontologies.md),
section, to use an ontology you first have to install it, and to do so 
usually you have either to define a `yml` configuration file (for OWL 
ontologies and RDFS vocabularies) or provide the ontology in the OSP-core 
YAML ontology format. 

However, in order to make using ontologies easier, we bundle a few of these 
files with OSP-core to enable rapid installation of common, 
well-known ontologies.

Do not hesitate to contact us if you want your ontology to be shipped with 
SimPhoNy.

## Elementary Multiperspective Material Ontology (EMMO) 

For a short introduction on this ontology, see the [fundamentals](fundamentals.md#emmo). 
You can install EMMO using [Pico](utils.md#pico-installs-cuds-ontologies),

```sh
pico install emmo
```

and then just start creating cuds objects

```py
>>> from osp.core.namespaces import math
>>> math.Numerical.attributes
{<OntologyAttribute math.hasNumericalData>: None}
>>> x = math.Numerical(hasNumericalData=12)
>>> x
<math.Numerical: c11cc272-cdcf-421a-8838-5f177b065746,  CoreSession: @0x7f1987173190>
>>> x.hasNumericalData
12
```

## Dublin Core Metadata Initiative (DCMI)

The `dcmitype` and `dcterms` RDFS vocabularies from the [Dublin Core 
Metadata Initiative (DCMI)](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
can be quickly installed using

```sh
pico install dcmitype dcterms
```

Note that due to the fact that OSP-core [does not support RDFS properties](working_with_ontologies.html#limitations), 
properties in these two vocabularies will be ignored by OSP-core. Only the 
classes will be detected.

## Data Catalog Vocabulary - Version 2 (DCAT2)

To install the DCAT2 ontology, use

```sh
pico install dcat2 dcterms foaf prov 
```

Just installing `dcat2` will fail, as it depends on the `dcterms`, `foaf` 
and `prov` vocabularies.

## Friend of a Friend (FOAF)

To install the [FOAF ontology](http://xmlns.com/foaf/spec/), use

```sh
pico install foaf
```

## The PROV Ontology (PROV-O)

To install the [PROV-O ontology](https://www.w3.org/TR/prov-o/), use

```sh
pico install prov
```

## The City Ontology (city)

It is a simple, example ontology included with OSP-core. It can be 
installed as follows.

```sh
pico install city
```

Click [here](ontology_intro.html#an-example-the-city-ontology) 
for more details on this ontology.
