# Included ontologies

## The City ontology

OSP-core currently ships with two ontologies.
The first one, called `city` is a simple example ontology.
You can use it to play around and get familiar with OSP-core.
We will also use it a lot in this documentation as an example.

The city ontology provides the concepts to describe people and
buildings in a city. In this graph we show the different entities in the
ontology. We used [Ontology2Dot](utils.md#ontology2dot) for that:

![ontology2dot sample image](_static/img/ontology2dot.png)

To use the city ontology you have to install it using the tool [Pico](utils.md#pico-installs-cuds-ontologies):

```sh
pico install city
```

Take a look at our [examples](jupyter/cuds_api.md) to see how you can build your own city!

## Working with EMMO

The second ontology that is ready to be used out of the box is the Elementary Multiperspective Material Ontology,
or EMMO in short. For a short introduction, see the [fundamentals](fundamentals.md#emmo).

You can install EMMO using [Pico](utils.md#pico-installs-cuds-ontologies).

```sh
pico install emmo
```

Start creating cuds objects:

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

## More ontologies

To create you own or use an existing ontology, see the upcoming sections.
Contact us, if you want your ontology to be shipped with SimPhoNy.
