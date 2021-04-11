# Fundamental concepts
In this section we will present some of the main concepts behind SimPhoNy.

## General notions
### Operability
There is a multitude of tools and programs out there, all with their own formats and protocols.

Every time a user wants to use one of these tools, they must familiarise themselves with the software.
Furthermore, if they want to integrate multiple tools in one workflow, the must, in most cases,
take care of the conversion on their own.

Based on how tools communicate with other tools, we can define 3 levels of operability:

#### Compatibility
  ```eval_rst
  .. uml::
    :align: center
    :caption: Compatibility
    
    rectangle A
    rectangle B
    rectangle C
    rectangle D

    A <-> B
    A <-[hidden]- C
    C <-> D
  ```

  When we say two tools are compatible, they are able to communicate with each other
  in a one to one basis.
  This means the tools must either use the same format, or be able to convert to the format of the other.

  If we compare this to speaking languages, you could say `A` and `B`, or `C` and `D` speak the same language.
  However, `A` has no way to talk with `C` or `D`, for example.

#### De Facto Standard
  ```eval_rst
  .. uml::
    :align: center
    :caption: De Facto Standard
    
    rectangle A
    rectangle B
    rectangle C
    rectangle D
    
    A <--> B
    A <-> C
    C <-[hidden]- D
    B <-[hidden]- D
    A <-> D
  ```

  In this case, the level of operability is higher. 
  All tools know how to communicate with a tool whose format has become a de facto standard.

  To continue with our language simile, `A` would be a translator that speaks the languages of `B`, `C` and `D`.
  If `B` wants to talk to `C`, they must first relay the message to `A`,
  and `A` will convert it to a format that `C` understands.

