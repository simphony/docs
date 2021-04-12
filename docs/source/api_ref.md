```eval_rst
.. raw:: html

    <h1>API Reference</h1>

```
This document is for developers and/or advanced users of OSP-core, it contains all API details.

## CUDS
```eval_rst
.. autoclass:: osp.core.cuds.Cuds
    :members:
    :show-inheritance:
```

## Ontology interface
```eval_rst
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
```eval_rst
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
```eval_rst
.. autoclass:: osp.core.session.registry.Registry
    :members:
    :show-inheritance:
```

## Utilities
```eval_rst
.. autoclass:: osp.core.utils.cuds2dot.Cuds2dot
    :members:

.. automodule:: osp.core.utils.general
    :members:

.. automodule:: osp.core.utils.pretty_print
    :members:

.. automodule:: osp.core.utils.simple_search
    :members:

.. automodule:: osp.core.utils.wrapper_development
    :members:
```