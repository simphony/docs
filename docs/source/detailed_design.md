# Detailed design
Here we will give an in-depth view of the design of the 3 layers.

For a more general overview, go to [getting started](./getting_started.md#general-architecture).


```eval_rst
.. uml::
  :caption: Standard design
  :align: center

  allow_mixing
  actor User

  rectangle SemanticLayer {

   class Cuds {
    Session session
    UUID uuid
    CUBA cuba_key
    --
    add() : Cuds
    get() : Cuds
    remove() : void
    update() : void
    iter() : Iterator<Cuds>
   }
  }

  rectangle InteroperabilityLayer {

   class Registry <dict> {
   }

   abstract class Session {
    Registry : registry
    --
    store() : void
    load() : Cuds
    sync() : void
   }

   class SomeWrapperSession implements Session {
    List added
    List updated
    List removed
    SyntacticLayer syntactic
    --  
   }
  }

  rectangle SyntacticLayer {
    class SyntacticLayer {
    }
  }

  database backend


  ' -----------------------
  ' ------ RELATIONS ------
  ' -----------------------
  User -> Cuds : interacts_with

  Cuds -> Session : has_a
  Session -> Registry : manages

  SomeWrapperSession -> SyntacticLayer : manages

  SyntacticLayer -> backend : acts_on

  ' -----------------------
  ' -------- NOTES --------
  ' -----------------------
  note top of Cuds
   This will be shallow structure with 
   the uuids of the contained elements:
   {
    Relation1: {uid1: cuba_key, uid2: cuba_key},
    Relation2: {uid4: cuba_key},
    Relation3: {uid3: cuba_key, uid5: cuba_key},
    }
  end note

  note top of Session
   Provides the info requested to Cuds
  end note

  note top of SomeWrapperSession
   Updates the registry with information
   from the backend and vice versa.
  end note

  note top of Registry
   Flat structure that contains all the
   objects accessible through their uid:
   {
    uid1: object1,
    uid2: object2,
    uid3: object3,
    }
  end note

  note top of SyntacticLayer
   Connects to the engine and
   knows its specific API
  end note
```


## Semantic layer
The semantic layer is the representation of the classes of the ontology in a programming language.

When the user installs an ontology through `pico`,
all ontology classes are saved in a pickle file in the site-packages of the python environment.

The procedure is as follows:
- The `OntologyInstallationManager` receives a list of yml files with ontologies to install.
- It instantiates a `Parser`.
- The parser goes through the ontologies and creates an `OntologyClass` per entity.
- All the oclasses of the same namespace are grouped in an `OntologyNamespace`.
- All the registries are collected in the `NamespaceRegistry`. This object will be pickled.

Installing new ontologies loads the pickle and adds new namespaces or modifies the existing ones.

When a class is instantiated, an individual is created.
The pickled file is read, and an instance of the [Cuds](#cuds) class with the ontology information is created.

Through the Cuds they realise the [Cuds API](#cuds-api) which enables the user to work with them in a generic, simple way.

### Cuds
_Location:_ `osp.core.cuds`

It is the base class for all instances. 
Besides whatever might have been defined in the ontology, they all have 3 basic attributes:
 - uid: instance of `uuid.UUID`, it serves to uniquely identify an instance
 - session: this is the link to the interoperability layer.
   By default all objects are in the `CoreSession`, unless they are in a wrapper.
 - oclass: indicates the ontology class they originate from.

#### Cuds structure
Each cuds object contains the uids and oclass of the directly related entities,
as well as the relationship that connects them.
The actual related objects are kept in the [registry](#registry)
```
 a_cuds_object :=  {
    Relation1: {uid1: oclass, uid2: oclass},
    Relation2: {uid4: oclass},
    Relation3: {uid3: oclass, uid5: oclass},
    }
```

```eval_rst
.. note::
   This is an abstraction to show the general structure.
   The actual implementation is a bit more complex.
```

#### Cuds API
The governing idea behind the API design was to simplify as much as possible the usage.

This CRUD API is defined by 6 methods:

##### Create
```python
from osp.core.namespaces import some_namespace

ontology_class = some_namespace.OntologyClass

relationship = some_namespace.relationship

cuds_obj = some_namespace.OntologyClass()
```

##### Add
  ```python
  # These will also add the opposed relationship to the new contained cuds object
  cuds_obj.add(*other_cuds, rel=relationship)
  cuds_obj.add(yet_another_cuds)                           # Uses default relationship from ontology
  ```

  The flow of information for the call of the `add` method would be:
  ```eval_rst
     .. uml::
       :caption: `add` method call
       :align: center

       actor user
       box "Semantic Layer"
         participant "cuds" as cuds
       end box 

       box "Interoperability Layer"
         participant "session" as sess
       end box

       box "Syntactic Layer"
         participant "engine" as eng
       end box

       database "backend" as back

       user -> cuds: add
       cuds <- sess: load
       cuds -> sess: store
  ```
  As you can see, the information is sent to the next layer, but not all the way to the backend.
  This will be propagated when the user calls `session.run()` or `session.commit`.
  The registry is checked for a pre-existing object, in case something that is already there is being added.


##### Get
  ```python
  # Returns a list, unless only one uid was given
  cuds_obj.get()                                           # All the contained cuds objects
  cuds_obj.get(rel=relationship)                           # Entities under that relationship
  cuds_obj.get(*uids)                                      # Searches elements for the uids
  cuds_obj.get(*uids, rel=relationship)                    # Faster, filters by relationship
  cuds_obj.get(oclass=ontology_class)                      # Elements of that class
  cuds_obj.get(rel=relationship, oclass=ontology_class)    # Filters by rel and oclass
  ```
  In this case, the calls carried out by the  `get` method are as follows:
  ```eval_rst
     .. uml::
       :caption: `get` method call
       :align: center

       actor user
       box "Semantic Layer"
         participant "cuds" as cuds
       end box 
 
       box "Interoperability Layer"
         participant "session" as sess
       end box
 
       box "Syntactic Layer"
         participant "engine" as eng
       end box
 
       database "backend" as back
 
       user -> cuds: get
       cuds -> sess: load
 
       == Object not in registry ==
       sess -> eng: _load_from_backend
       eng -> back: <get info>
       back --> eng: <info>
       eng --> sess: <info>
       == Object in registry ==
       sess --> cuds: object
       cuds --> user: object
   ```
   Now the backend is contacted to make sure the user receives the latest 
   available version of the objects being queried.
   This is done through `_load_from_backend()`.

##### Update
  ```python
  # Objects to update must exist already
  cuds_obj.update(*cuds_objs)
  ```
  
  A simple `update` call triggers the following behaviour:
  ```eval_rst
     .. uml::
       :caption: `update` method call
       :align: center

       actor user
       box "Semantic Layer"
         participant "cuds" as cuds
       end box 

       box "Interoperability Layer"
         participant "session" as sess
       end box

       box "Syntactic Layer"
         participant "engine" as eng
       end box

       database "backend" as back

       user -> cuds: update
       cuds <- sess: load()
       cuds -> sess: store()
   ```
   You can see the calls are very much the same as with the `add` method.
   The difference is that the `update` requires the object to be there previously.
   And so the object is first loaded from the registry, then updated and stored.


##### Remove
  ```python
  # These will trigger the update in the opposed relationship of the erased element
  cuds_obj.remove()                                        # Remove all
  cuds_obj.remove(*uids/cuds_objs)                         # Remove objects with the given uids
  cuds_obj.remove(*uids/cuds_objs, rel=relationship)       # Faster, filters by relationship
  cuds_obj.remove(rel=relationship)                        # Delete all elements under a relationship
  cuds_obj.remove(oclass=ontology_class)                   # Delete all elements of a certain class
  cuds_obj.remove(rel=relationship, oclass=ontology_class) # Delete filtering by rel and oclass
  ```

  The sequence for a simple `remove` is:
  ```eval_rst
     .. uml::
       :caption: `remove` method call
       :align: center

       actor user
       box "Semantic Layer"
         participant "cuds" as cuds
       end box 

       box "Interoperability Layer"
         participant "session" as sess
       end box

       box "Syntactic Layer"
         participant "engine" as eng
       end box

       database "backend" as back

       user -> cuds: remove
       cuds <- sess: load()
       cuds -> cuds: remove_rel()
   ```
   Here the registry is accessed to fetch the neighbours of the removed object
   and delete their links (relationships) to it.


##### Iterate
  ```python
  cuds_obj.iter()                                          # Iterates through all
  cuds_obj.iter(oclass=ontology_class)                     # Iterates filtering by the ontology class
  cuds_obj.iter(rel=relationship)                          # Iterates filtering by the relationship
  ```
  
  The general behaviour of the `iter` is:
  ```eval_rst
     .. uml::
       :caption: `iter` method call
       :align: center

       actor user
       box "Semantic Layer"
         participant "cuds" as cuds
       end box 

       box "Interoperability Layer"
         participant "session" as sess
       end box

       box "Syntactic Layer"
         participant "engine" as eng
       end box

       database "backend" as back

       user -> cuds: iterate
       cuds <- sess: load()
       cuds -> user: yield(object)
   ```
   First the uids of all the objects to be iterated are gathered,
   and then they are yielded like a generator
   
```eval_rst
.. hint::
   There is also an :code:`is_a` method for checking oclass inheritance.
```

```eval_rst
.. note::
   Be aware that the sequence diagrams shown represent simple use cases,
   and more complex scenarios are also possible (e.g. adding an object with children).
```
## Interoperability layer
The interoperability layer takes care of the connection and translation between the semantic and syntactic parts.
It also contains the storage of all the objects that share a session.
### Registry
_Location:_ `osp.core.session.registry`

This flat datastructure stores all the objects in the same workspace (session) by their uid.
It is accessed through the session, and invisible to the user.

It also has functionality for pruning, resetting, or filtering its elements.

### Session
_Location:_ `osp.core.session`

The main purpose of session objects is to propagate the changes introduced by the user (and stored in the registry)
to the backend, and update the registry with the modifications coming from the backend.

The backend is accessed via the Syntactic layer, through the `_engine` property.

To simplify and group functionality, we built an inheritance scheme:

```eval_rst
.. uml::
  :caption: Session inheritance scheme
  :align: center

  rectangle "OSP-core" as OSP {
    abstract class Session {
      Registry : registry
      --
      store(cuds_object) : Cuds
      load(*uids) : Iterator<Cuds>
      prune(rel) : void
      {abstract}_notify_delete(cuds_object)
      {abstract}_notify_update(cuds_object)
      {abstract}_notify_read(cuds_object)
    }

    class CoreSession implements Session {
      --
      load(*uids) : Iterator<Cuds>
    }

    abstract class WrapperSession extends Session {
      SyntacticLayer: _engine
      Set : _expired
      Dict : _added
      Dict : _updated
      Dict : _deleted
      --
      expire(*cuds_or_uids) : void
      expire_all() : void()
      refresh(*cuds_or_uids) : void
      _apply_added() : void
      _apply_updated() : void
      _apply_deleted() : void
      _notify_delete(cuds_object) : void
      _notify_update(cuds_object) : void
      _notify_read(cuds_object) : void
      _reset_buffers(changed_by) : bool
      _check_cardinalities() : void
      {abstract}_load_from_backend(uids) : void
    }

    class TransportSession implements WrapperSession {
      CommunicationEngineServer : com_facility
      Session : session_cls
      dict : session_objs
      --
      startListening() : void
      handle_disconnect(user) : void
      handle_request(command, data, user) : str
    }

    abstract class DbWrapperSession extends WrapperSession {
      --
      commit() : void
      load_by_cuba_key(cuba_key, update_registry) : Iterator<Cuds>
      store(cuds_object) : void
      {abstract}_initialize() : void
      {abstract}_load_first_level : void
      {abstract}_init_transaction : void
      {abstract}_rollback_transaction : void
      {abstract}close : void
      {abstract}_load_by_cuba(uids, update_registry): Cuds
    }

    abstract class SqlWrapperSession extends DbWrapperSession {
      --
      _apply_added() : void
      _apply_updated() : void
      _apply_deleted() : void
      _load_from_backend() : Iterator<Cuds>
      _apply_deleted() : void
      load_first_level : void
      _load_by_cuba : void
      {abstract}_db_create(...)
      {abstract}_db_select(...)
      {abstract}_db_insert(...)
      {abstract}_db_update(...)
      {abstract}_db_delete(...)
    }

    abstract class SimWrapperSession extends WrapperSession { 
      bool : _ran
      --
      run()
      {abstract}_run(root_cuds)
      {abstract}_update_cuds_after_run(root_cuds)
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

  rectangle "Simlammps" as simlammps {
    class SimlammpsSession implements SimWrapperSession {
    }
  }
  @enduml
```

```eval_rst
.. note::
   This is a reduced version and does not represent the entirety of the contained functions.
```

The simplest session, called `CoreSession`, is the default one for entities created in a python workspace
and has no backend. It just accesses the registry to manage the operations made by users.

All wrappers will share `WrapperSession` as an ancestor.
This will define which methods have to be implemented and `_engine` as the access point to a backend.

`SimWrapperSession` and `DbWrapperSession` further specify the behaviour of wrappers, defining the methods that 
trigger an action on the backend (`run` and `commit`, respectively).

```eval_rst
.. note::
   You might have noticed that the semantic layer defines :code:`remove` in the API,
   but in the session and registry we use :code:`delete`. The different between them
   is conceptual: :code:`remove` is interpreted as detachment i.e. removal of edges,
   while :code:`delete` implies the erasure of the note itself.
```

#### Buffers
Session classes under `WrapperSession` share 3 types of buffers, namely `added`, `updated` and `deleted`.
The previous buffers are repeated twice, first for the user and then for the engine, 
so the number of buffers is actually 6.

As we have seen in the previous section, not all API calls trigger a change all the way to the backend.
In fact, most of them do not. This is done to limit the traffic in the slower sections 
(networking or communicating with the engine).

On the other hand, the user should be able to access the latest version of the data 
(meaning the changes they might have just done), and the wrapper should know what changes have taken place
since the last sync with the backend software (`commit` or `run`).
In order to achieve these, the changes done by the user directly modify the semantic layer and are
flagged in the buffers as changes to be propagated

Users or wrapper developers do not have to worry about updating this buffers, OSP-core handles them 
(both filling them up and emptying them).

However, these structures will be used in the different `_apply_<buffer>` methods when developing a wrapper
(see [this](./wrapper_development.md#coding) section of wrapper development).

#### Load from Backend
Similar to how the `_apply_<buffer>` methods are used to send information to the engine, 
`_load_from_backend` has the purpose of updating the semantic layer with the latest information from the backend.

You can see in the [`get` sequence diagram](#id3) that when the information has potentially
changed in the backend (i.e the simulation has run, or a database has more data)
the `get` has to fetch the latest version. 
To achieve this, OSP-core calls `_load_from_backend` with the list of desired uids, 
and the wrapper wrapper will update the objects in the registry with the relevant
information and `yield` them.

### Networking
_Location:_ `osp.core.session.transport`

You may have noticed in the [session inheritance scheme](#id2) that there is `TransportSession` implementing the `WrapperSession`.
This session class is the way to connect to engines that are located in other machines through web sockets.

The behaviour is as follows:
- The user instantiates a `TransportSessionClient` and provides
  the session class of the remote server, the hostname and the port.
- The `TransportSessionClient` will connect to a `TransportSessionServer`
  through a `CommunicationEngineClient`.
- The server has the wrapper package installed locally.
- `CommunicationEngineClient` and `CommunicationEngineServer` (one on each side)
  take care of the communication, so that:
  - The methods that the user would call on the remote wrapper are encoded
    with the relevant data (in json) and sent to the server.
  - The server deserialises the data and calls the method on the wrapper.
  - The results are serialised and sent back to the user´s local transport session.

The chosen implementation hides most of the work from the users and wrapper developers.
The only difference between a local wrapper and a remote one is the line where the wrapper session is instantiated, from:
```python
sess = SomeWrapperSession(parameter_a, parameter_b)
wrapper = AWrapperInstance(session=sess)
```
to:
```python
# Once the server is properly setup
sess = TransportSessionClient(SomeWrapperSession, host, port,
                              parameter_a, parameter_b)
wrapper = AWrapperInstance(session=sess)
```
## Syntactic layer
This layer is in direct communication with the backend. 
It has no ontological knowledge and must just provide a simple interface for the interoperability layer to interact with the wrapped application. 

This means it may have to be a binding if the application is in a different language. 
It could also be a file generator/parser for backends that only allow file i/o.
In other cases, (e.g. LAMMPS with PyLammps) it is provided by the backend itself, and requires no implementation. 

Since the syntactic layer will greatly depend on the specific backend, no standardisation is provided there.

