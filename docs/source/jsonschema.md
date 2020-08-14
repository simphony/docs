

# Serialization JSON schema of CUDS objects

When you serialize a CUDS object using the
[`serialize()` method in the utils module](api_ref.html#osp.core.utils.general.serialize),
you will get a json document as a result.
The method will traverse the hierarchical datastructure
using Depth First Traversal.
Therefore, its result is a json array composed of several flat CUDS objects.

The following explains the schema of the CUDS serialization:

```eval_rst
.. jsonschema:: openapi/serialized_cuds.json#/cuds_array
.. jsonschema:: openapi/serialized_cuds.json#/definitions/cuds
.. jsonschema:: openapi/serialized_cuds.json#/definitions/entity
.. jsonschema:: openapi/serialized_cuds.json#/definitions/uuid
.. jsonschema:: openapi/serialized_cuds.json#/definitions/attributes
.. jsonschema:: openapi/serialized_cuds.json#/definitions/relationships

```
