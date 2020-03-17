# Wrapper development
For an skeleton structure of a wrapper, you can visit the [wrapper development repo](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/wrapper-development/).
## Ontology
The end goal is to build one, unique and standard ontology with all the relevant entities and relationships.
This ontology could use modules where the entities regarding a certain domain are present. 

However, for the development of a wrapper, it is usually more practical to create a minimal temporary ontology
with the entities required by a wrapper. Once the development is in a more stable stage, the development and merge
of a correct ontology can be done, and should not require major changes in the code.

These are the requirements for a minimal wrapper ontology:

- Should contain an entity representing the wrapper.
  Said entity should inherit from (subclass, is_a) `CUBA.WRAPPER`.
- All attributes should subclass `CUBA.ATTRIBUTE`.
- Top level entities should subclass `CUBA.ENTITY`
- Active relationships should subclass `CUBA.ACTIVE_RELATIONSHIP`
- Passive relationships should subclass `CUBA.PASSIVE_RELATIONSHIP`

<details>
  <summary>Dummy ontology sample</summary>

  ```yaml
  ---
  version: "M.m"

  author: Parmenides <parmenides@ontology.creator>

  namespace: SOME_NEW_WRAPPER_ONTOLOGY

  ontology:

    A_RELATIONSHIP:
      description: "default relationship"
      subclass_of:
      - CUBA.ACTIVE_RELATIONSHIP
      inverse: SOME_NEW_WRAPPER_ONTOLOGY.PIHSNOITALER_A
      default_rel: true

    PIHSNOITALER_A:
      description: "inverse of the default relationship"
      subclass_of:
      -  CUBA.PASSIVE_RELATIONSHIP
      inverse: SOME_NEW_WRAPPER_ONTOLOGY.A_RELATIONSHIP

  ################

    SOME_NEW_WRAPPER:
      subclass_of: 
      -  CUBA.WRAPPER

    VALUE:
      subclass_of:
      -  CUBA.ATTRIBUTE

    SOME_ENTITY:
      subclass_of:
      -  CUBA.ENTITY

  ```
</details>

