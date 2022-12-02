# Operations development

SimPhoNy operations are actions (written in Python) that can be executed on
demand by the user on instance of specific ontology classes that they are
defined for. An example of how to use them for the SimPhoNy's File ontology
class is shown in the
[assertional knowledge section](../usage/assertional_knowledge.ipynb#Operations)
.

Developing operations for an ontology class is fairly simple. To do so, create
a Python package, import the `Operations` abstract class from the
`simphony_osp.development` module, and create an implementation by subclassing
it.

Define an `iri` attribute with the IRI of the ontology class that the operation
should be associated to. Every non-private method (not starting with an
underscore) defined on the implementation is automatically detected and
assigned as an operation of said ontology class. The
[ontology individual object](../usage/assertional_knowledge.ipynb#Ontology-individual-objects)
on which the operation is executed is available as a private attribute
`_individual` on every instantiation of the implementation. The implementation
gets instantiated for a specific ontology individual the first time that any
of the operations defined in it is called by the user.

Finally, define an
[entry point](https://packaging.python.org/en/latest/specifications/entry-points/#entry-points-specification)
(or many if implementing operations for several ontology classes) under the
`simphony_osp.ontology.operations`
[group](https://packaging.python.org/en/latest/specifications/entry-points/#data-model)
that points to your
implementation of the `Operations` abstract class.

```{note}
As implementation example of operations, have a look at
[how file uploads and downloads are implemented in SimPhoNy](https://github.com/simphony/simphony-osp/blob/v4.0.0rc5/simphony_osp/ontology/operations/file.py#L17).
The corresponding entry points are defined [here](https://github.com/simphony/simphony-osp/blob/v4.0.0rc5/setup.py#L81).
```
