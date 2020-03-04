# Getting started
## General design
The purpose of this framework is to provide an easy, standard interoperability between multiple different backends through the exchange of data stored in an ontology-based data-structure.

```eval_rst
.. uml::
   :align: center
   :caption: Interoperability concept

   skinparam linetype ortho
   actor user
   rectangle SimPhoNy {
      usecase "osp-core" as osp #FFFFFF
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

As you can see, osp-core provides the standard data format, and the wrappers 
take care of mapping that format to and from the backend specific syntax.

In order to simplify and generalise the usage as much as possible, the backend 
specific and syntactic knowledge should be abstracted to ontology concepts 
that encompass all third party tools.

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
   user -> sem
   sem -> intop
   intop -> syn
   syn -> backend

   user -[hidden]-> gen
   gen -> spe
   backend -[hidden]-> spe
```

- The *Semantic layer* are the classes generated from the ontology and follow the CUDS API.
- The *Interoperability layer* maps the changes in the semantic layer to calls in the syntactic layer.
- The *Syntactic layer* provides access to the backend.

The closer to the user, the closer to the ontology concepts.
The abstraction is replaced by specificity when you move towards the backend.

For a full explanation on the architecture and design, go to [detailed design](./detailed_design.md).

## OSP-core
[OSP-core](https://gitlab.cc-asp.fraunhofer.de/simphony/osp-core) is the main component of the SimPhoNy framework.
It is independent of any backend and provides the basic ontology based data structures for the seamless exchange of data between wrappers.


### Ontology file
OSP-core requires an ontology file to create the appropriate CUDS classes.

Said ontology must be in a YAML format as defined by [our specification](yaml_spec.md).

<details>
  <summary>Ontology sample</summary>

  ```yaml
    version: "0.0.1"
    namespace: "CUBA"

    ontology:
      ENTITY:
        description: The root of the ontology.
        subclass_of: []

      NOTHING:
        description: A class without any individuals.
        subclass_of:
        - CUBA.ENTITY

    ################

      RELATIONSHIP:
        description: The root of all relationships.
        subclass_of:
        - CUBA.ENTITY

      ACTIVE_RELATIONSHIP:
        description: The root of all active relationships. Active relationships express that one cuds object is in the container of another.
        subclass_of:
        - CUBA.RELATIONSHIP

      ################

      WRAPPER:
        description: The root of all wrappers. These are the bridge to simulation engines and databases.
        subclass_of:
        - CUBA.ENTITY

      ATTRIBUTE:
        description: The root of all attributes.
        subclass_of:
        - CUBA.ENTITY
  ```
</details>

OSP-core can also be used with EMMO (European Materials and Modelling Ontology).
Tools for converting EMMO from the OWL format to YAML are provided. See more [here](working_with_emmo.md).

### Python classes
Upon installation of OSP-core, each ontology class (except from attributes and relationships) becomes a python class.

Since each ontology has a namespace, it can be used to import the classes and create cuds objects:

```py
from osp.core import cuba, another_namespace

entity = cuba.Entity()
other_entity = another_namespace.SomeOtherEntity()
```

### Sessions
The sessions are the interoperability classes that connect to where the data is stored. In the case of wrappers, they take care of keeping consistency between the backends (e.g. databases) and the internal registry.

To simplify the understanding and development of session classes, we have created a hierarchy:

```eval_rst
.. uml::
  :caption: Simplified session inheritance scheme
  :align: center

  rectangle "OSP-Core" as OSP {
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

When you add an object to a wrapper, a copy of the object is created in the registry belonging to the session of the wrapper.

## Wrappers
Like we have mentioned in previous sections, wrappers allow the user to interact 
through the cuds API with different backends.

Since each backend is different, for more detailed documentation of each wrapper
we suggest going through the different available [repositories]
(https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/).

For more technical information regarding wrappers, particularly for wrapper developers, 
we recommend visiting [wrapper development](./wrapper_development.md).

## Installation
For the installation and usage of the framework, we *highly* encourage the use of a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

```shell
~/test$ python3 -m venv SimPhoNy
~/test$ source SimPhoNy/bin/activate
(SimPhoNy) ~/test$ 
```

### OSP-core installation
First, the repository must be cloned:

```shell
git clone git@gitlab.cc-asp.fraunhofer.de:simphony/osp-core.git
```

Once available locally, the project must be installed. The default installation is:

```shell
cd osp-core
python3 setup.py install
```

After installing osp-core, you can install an ontology file using **pico** (**p**ico **i**nstalls **c**uds **o**ntologies):

```shell
pico install <path/to/ontology.yml>
```

### Wrapper installation
The installation of a wrapper is similar. First, the repository is cloned:

```shell
git clone git@gitlab.cc-asp.fraunhofer.de:simphony/wrappers/<some-wrapper>.git
```

If the wrapper has its own ontology, this ontology *must* be installed:

```shell
pico install <path/to/ontology.yml>
```

For the wrappers that require the installation of a backend, a `install_engine.sh` script is provided.
It will automatically call `install_engine_requirements.sh`, where the engine specific requirements are installed.

```shell
./install_engine.sh
```

Now the wrapper can be installed:

```shell
python3 setup.py install
```

Some wrappers also provided a [Dockerfile](https://docs.docker.com/engine/reference/builder/) for an automatic installation in a container.
