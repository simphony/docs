# About
SimPhoNy is an ontology-based framework that promotes and enables interoperability between any 3rd-party software tool.
Its latest version is soon to become an open-source python project.
The name ‘SimPhoNy’ stems from the SimPhoNy EU-project in which it was originally developed
(See more details [here](https://www.simphony-project.eu/)). 
One of SimPhoNy’s main tasks is to convert *opaque* data, meaning data whose semantics are hidden, to *transparent* data, that is data whose semantics is understood and easily accessible.

This project aims to clarify the purpose and usage of the SimPhoNy platform through simple, short examples.
In particular, this guide will try to expose the main concepts and components.

_Contact:_ [Pablo de Andres](mailto:pablo.de.andres@iwm.fraunhofer.de), 
[Matthias Urban](mailto:matthias.urban@iwm.fraunhofer.de) and 
[Yoav Nahshon](mailto:yoav.nahshon@iwm.fraunhofer.de) from 
the Materials Data Science and Informatics team, Fraunhofer IWM.

# License
BSD 3-Clause 
Copyright 2020 SimPhoNy OSP-core developers

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Terminology
These are some of the terms used in the following sections:
1. `API`: Application Programming Interface. A set of functions that allow the interaction with an application or system.
1. `OSP`: Open Simulation Platform. 
   A set of common standards and related tools that form the basic environment on top of which compatible and compliant simulation workflows can be developed and run.
   An OSP does not contain any simulation tools itself, it is the common framework enabling to couple and link them.
1. `backend`: a third party application or service. 
   Simulation engines and databases are examples of backends.
1. `wrapper`: a plugin for OSP-core that adds support to a new backend.
   It must allow the user to interact with the backend through the same API as OSP-core.
1. `ontology`: an explicit, formal specification of a shared conceptualization.
   In the context of ontology, other relevant terms are:
   1. `class`: a concept. E.g., 'City', 'Experiment'.
   1. `attribute`: a property of a class that has a data type. E.g., 'name' of the type String which could be used as an attribute of 'City'.
   1. `individual`: an instance of a class. E.g., an instance of the class 'City' can be used to represent the city of Freiburg in which case it would have the attribute 'name' with the value 'Freiburg'.
   1. `relationship`: a type of a way in which one individual relates to another. E.g., 'Has-A' which could use to form the relationship 'Freiburg (City) Has-A Dreisam (River)'.
   1. `entity`:  a general term that can refer to a class, a relationship, attribute, or an individual. E.g., 'City', 'name', 'Has-A', the Freiburg individual are all entities.
   1. `namespace`: an ontology identifier. E.g., 'city_ontology' which could be used as a namespace for the ontology that consists of the entities 'City', 'name' and 'Has-A'.
       - Each entity is uniquely identified by its name and the namespace it is contained in. We call \<namespace name\>.\<entity name\> the `qualified entity name`.
1. `CUDS`:  Common Universal Data Structure. A data structure that is used to uniformly represent ontology concepts in programming code.
   - CUDS exposes an API that provides CRUD (Create, Read, Update and Delete) functionalities.
   - CUDS is a recursive data structure in that a CUDS object may contain other CUDS objects.
   - CUDS is the fundamental data type of OSP-core, a framework that establishes interoperability between software systems that are built on top of ontologies.
1. `CUDS class`: represents an ontology class (a concept) and encodes its ontological information.
1. `CUDS object`: is an instance of a CUDS class and represents an ontology individual.
