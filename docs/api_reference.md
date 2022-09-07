# API Reference

This document is for advanced users of SimPhoNy and defines all its public API
details. This means that only when there is a breaking change in any of the
methods listed on this page, the major version number of SimPhoNy
will change accordingly, as prescribed by the
[Semantic Versioning Specification](https://semver.org/spec/v2.0.0.html#spec-item-8).

**Do not rely** on the stability of methods not listed on this page.

If the `__init__` method is not listed for a class, you are **not expected
to instantiate such class by yourself**, and thus doing so is unsupported.

### Ontology management (pico)

```{eval-rst}
.. automodule:: simphony_osp.tools.pico
   :members: install, uninstall, packages, namespaces
```

## Ontological framework

```{eval-rst}
.. autoclass:: simphony_osp.ontology.OntologyNamespace
    :members: from_iri, from_label, from_suffix, get, iri, name, ontology
    :special-members: __getattr__, __getitem__, __contains__, __iter__, __eq__,
        __len__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyEntity
    :members: direct_subclasses, direct_superclasses, identifier, iri, is_subclass_of, is_superclass_of, iter_labels, label, label_lang, label_literal, namespace, session, subclasses, superclasses, triples, uid
    :special-members: __bool__, __eq__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyClass
    :members: attributes, optional_attributes, axioms
    :special-members: __call__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.Restriction
    :members: quantifier, target, relationship, attribute, rtype
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.RESTRICTION_QUANTIFIER
    :members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.RESTRICTION_TYPE
    :members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.Composition
    :members: operator, operands
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyRelationship
    :members: inverse
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyAttribute
    :members: datatype
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyAnnotation
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyIndividual
    :members: classes, is_a, connect, disconnect, get, iter, operations, attributes
    :special-members: __getattr__, __setattr__, __getitem__, __setitem__, __delitem__, __enter__, __exit__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.RelationshipSet
    :inherited-members:
    :members:
    :special-members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.AttributeSet
    :inherited-members:
    :members:
    :special-members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.AnnotationSet
    :inherited-members:
    :members:
    :special-members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.ResultEmptyError
    :inherited-members:
    :members:
    :special-members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.MultipleResultsError
    :inherited-members:
    :members:
    :special-members:
    :show-inheritance:
```

## Sessions

```{eval-rst}
.. autoclass:: simphony_osp.session.Session
    :show-inheritance:

.. autoclass:: simphony_osp.session.SessionSet
    :show-inheritance:

.. autoclass:: simphony_osp.session.core_session
    :show-inheritance:
```
