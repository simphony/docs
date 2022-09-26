# API Reference

This document is for advanced users of SimPhoNy and defines all its public API
details. This means that only when there is a breaking change in any of the
methods listed on this page, the major version number of SimPhoNy
will change accordingly, as prescribed by the
[Semantic Versioning Specification](https://semver.org/spec/v2.0.0.html#spec-item-8).

**Do not rely** on the stability of methods not listed on this page.

If the `__init__` method is not listed for a class, you are **not expected
to instantiate such class by yourself**, and thus doing so is unsupported.

## Ontology management

```{eval-rst}
.. autofunction:: simphony_osp.tools.pico.install

.. autofunction:: simphony_osp.tools.pico.uninstall

.. autofunction:: simphony_osp.tools.pico.packages

.. autofunction:: simphony_osp.tools.pico.namespaces
```

## Terminological- and assertional knowledge

```{eval-rst}
.. autoclass:: simphony_osp.ontology.OntologyNamespace
    :members: from_iri, from_label, from_suffix, get, iri, name
    :special-members: __getattr__, __getitem__, __contains__, __iter__, __eq__,
        __len__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.OntologyEntity
    :members: direct_subclasses, direct_superclasses, identifier, iri, is_subclass_of, is_superclass_of, iter_labels, label, label_lang, label_literal, namespace, session, subclasses, superclasses, triples
    :special-members: __bool__, __eq__

.. autoclass:: simphony_osp.ontology.OntologyClass
    :members: attributes, optional_attributes, axioms
    :special-members: __call__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.Restriction
    :members: quantifier, target, relationship, attribute, rtype
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.RESTRICTION_QUANTIFIER
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.RESTRICTION_TYPE
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.Composition
    :members: operator, operands
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.COMPOSITION_OPERATOR
    :members:
    :undoc-members:
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
    :special-members: __getattr__, __setattr__, __getitem__, __setitem__, __delitem__
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.RelationshipSet
    :members: update, intersection_update, difference_update, symmetric_difference_update, inverse
    :inherited-members: individual, predicate, one, any, all, isdisjoint, clear, pop, copy, difference, discard, intersection, issubset, issuperset, add, remove, symmetric_difference, union
    :special-members: __iter__, __contains__, __invert__, __len__, __le__, __lt__, __ne__, __gt__, __ge__, __and__, __radd__, __ror__, __rsub__, __rxor__, __or__, __xor__, __iadd__, __isub__, __ior__, __iand__, __ixor__
    :exclude-members: iter_low_level, prevent_class_filtering

.. autoclass:: simphony_osp.ontology.AttributeSet
    :members: update, intersection_update, difference_update, symmetric_difference_update
    :inherited-members: individual, predicate, one, any, all, isdisjoint, clear, pop, copy, difference, discard, intersection, issubset, issuperset, add, remove, symmetric_difference, union
    :special-members: __iter__, __contains__, __len__, __le__, __lt__, __ne__, __gt__, __ge__, __and__, __radd__, __ror__, __rsub__, __rxor__, __or__, __xor__, __iadd__, __isub__, __ior__, __iand__, __ixor__

.. autoclass:: simphony_osp.ontology.AnnotationSet
    :members: update, intersection_update, difference_update, symmetric_difference_update
    :inherited-members: individual, predicate, one, any, all, isdisjoint, clear, pop, copy, difference, discard, intersection, issubset, issuperset, add, remove, symmetric_difference, union
    :special-members: __iter__, __contains__, __len__, __le__, __lt__, __ne__, __gt__, __ge__, __and__, __radd__, __ror__, __rsub__, __rxor__, __or__, __xor__, __iadd__, __isub__, __ior__, __iand__, __ixor__

.. autoclass:: simphony_osp.ontology.ResultEmptyError
    :show-inheritance:

.. autoclass:: simphony_osp.ontology.MultipleResultsError
    :show-inheritance:
```

## Sessions and wrappers

```{eval-rst}
.. autoclass:: simphony_osp.session.Session
    :members: commit, compute, close, sparql, identifier, update, from_label, add, delete, clear, get, iter
    :inherited-members: locked
    :special-members: __init__, __iter__,  __contains__, __enter__, __exit__, __len__,
    :exclude-members: bind, default-ontology, driver, entity_cache_timestamp, from_identifier, from_identifier_typed, get_default_environment, get_default_session, get_entities, get_identifiers, get_namespace, get_namespace_bind, graph, iter_labels, label_languages, label_predicates, load_parser, lock, unlock, merge, namespaces, ontology, set_default_session, subscribers, unbind, unlock, update, iter_identifiers, default_ontology

.. autoclass:: simphony_osp.session.SessionSet
    :members: update, intersection_update, difference_update, symmetric_difference_update
    :inherited-members: individual, predicate, one, any, all, isdisjoint, clear, pop, copy, difference, discard, intersection, issubset, issuperset, add, remove, symmetric_difference, union
    :special-members: __iter__, __contains__, __len__, __le__, __lt__, __ne__, __gt__, __ge__, __and__, __radd__, __ror__, __rsub__, __rxor__, __or__, __xor__, __iadd__, __isub__, __ior__, __iand__, __ixor__

.. autoclass:: simphony_osp.session.core_session
    :show-inheritance:

.. autofunction:: simphony_osp.tools.import_file

.. autofunction:: simphony_osp.tools.export_file
```

### Search

```{eval-rst}
.. autofunction:: simphony_osp.tools.search.find

.. autofunction:: simphony_osp.tools.search.find_by_identifier

.. autofunction:: simphony_osp.tools.search.find_by_class

.. autofunction:: simphony_osp.tools.search.find_by_attribute

.. autofunction:: simphony_osp.tools.search.find_relationships

.. autofunction:: simphony_osp.tools.search.sparql
```

## Visualization

```{eval-rst}

.. autofunction:: simphony_osp.tools::semantic2dot

.. autoclass:: simphony_osp.tools.semantic2dot::Semantic2Dot
    :members: render, _repr_mimebundle_

.. autofunction:: simphony_osp.tools.pretty_print
```

## Tools

```{eval-rst}

.. autofunction:: simphony_osp.tools.host

.. autofunction:: simphony_osp.tools.branch

.. autofunction:: simphony_osp.tools.relationships_between
```

## Development

```{eval-rst}
.. autoclass:: simphony_osp.development.Wrapper
    :members: open, populate, commit, compute, close, load, save, delete, add, remove, triples
    :special-members: __init__

.. autoclass:: simphony_osp.development.BufferType
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: simphony_osp.development.Operations
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autofunction:: simphony_osp.development.find_operations
```