## Coding
An advantage of the [3-layered-design](./getting_started.md#general-design) that we follow is the modularity and conceptual separation.
The closer to the user, the higher the abstraction.

This allows us to group and clearly define which components should and which ones should not be modified when creating a new wrapper.

 - [Syntactic layer](./detailed_design.md#syntactic-layer): 
   If none is available, one must be developed.

 - [Interoperability layer](./detailed_design.md#interoperability-layer):
   - [Session class](./detailed_design.md#session): 
     Represents the bulk of the work that a wrapper developer needs to do.
     A new class inheriting from the appropriate Session Abstract Base Class must be coded.
     It should at least implement all the inherited abstract methods.
     - `__str__(self)`: String representation of the wrapper.
     - `_apply_added(self, root_obj, buffer)`: Add all the elements in `buffer` to the engine.
     - `_apply_updated(self, root_obj, buffer)`: Update all the elements in `buffer` in the engine.
     - `_apply_deleted(self, root_obj, buffer)`: Remove all the elements in `buffer` from the engine.
     - `_load_from_backend(self, uids, expired=None)`: Loads the given uids (and the dependant entities)
       with the latest information from the backend.
     - Specific for a simulation:
       - `_run(self, root_cuds_object)`: Call the run method on the simulation.
     - Specific for a database:
       - `_initialize(self)`: Initialise the database.
       - `_load_first_level(self)`: Load the first level of children from the root from the database.
       - `_init_transaction(self)`: Start the transaction.
       - `_rollback_transaction(self)`: Rollback the transaction.
       - `close(self)`: Close the connection.

 - [Semantic layer](./detailed_design.md#semantic-layer): 
   Requires no work. 
   Only needs an entity representing the wrapper, as presented in the previous section.

## Engine installation
Most engines will require some sort of compilation or installation before being able to use them through Python.

To facilitate the installation of the back-end to the end users, a shell script with the necessary commands should be made available.
It is also recommended to split the installation of the engine from the installation of the engine requirements.

<details>
  <summary>Sample install_engine_requirements.sh</summary>

  ```shell
    #!/bin/bash
    #
    # Author: Ada Lovelace <ada.lovelace@programmer.algorithm>
    #
    # Description: This script install the requirements for some engine
    #              Used as part of the installation for SomeWrapper.
    #
    # Run Information: This script is called by install_engine.sh

    echo "Installing necessary requirements for the engine"
    platform=$(python3 -mplatform)

    case $platform in
      *"Ubuntu"*)
        sudo apt-get update
        sudo apt-get install cmake
      ;;
      *"centos"*)
        sudo yum update
        sudo yum install make -y
        sudo yum install cmake -y
      ;;
      # Add other platforms here
    esac

  ```
</details>

<details>
  <summary>Sample install_engine.sh</summary>

  ```shell
    #!/bin/bash
    #
    # Author: Ada Lovelace <ada.lovelace@programmer.algorithm>
    #
    # Description: This script installs SomeEngine and its Python binding
    #              Used as part of the installation for SomeWrapper.
    #
    # Run Information: This script is run manually.

    ###################################
    ### Install engine requirements ###
    ###################################
    ./install_engine_requirements.sh

    ################################
    ### Download necessary files ###
    ################################
    echo "Checking out a recent stable version"
    git clone some-repo.com/some-engine.git
    cd some-engine

    ############################
    ### Perform installation ###
    ############################
    cmake cmake 
    make install

    #########################
    ### Test installation ###
    #########################
    {
        python3 -c 'from someEngine import engine; engine.test()'
    } || {
        echo "There was an error with the installation."
        echo "Please, try again or contact the developer."
    }

  ```
</details>

When the implementation of the wrapper is done, the user should be able to install all the necessary components via:

```shell
(env) user@computer:~/some_wrapper$ ./install_engine.sh
(env) user@computer:~/some_wrapper$ python setup.py install
```

### Dockerfile with the engine
Apart from a system installation, we highly recommend providing a `Dockerfile` with the engine
and other minimal requirements, in case the system installation is not possible or desired.

Similar to how OSP core is the structure on top of which the wrappers are made,
we designed a schema of Docker images where OSP core is used as a base image.

Thus, OSP core has an image (currently using Ubuntu) that should be tagged `simphony/osp-core:<VERSION>`.
The Dockerfile of a wrapper will have that image in the `FROM` statement at the top, 
and take care of installing the engine requirements (and the wrapper itself).

To fix the tagging of the images and the versioning compatibility, 
the `Dockerfile` should be installed via the provided `docker_install.sh` script.
It will tag the OSP core image and call the Dockerfile in the root of the wrapper accordingly.

In terms of implementation, a wrapper developer needs to take care of the `Dockerfile`,
taking care to leave the first two lines as they are in the [wrapper development repo](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/wrapper-development/blob/master/Dockerfile).
`docker_install.sh` will only have to be modified with the proper tag for the wrapper image.

## Continuous Integration
GitLab provides Continuous Integration via the `.gitlab-ci.yml` file. 
This should be used for checking both the style and the functionality of the code automatically after each commit.

If the wrapper requires the installation of an engine, it would probably be best to install it in a Docker image 
and push the image to Gitlab Container Registry so that the CI jobs use that image as the base system in which to run.

The `Dockerfile` for the Container Registry image will be very similar to the one used for installing the engine.
However, here it might be useful to install other libraries like flake8 for style checks.

## Utility functions for wrapper development
We have developed some functions that will probably come in handy when developing a wrapper. You can find them in [osp.core.utils.wrapper_development](https://gitlab.cc-asp.fraunhofer.de/simphony/osp-core/blob/master/osp/core/utils/wrapper_development.py).

## Wrapper Examples
Some wrappers we are developing are:
- [SQLAlchemy](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/sqlalchemy-wrapper)
- [SQLite](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/sqlite-wrapper)
- [SimLammps](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/simlammps)
- [SimGromacs](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/simgromacs)
- [SimOpenFoam](https://gitlab.cc-asp.fraunhofer.de/simphony/wrappers/simopenfoam)