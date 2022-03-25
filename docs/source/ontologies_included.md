# Included ontologies

As described on the [working with ontologies](../working_with_ontologies.md)
section, to use an ontology you first have to install it, and to do so 
usually you have either to define a `yml`
[configuration file](working_with_ontologies.md#owl-ontologies-and-rdfs-vocabularies) 
(for OWL ontologies and RDFS vocabularies) or provide the ontology in the 
[OSP-core YAML ontology format](working_with_ontologies.md#osp-core-yaml-ontology-format). 

However, in order to make using ontologies easier, we bundle a few of these 
files with OSP-core to enable rapid installation of common, 
well-known ontologies. Do not hesitate to [contact us](contact.md) if you want 
your ontology to be shipped with SimPhoNy.

The included ontologies, together with their domains of application, are 
listed below.

- [Elementary Multiperspective Material Ontology (EMMO)](ontologies_included.html#elementary-multiperspective-material-ontology-emmo) 
  \- Applied sciences
- [Dublin Core Metadata Initiative (DCMI)](ontologies_included.html#dublin-core-metadata-initiative-dcmi)
  \- Metadata description
- [Data Catalog Vocabulary - Version 2 (DCAT2)](ontologies_included.html#data-catalog-vocabulary-version-2-dcat2)
  \- Data catalogue information
- [Friend of a Friend (FOAF)](ontologies_included.html#friend-of-a-friend-foaf)
  \- People and information on the web
- [The PROV Ontology (PROV-O)](ontologies_included.html#the-prov-ontology-prov-o)
  \- Provenance information
- [The City Ontology](ontologies_included.html#the-city-ontology)
  \- Example ontology aimed at demonstrating the usage of SimPhoNy OSP-core

The ontologies can be installed providing the right
_[package identifier](working_with_ontologies.md#keywords)_ to
[pico](utils.md#pico-installs-cuds-ontologies). You can find such 
package identifier and additional information on each ontology by clicking on 
the links from the list above.

## Elementary Multiperspective Material Ontology (EMMO) 

```{eval-rst}
.. epigraph::

   EMMO is a multidisciplinary effort to develop a standard representational 
   framework (the ontology) for applied sciences. It is based on physics, 
   analytical philosophy and information and communication technologies. It 
   has been instigated by materials science to provide a framework for 
   knowledge capture that is consistent with scientific principles and 
   methodologies. It is released under a Creative Commons 
   `CC BY 4.0 <https://github.com/emmo-repo/EMMO/blob/master/LICENSE.md>`_ 
   license.

   -- `About EMMO section <https://github.com/emmo-repo/EMMO#about-emmo>`_, 
   from the 
   `official EMMO GitHub repository <https://github.com/emmo-repo/EMMO#readme>`_
```

For a short introduction on this ontology, see the [fundamentals](fundamentals.md#emmo)
section. To install the [EMMO ontology](https://emmo-repo.github.io/), use  

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

```{eval-rst}
.. epigraph::

   The Dublin Core™ Metadata Initiative, or "DCMI", is an organization 
   supporting innovation in metadata design and best practices across the 
   metadata ecology. DCMI works openly, and it supported by a 
   `paid-membership model <https://www.dublincore.org/membership/>`_.

   -- `About DCMI <https://www.dublincore.org/about/>`_
```

The Dublin Core™ Metadata Initiative has published, among others, the 
[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
specification, which establishes a set of core metadata terms enabling 
cross-domain description of resources on the web.

```{eval-rst}
.. epigraph::

   Included are the fifteen terms of the Dublin Core™ Metadata Element Set 
   (also known as "the Dublin Core") plus several dozen properties, classes, 
   datatypes, and vocabulary encoding schemes. [...] These terms are intended 
   to be used in combination with metadata terms from other, compatible 
   vocabularies in the context of application profiles.

   -- `DCMI Metadata Terms <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/>`_
```

To install the `dcmitype` and `dcterms` RDFS vocabularies from the [Dublin 
Core Metadata Initiative (DCMI)](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), use

```sh
pico install dcmitype dcterms
```

Note that due to the fact that
[RDFS properties are not supported by OSP-core](working_with_ontologies.html#rdfs-vocabularies),
the properties in these two vocabularies will be ignored. Only the classes will
be detected.

## Data Catalog Vocabulary - Version 2 (DCAT2)

```{eval-rst}
.. epigraph::

   DCAT is an RDF vocabulary designed to facilitate interoperability 
   between data
   catalogs published on the Web. [...]

   DCAT enables a publisher to describe datasets and data services in a catalog
   using a standard model and vocabulary that facilitates the consumption and 
   aggregation of metadata from multiple catalogs. This can increase the 
   discoverability of datasets and data services. It also makes it possible to
   have a decentralized approach to publishing data catalogs and makes 
   federated search for datasets across catalogs in multiple sites possible 
   using the same query mechanism and structure. Aggregated DCAT metadata 
   can serve as a manifest file as part of the digital preservation process.

   -- `Data Catalog Vocabulary (DCAT) - Version 2 <https://www.w3.org/TR/vocab-dcat-2/>`_
```

To install the [DCAT2 ontology](https://www.w3.org/TR/vocab-dcat-2/), use

```sh
pico install dcat2
```

## Friend of a Friend (FOAF)

```{eval-rst}
.. epigraph::

   FOAF is a project devoted to linking people and information using the Web. 
   Regardless of whether information is in people's heads, in physical or 
   digital documents, or in the form of factual data, it can be linked. 
   FOAF integrates three kinds of network: social networks of human 
   collaboration, friendship and association; representational networks that 
   describe a simplified view of a cartoon universe in factual terms, and 
   information networks that use Web-based linking to share independently 
   published descriptions of this inter-connected world. FOAF does not 
   compete with socially-oriented Web sites; rather it provides an approach 
   in which different sites can tell different parts of the larger story, 
   and by which users can retain some control over their information in a 
   non-proprietary format.

   -- `FOAF Vocabulary Specification <http://xmlns.com/foaf/spec/>`_
```

To install the [FOAF ontology](http://xmlns.com/foaf/spec/), use

```sh
pico install foaf
```

## The PROV Ontology (PROV-O)

```{eval-rst}
.. epigraph::

   The PROV Ontology (PROV-O) expresses the PROV Data Model 
   [`PROV-DM <https://www.w3.org/TR/prov-o/#bib-PROV-DM>`_] 
   using the OWL2 Web Ontology Language (OWL2)
   [`OWL2-OVERVIEW <https://www.w3.org/TR/prov-o/#bib-OWL2-OVERVIEW>`_].
   It provides a set of classes, properties, and restrictions that can be used
   to represent and interchange provenance information generated in different 
   systems and under different contexts. It can also be specialized to create 
   new classes and properties to model provenance information for different 
   applications and domains.

   -- `PROV-O: The PROV Ontology <https://www.w3.org/TR/prov-o/>`_
```

To install the [PROV-O ontology](https://www.w3.org/TR/prov-o/), use

```sh
pico install prov
```

## The City ontology

The City ontology is a 
[simple, example ontology](ontology_intro.html#an-example-the-city-ontology) 
included with OSP-core. It provides a collection of concepts to describe 
people and buildings in a city, and is aimed at demonstrating the usage of 
SimPhoNy OSP-core.

To install the
[city ontology](ontology_intro.html#an-example-the-city-ontology), use

```sh
pico install city
```

