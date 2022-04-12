# General architecture

The following architecture has the aim to cover and support the goals presented in the [overview section](overview.md).

```{uml}
   :align: center
   :caption: Interoperability concept

   skinparam {
      linetype ortho
      Shadowing false
      BackgroundColor transparent
      UsecaseBackgroundColor #E3E3E3
      UsecaseBorderColor black
      ActorBackgroundColor transparent
      ActorBorderColor #179c7d
      DatabaseBackgroundColor transparent
      DatabaseBorderColor #179c7d
      PackageBorderColor black
      PackageBackgroundColor #9FC6DE
      ArrowColor #179c7d
      ranksep 10
   }


   actor user
   rectangle SimPhoNy {
      usecase "OSP-core" as osp
      usecase "database\nwrapper" as db_wrapper
      usecase "simulation\nwrapper" as sim_wrapper
      usecase wrapper
   }
   database database
   database "simulation\nengine" as sim_engine
   database backend

   ' -----------------------
   ' ------ RELATIONS ------
   ' -----------------------
   user <-left-> osp: interacts with

   db_wrapper <-up-> database: connects to
   sim_wrapper <-left-> sim_engine: connects to
   wrapper <-down-> backend: connects to

   osp <-up-> db_wrapper: updates
   osp <-left-> sim_wrapper: updates
   osp <-down-> wrapper: updates
```

As you can see, OSP-core provides the standard data format and API,
and the wrappers take care of mapping that format to and from the backend specific syntax and API.

In order to simplify and generalise the usage as much as possible, the backend
specific and syntactic knowledge should be abstracted to ontology concepts
that encompass all third party tools.

For that, a 3 layer schema is used:

```{uml}
   :caption: Three layered design
   :align: center

   skinparam {
      linetype ortho
      Shadowing false
      BackgroundColor transparent
      RectangleBackgroundColor #E3E3E3
      RectangleBorderColor black
      ActorBackgroundColor transparent
      ActorBorderColor #179c7d
      DatabaseBackgroundColor transparent
      DatabaseBorderColor #179c7d
      PackageBorderColor #55A5D9
      PackageBackgroundColor transparent
      ArrowColor #179c7d
      ranksep 10
   }

   skinparam rectangle<<invisible>> {
       BorderColor Transparent
       BackgroundColor transparent
       stereotypeFontColor transparent
   }
   Actor user

   rectangle "semantic layer" as sem {
   }

   rectangle "interoperability layer" as intop {
   }

   rectangle "syntactic layer" as syn {
   }

   database backend

   rectangle gen<<invisible>>[
     Ontology aware,  generic\t
   ]
   rectangle spe<<invisible>>[
     \tEngine specific knowledge
   ]

   ' -----------------------
   ' ------ RELATIONS ------
   ' -----------------------
   user <-> sem
   sem <-> intop
   intop <-> syn
   syn <-> backend

   user -[hidden]-> gen
   gen -> spe
   backend -[hidden]-> spe
```

- The _Semantic layer_ are the classes generated from the ontology with the CUDS API.
- The _Interoperability layer_ maps the changes in the semantic layer to calls in the syntactic layer.
- The _Syntactic layer_ provides access to the backend.

The closer to the user, the closer to the ontology concepts.
The abstraction is replaced by specificity when you move towards the backend.

For example, the City, Street or Neighborhood classes from the demonstrative [City Ontology](ontologies_included.md#the-city-ontology) included in OSP-core, as well as the individuals that can be instantiated using them, would be part of the semantic layer. Any wrapper (e.g. the included [SQLite wrapper](https://github.com/simphony/osp-core/tree/master/osp/wrappers/sqlite)), would be part of the interoperability layer. Finally, following the SQLite example, the [sqlite3 library](https://docs.python.org/3/library/sqlite3.html) from python would be part of the syntactic layer.

For a full explanation on the architecture and design, go to [detailed design](detailed_design.md).

## OSP-core

[OSP-core](https://github.com/simphony/osp-core) is the main component of the SimPhoNy framework.
It is independent of any backend and provides the basic ontology based data structures for the seamless exchange of data between wrappers.

### Ontology file

OSP-core requires an ontology file to create the appropriate CUDS classes.

Said ontology must be either in a YAML format as defined by [our specification](working_with_ontologies.md#osp-core-yaml-ontology-format)
or [one of the supported owl ontologies](working_with_ontologies.md#owl-ontologies-and-rdfs-vocabularies).

<details>
  <summary>YAML Ontology sample</summary>
  The following is an excerpt from the `city.ontology.yml` in osp-core.

```yaml
  ---
  version: "0.0.3"

  namespace: "city"

  ontology:

    encloses:
      subclass_of:
      - cuba.activeRelationship
      inverse: city.isEnclosedBy

    isEnclosedBy:
      subclass_of:
      - cuba.passiveRelationship
      inverse: city.encloses

    hasInhabitant:
      subclass_of:
      - city.encloses

    ################

    CityWrapper:
      subclass_of:
      - cuba.Wrapper
      - city.hasPart:
          range: city.City
          cardinality: 1+
          exclusive: false

    ################

    City:
      subclass_of:
      - city.PopulatedPlace
      - city.hasPart:
          range: city.Neighborhood
          cardinality: many
          exclusive: true
      - city.isPartOf:
          range: city.CityWrapper
          cardinality: 0-1
          exclusive: true
      - city.hasMajor:
          range: city.Citizen
          cardinality: 0-1
          exclusive: true

    Building:
      subclass_of:
      - city.ArchitecturalStructure
      - city.hasPart:
          range: city.Address
          cardinality: 1
          exclusive: false
      - city.hasPart:
          range: city.Floor
          cardinality: many
          exclusive: false
      - city.isPartOf:
          range: city.Street
          cardinality: 1
          exclusive: true

    Citizen:
      subclass_of:
      - city.Person
```

</details>

OSP-core can be used with EMMO (Elementary Multiperspective Material Ontology) out of the box.
See more [here](ontologies_included.md).

### Python classes

Upon installation of OSP-core, each ontology class (except from attributes and relationships) becomes a python class.

Since each ontology has a namespace, it can be used to import the classes and create cuds objects:

```py
from osp.core.namespaces import cuba, another_namespace

entity = cuba.Entity()
other_entity = another_namespace.SomeOtherEntity()
```

### Sessions

The [sessions](./detailed_design.md#session) are the interoperability classes that connect to where the data is stored.
[In the case of wrappers](./wrapper_development.md#coding), they take care of keeping consistency between the backends (e.g. databases) and the internal registry.

The `CoreSession` is the default one used when instantiating a new object in your workspace. When you add an object to a wrapper, a copy of the object is created in the registry belonging to the session of the wrapper.

## Wrappers

Like we have mentioned in previous sections, wrappers allow the user to interact
through the cuds API with different backends.

Since each backend is different, for more detailed documentation of each wrapper
we suggest going through the different available [repositories](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/).

For more technical information regarding wrappers, particularly for wrapper developers,
we recommend visiting [wrapper development](wrapper_development.md).
