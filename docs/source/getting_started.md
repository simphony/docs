# General architecture
The following architecture has the aim to cover and support the goals presented in the [motivation section](./motivation.md).

```eval_rst
.. uml::
   :align: center
   :caption: Interoperability concept

   skinparam linetype ortho
   actor user
   rectangle SimPhoNy {
      usecase "OSP-core" as osp #FFFFFF
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

```eval_rst
As you can see, :hoverxref:`OSP-core <TERM_OSP>` provides the standard data format and :hoverxref:`API <TERM_API>`,
and the :hoverxref:`wrapper <TERM_WRAPPER>` take care of mapping that format to and from the :hoverxref:`backend <TERM_BACKEND>` specific syntax and :hoverxref:`API <TERM_API>`.

In order to simplify and generalise the usage as much as possible, the :hoverxref:`backend <TERM_BACKEND>` 
specific and syntactic knowledge should be abstracted to :hoverxref:`ontology <TERM_ONTOLOGY>` concepts 
that encompass all third party tools.
```

For that, a 3 layer schema is used:

```eval_rst
.. uml::
   :caption: Three layered design
   :align: center

   skinparam linetype ortho
   
   skinparam rectangle<<invisible>> {
       backgroundColor Transparent
       borderColor Transparent
       titleFontColor Red
       stereotypeFontColor Transparent
       shadowing false
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

```eval_rst
- The *Semantic layer* are the classes generated from the :hoverxref:`ontology <TERM_ONTOLOGY>` and follow the :hoverxref:`CUDS <TERM_CUDS>` :hoverxref:`API <TERM_API>`.

- The *Interoperability layer* maps the changes in the semantic layer to calls in the syntactic layer.

- The *Syntactic layer* provides access to the :hoverxref:`backend <TERM_BACKEND>`.

The closer to the user, the closer to the :hoverxref:`ontology <TERM_ONTOLOGY>` concepts.
The abstraction is replaced by specificity when you move towards the :hoverxref:`backend <TERM_BACKEND>`.


For example, the City, Street or Neighborhood classes from the demonstrative `City Ontology <./ontologies_included.html#the-city-ontology>`_ included in :hoverxref:`OSP-core <TERM_OSP>`, as well as the individuals that can be instantiated using them, would be part of the semantic layer. Any :hoverxref:`wrapper <TERM_WRAPPER>` (e.g. the included `SQLite wrapper <https://github.com/simphony/osp-core/tree/master/osp/wrappers/sqlite>`_), would be part of the interoperability layer. Finally, following the SQLite example, the `sqlite3 library <https://docs.python.org/3/library/sqlite3.html>`_) from python would be part of the syntactic layer.
```

For a full explanation on the architecture and design, go to [detailed design](./detailed_design.md).

## OSP-core
```eval_rst
`OSP-core <https://github.com/simphony/osp-core>`_ is the main component of the SimPhoNy framework.
It is independent of any :hoverxref:`backend <TERM_BACKEND>` and provides the basic :hoverxref:`ontology <TERM_ONTOLOGY>` based data structures for the seamless exchange of data between :hoverxref:`wrappers <TERM_WRAPPER>`.
```

### Ontology file
```eval_rst
:hoverxref:`OSP-core <TERM_OSP>` requires an :hoverxref:`ontology <TERM_ONTOLOGY>` file to create the appropriate :hoverxref:`CUDS classes <TERM_CUDS_CLASS>`.

Said :hoverxref:`ontology <TERM_ONTOLOGY>` must be either in a YAML format as defined by `our specification <./yaml.md>`_
or `one of the supported owl ontologies <./owl.md>`_.
```

<details>
  <summary>YAML Ontology sample</summary>
  The following is an excerpt from the `city.ontology.yml` in OSP-core.

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

```eval_rst
:hoverxref:`OSP-core <TERM_OSP>` can be used with EMMO (European Materials and Modelling Ontology) out of the box.
See more `here <./ontologies_included.md>`_.
```

### Python classes
```eval_rst
Upon installation of :hoverxref:`OSP-core <TERM_OSP>`, each :hoverxref:`ontology <TERM_ONTOLOGY>` class (except from attributes and relationships) becomes a python class.

Since each :hoverxref:`ontology <TERM_ONTOLOGY>` has a namespace, it can be used to import the classes and create :hoverxref:`CUDS objects <TERM_CUDS_OBJECT>`:
```

```py
from osp.core.namespaces import cuba, another_namespace

entity = cuba.Entity()
other_entity = another_namespace.SomeOtherEntity()
```

### Sessions
```eval_rst
The sessions are the interoperability classes that connect to where the data is stored. 
In the case of :hoverxref:`wrappers <TERM_WRAPPER>`, they take care of keeping consistency between the :hoverxref:`backends <TERM_BACKEND>` (e.g. databases) and the internal registry.

When you add an object to a :hoverxref:`wrapper <TERM_WRAPPER>`, a copy of the object is created in the registry belonging to the session of the :hoverxref:`wrapper <TERM_WRAPPER>`.
```

To simplify the understanding and development of session classes, we have created a hierarchy:

```eval_rst
.. uml::
  :caption: Simplified session inheritance scheme
  :align: center

  rectangle "OSP-core" as OSP {
    abstract class Session {
    }

    class CoreSession implements Session {
    }

    abstract class WrapperSession extends Session {
    }

    class TransportSession implements WrapperSession {
    }

    abstract class DbWrapperSession extends WrapperSession {
      commit()
    }

    abstract class SqlWrapperSession extends DbWrapperSession {
    }

    abstract class SimWrapperSession extends WrapperSession {
      run()
    }
  }

  rectangle "Sqlite wrapper" as sqlite {
    class SqliteWrapperSession implements SqlWrapperSession {
    }
  }

  rectangle "SqlAlchemy wrapper" as sqlalchemy {
    class SqlAlchemyWrapperSession implements SqlWrapperSession {
    }
  }

  rectangle "Simlammps wrapper" as simlammps {
    class SimlammpsSession implements SimWrapperSession {
    }
  }

  ' -----------------------
  ' -------- NOTES --------
  ' -----------------------
    note as OSP.note_core
      The CoreSession is the default
      shared session for all Python objects
    end note
    OSP.note_core .. CoreSession

    note as note_db
      The db changes are persisted via
      cuds_object.session.commit()
    end note
    note_db .. DbWrapperSession

    note as OSP.note_sim
      The simulation is run by calling
      cuds_object.session.run()
    end note
    OSP.note_sim .. SimWrapperSession
```

As you can see, CoreSession is the default one used when instantiating a new object in your workspace.

## Wrappers
```eval_rst
Like we have mentioned in previous sections, :hoverxref:`wrappers <TERM_WRAPPER>` allow the user to interact 
through the :hoverxref:`CUDS <TERM_CUDS>` :hoverxref:`API <TERM_API>` with different :hoverxref:`backends <TERM_BACKEND>`.

Since each :hoverxref:`backend <TERM_BACKEND>` is different, for more detailed documentation of each :hoverxref:`wrapper <TERM_WRAPPER>`
we suggest going through the different available `repositories <https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/>`_.

For more technical information regarding :hoverxref:`wrappers <TERM_WRAPPER>`, particularly for :hoverxref:`wrapper <TERM_WRAPPER>` developers, 
we recommend visiting `wrapper development <./wrapper_development.md>`_.
```