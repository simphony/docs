## Fundamental concepts
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
  In our day to day life we use a series of sounds, symbols and rules to communicate.
  In its simplest level, words have a syntactic side, a role in the sentence they make up, and a explicit meaning.

  However, this is not enough for higher levels of communication and understanding.
  If you look at the following sentence:

  <p align=center style="font-style: italic">Time flies like an arrow</p>

  From a syntactic perspective, we can see that _time_ is the subject. A noun.
  _Flies_ is the verb, and so on.
  If we analyse literally the meaning, we can picture time moving with a motion alike that of an arrow.

  On the other hand, we know the real meaning of the sentence is different.
  Here we can deduce that the arrow is used to represent a fast movement,
  and that characteristic is then applied to time. This is the semantic knowledge.

  In a semantic approach, we don't just see words as a series of symbols, but as a link to a sign.
  And we can apply different rules and behaviours to different concepts because of the properties inherent to each entity.

  If we now look at:

  <p align=center style="font-style: italic">Fruit flies like a banana</p>

  The moment we get to the word _banana_, 
  we realise something is wrong. Syntactically, this sentence could be equivalent to the previous one.
  However, we know that _bananas_ do not usually fly.
  And so we decide to change the syntactic interpretation.
  _Fruit flies_ becomes the subject, _like_ the verb and _a banana_ the object.
  Now it makes sense semantically as well.

  In this semantic realm, the concept of ontologies that will be presented in further sections plays a major role.
#### Requirement simplification
  Since we know what a user means from the semantic approach, 
  we can use this to automatise and simplify the setup and initialisation of processes using default settings.

  For example, a user could decide they want to run a simple simulation, with a certain level of detail
  (let's say low, medium or high).
  This could be translated into a meaningful initial state that might suffice a general situation.
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
