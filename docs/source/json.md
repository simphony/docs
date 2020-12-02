

# Serialization JSON schema of CUDS objects

When you serialize a CUDS object using the
[`serialize()` method in the utils module](api_ref.html#osp.core.utils.general.serialize),
you will get a json document as a result.
The method will traverse the hierarchical datastructure
using Depth First Traversal.
Therefore, its result is a json array composed of several flat CUDS objects.

This array can later be deserialized using the opposite 
[`deserialize`](api_ref.html#osp.core.utils.general.deserialize).

The serialization is done via [JSON-LD](https://json-ld.org/),
with the schema used for the [OSP API in Marketplace](https://gitlab.cc-asp.fraunhofer.de/MarketPlace/osp-api).
