```{eval-rst}
.. raw:: html

    <h1>API Reference</h1>

```
This document is for developers and/or advanced users of OSP-core, it contains all API details.

## CUDS
```{eval-rst}
.. autoclass:: osp.core.cuds.Cuds
    :members:
    :show-inheritance:
```

## Ontology interface
```{eval-rst}
.. autoclass:: osp.core.ontology.namespace.OntologyNamespace
    :members:
    :special-members: __getattr__, __getitem__, __contains__, __iter__, __eq__
    :show-inheritance:
    
.. autoclass:: osp.core.ontology.entity.OntologyEntity
    :members:
    :show-inheritance:
    
.. autoclass:: osp.core.ontology.oclass.OntologyClass
    :members:
    :show-inheritance:
    
.. autoclass:: osp.core.ontology.oclass_restriction.Restriction
    :members:
    :show-inheritance:
    
.. autoclass:: osp.core.ontology.oclass_composition.Composition
    :members:
    :show-inheritance:
    
.. autoclass:: osp.core.ontology.relationship.OntologyRelationship
    :members:
    :show-inheritance:
    
.. autoclass:: osp.core.ontology.attribute.OntologyAttribute
    :members:
    :show-inheritance:
```

## Sessions
```{eval-rst}
.. autoclass:: osp.core.session.session.Session
    :members:
    :show-inheritance:

.. autoclass:: osp.core.session.core_session.CoreSession
    :members:
    :show-inheritance:

.. autoclass:: osp.core.session.wrapper_session.WrapperSession
    :members:
    :show-inheritance:

.. autoclass:: osp.core.session.sim_wrapper_session.SimWrapperSession
    :members:
    :show-inheritance:

.. autoclass:: osp.core.session.db.db_wrapper_session.DbWrapperSession
    :members:
    :show-inheritance:

.. autoclass:: osp.core.session.db.sql_wrapper_session.SqlWrapperSession
    :members:
    :show-inheritance:
```

## Registry
```{eval-rst}
.. autoclass:: osp.core.session.registry.Registry
    :members:
    :show-inheritance:
```

## Utilities
```{eval-rst}
.. automodule:: osp.core.utils
   :imported-members:
   :members:
```

### pico
```{eval-rst}
.. automodule:: osp.core.pico
   :members: install, uninstall, packages, namespaces
```