#### Interoperability
  ```eval_rst
  .. uml::
    :align: center
    :caption: Interoperability
    
    usecase x as "open standard"
    rectangle A
    rectangle B
    rectangle C
    rectangle D
    A <-down-> x
    B <-right-> x
    C <-left-> x
    D <-up-> x
  ```
  The highest level of operability is interoperability. 
  Here there is no need for all tools to go through the De Facto standard, 
  because there is a format that is known by all of them and enables all components to communicate among themselves.

  This final stage could be compared to all parties learning a language like 
  [Esperanto](https://en.wikipedia.org/wiki/Esperanto).


Interoperability between software tools is one of the most important objectives of the SimPhoNy framework.
### Semantic vs. syntactic
  We can interpret a word as a specific sequence of characters without caring about the meaning itself.
  This way, a simulation engine parsing an input file will know that the integer written after the keyword
  `step` will be used to set the number of iterations the execution loop will run.
  It does nothing else, and could as easily use the sequence `ppp`.

  However, for a person, the word `step` will be a sign representing a specific concept.
  It could be the number of rounds in a simulation, but also the consecutive instructions in an algorithm, the
  different levels in a stair or the motion a person makes when walking. 
  Based on the domain, a person can also list other relevant concepts and relationships
  (e.g. when thinking of a stair, the `material` or the `width`).

  Being able to know the semantic meaning of an instance and hence its connection to other concepts
  is one of the principles of SimPhoNy. For that, ontologies play a major role.

### Ontology
```eval_rst
.. important::
   An ontology is a formal specification of a shared conceptualization.  `[Borst, 1997]
   <https://research.utwente.nl/en/publications/construction-of-engineering-ontologies-for-knowledge-sharing-and->`_ .

```

Let's look at the individual components of this definition, starting from the end.
 - _Conceptualization_, an ontology will work on the ideas and relationships in an area of interest.
 - _Shared_, the ideas and concepts are perceived and agreed by multiple people.
 - _Specification_, it will define and describe them in detail, following some predetermined rules and format.
 - _Formal_, meaning it will follow a machine readable syntax.

In a simpler way, an ontology can be seen as the definition of concepts relevant to a given domain, 
as well as the relationships between them, in a way that a machine can interpret it.

For a deeper, more detailed analysis of the definition, refer to [[Guarino, 2009]](http://dx.doi.org/10.1007/978-3-540-92673-3_0).

Ontologies are more elaborated than taxonomies in that they can include multiple kinds of relationships
(not just parent-child) between complex concepts in big domains.

#### EMMO
TODO
### CUDS
Cuds, or Common Universal Data Structure, is the ontology compliant data format of OSP-core:
- **Cuds is an ontology individual**: each Cuds object is an instantiation of a class in the ontology.
  If there is a food ontology, describing classes like pizza or pasta, a Cuds object could represent one specific pizza or pasta dish, that exists in the real world.
  Like ontology individuals, Cuds objects can be related with other individuals/Cuds by relations defined in the ontology. Like a _pizza_ that 'hasPart' _tomato sauce_
- **Cuds is API**: To allow users to interact with the ontology individuals and their data, Cuds provide a CRUD API.
- **Cuds is a container**: Depending on the relationship connecting two Cuds objects, a certain instance can be seen as a container of other instances.
  We call a relationship that express containment an 'active relationship'.
  In the pizza example, 'hasPart' would be an 'active relationship'. If one would like to share the pizza Cuds object with others, one would like to share also the tomato sauce.
- **Cuds is RDF**: Internally a Cuds object is only an interface to an RDF-based triple store that contains the data of all Cuds objects.
- **Cuds is a node in a graph**: : Cuds being individuals in an RDF graph implies that each Cuds object can also be seen as a node in a graph.
  This does not conflict with the container perspective, instead we see it as to different views on the data.
## Technologies and frameworks
### RDF
[RDF](https://www.w3.org/RDF/) (Resource Description Framework) is a formal language for describing structured information
used in the Semantic Web. Its first specification was published in 1999 and extended in 2004.

Knowledge is represented in directed graphs where the nodes are either ontological classes,
instances of those classes or literals and the edges the relationships connecting them. 

The graph is serialised in the form of triples of the form "subject-predicate-object"
- _Subject_: The IRI of the entity the triple refers to.
	Blank nodes have no IRI, but they are outside of the scope of this thesis.
- _Predicate_: IRI of the relationship from subject to object.
- _Object_: Literal or IRI of an entity

The following is an example of an RDF triple. This example will also be used to show the different serialisation formats of RDF.
For the IRIs, `dbpedia`'s namespace was used.
```eval_rst
.. uml::
   :align: center
   :caption: RDF triple sample

   (dbr:J._R._R._Tolkien) as tolkien
   (dbr:The_Lord_of_the_Rings) as lotr
   lotr -> tolkien : dbo:author
```

The most used formats for storing RDF data are:
- [XML](https://www.w3.org/2001/sw/RDFCore/TR/WD-rdf-syntax-grammar-20030117/):
  Historically the most common format given the amount of libraries for handling it.
	It was released hand in hand with the RDF specification.
	Unfortunately, XML is best used with tree-like structures rather than graphs,
	which also makes it harder for humans to read.

	The example triple in XML is:
  ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <?xml version="1.0" encoding="utf-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
            xmlns:dbp="http://dbpedia.org/property/">
        <rdf:Description rdf:about="http://dbpedia.org/resource/The_Lord_of_the_Rings">
            <dbp:author rdf:resource="http://dbpedia.org/resource/J._R._R._Tolkien"/>
        </rdf:Description>
    </rdf:RDF>
  ```

- [N3](https://www.w3.org/TeamSubmission/n3/): Notation3 is designed with human readability as a motivator.
	The RDF triples are written one per line, with the possibility to define common prefixes
	and other directives for simplicity.
	
	The previous example in N3 would be:
  ```turtle
      @prefix dbo: <http://dbpedia.org/ontology/> .
      @prefix dbr: <http://dbpedia.org/resource/> .
      dbr:The_Lord_of_the_Rings  dbo:author  dbr:J._R._R._Tolkien .
  ```

- [Turtle](https://www.w3.org/TR/turtle/): Based on N3, it strips some of its syntax, making it easier to parse
	for machines.
	The recurring example would be exactly the same in Turtle as in N3.

- [N-Triples](https://www.w3.org/TR/n-triples/): N-Triples are even simpler, without any of the syntactic sugar from N3 or Turtle.
	The triples are written one per line without prefixes. This makes it a very easy format to parse
	but complex to maintain/read by a human.

	The following representation should be in one line (it has been split for readability)
  ```xml
    <http://dbpedia.org/resource/The_Lord_of_the_Rings>
      <http://dbpedia.org/ontology/author>
      <http://dbpedia.org/resource/J._R._R._Tolkien> .
  ```
	
- [JSON-LD](https://www.w3.org/TR/json-ld/): uses the commonly accepted web data scheme for serialising RDF triples.
	Easier than XML for humans, JSON has standard libraries in practically all programming languages.

	The example in JSON is:
  ```json
    {"@id": "http://dbpedia.org/resource/The_Lord_of_the_Rings",
      "http://dbpedia.org/property/author": 
        [{"@id": "http://dbpedia.org/resource/J._R._R._Tolkien"}]
      }
  ```
SimPhoNy supports all the previous formats (plus a simpler custom YAML) as inputs in the ontology installation.

#### SPARQL
[SPARQL](https://www.w3.org/TR/sparql11-overview/) (recursively SPARQL Protocol and RDF Query Language) is the most common query language for RDF.
Queries are graph patterns (similar to the triples of Turtle) with variables for the parts of the pattern that make up the result.

Variables start with the identifier `?` and represent concrete values that will be matched in the query process.
They can appear in multiple locations in the patterns and those present in the 
`SELECT` clause will be returned as the query result.

The query for the author of _The Lord of the Rings_ from our sample triples in SPARQL is:
  ```sparql
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    SELECT ?person WHERE {
        dbr:The_Lord_of_the_Rings  dbo:author  ?person .
    }
  ```

The SPARQL query language offers multiple types of result sets and clauses, most of which won't be used for this Master's thesis.
One which should be mentioned is the `FILTER` keyword.
This will limit the result to those that evaluate `true` to the expression inside the brackets.
For instance (omitting the prefix declaration for simplicity):

  ```sparql
    SELECT ?character WHERE {
        ?character dbp:affiliation dbr:The_Lord_of_the_Rings .
        ?character dbo:age ?age .
        FILTER(?age >= 100)
    } 
  ```
The previous query would return the characters from the book series with an  age higher or equal to 100.
(Note that while the query is correct, the result is empty, as such information is not stored on DBpedia).

For a very interesting and comprehensive introduction into RDF and SPARQL, see [[Hitzler, 2009]](http://dx.doi.org/10.1201/9781420090512).
