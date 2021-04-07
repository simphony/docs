## Motivation
In this section, we will present some of the main concepts SimPhoNy was created to tackle.
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


### Abstraction and generalisation
Once a certain degree of interoperability has been reached, other interesting concepts and details that arise:
#### Semantic vs. syntactic
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

#### Requirement simplification
  Since we know what a user means from the semantic approach, we can use this to automatise and simplify
  the setup and initialisation of processes using default settings.

  For example, a user could decide they want to run a simple simulation with a certain level of detail
  (let's say low, medium or high).
  This could be translated into a meaningful initial state that might suffice a general situation.

  For other, more complex use cases, a higher level of customisation will of course still be available.
#### Coupling and linking
  In the domain of physics simulations, another interesting use case is coupling and linking.
  
  For example, a certain engine might be useful for representing structures made up of atomistic particles
  (molecular dynamics).

  Another software tool could be focussed on representing bodies of fluids (fluid dynamics).
  If both tools can communicate (i.e. there exists some interoperability between them),
  they could both be run and synced simultaneously to create more complex scenarios.

  Here is an example of what that could look like:

  <iframe src="./_static/videos/coupling_and_linking.mp4" frameborder="0" allowfullscreen="true">
  </iframe>

  Furthermore, a truly interoperable platform would enable users to store and 
  access data in databases or other repositories of information.
