# Ontología para la representación de Zonas Regulatorias

Esta ontología tiene como propósito definir, categorizar y relacionar las Zonas Regulatorias en el contexto de la movilidad inteligente y la gestión urbana (Smart Cities). Se ha diseñado como una extensión modular de la ontología del Sector Público de España (esadm).

# Purpose and scope of the vocabulary

Actualmente, existen vocabularios para divisiones administrativas (esadm) y geometrías (GeoSPARQL), pero existía un vacío semántico para representar entidades funcionales que se superponen a la trama urbana (ZBE, Carga y Descarga, etc...) sin responder a límites administrativos fijos. Esta ontología cubre dicho hueco.

# Ontology prefix and namespace

The ontology prefix is: `edintzone` and it is published under the namespace: [http://vocab.linkeddata.es/datosabiertos/def/common/zone#](http://vocab.linkeddata.es/datosabiertos/def/common/zone#)

# Ontology Conceptualization Image

Every ontology development repository should include, in this root README, a visual representation of the ontology conceptualization.
This image helps users and contributors quickly understand the ontology’s structure, key concepts, and relationships.
- The image should be located in the conceptualization folder.
- Accepted formats: .svg, .png, or .drawio.
- It should be referenced in this README using Markdown syntax, for example:

![Ontology Conceptualization Diagram](diagrams/diagram.png)

# Reposity structure

The repository should contain (at least) the following folders:

| Folder | Description |
|--------|--------------|
| **diagrams/** | Stores diagrams and other resources representing the conceptual model of the ontology (e.g., class hierarchies, relationships). |
| **documentation/** | Stores the HTML or human oriented documentation of the ontology and related artefacts. |
| **examples/** | Includes examples that demonstrate how to instantiate or apply the ontology in real data scenarios. |
| **kos/** | Stores controlled vocabularies or KOS implementation, usually SKOS implementations in rdf. |
| **ontology/** | Contains the actual ontology implementation files in formats such as `.owl`, `.rdf`, `.ttl`, or `.jsonld`. |
| **requirements/** | Contains all documents used to define the ontology’s requirements: data example, competency questions, functional requirements, use cases, etc. |
| **shapes/** | Contains the SHACL shapes used to define and validate ontology constraints. |

# Project maintenance

To manage those incidents or suggested improvements with respect to the vocabulary, we recommend you to follow
the guides provided in [Issues Management](https://github.com/nombre-repositorio/wiki/issues-management) to
generate an issue (work in progress)

# Funding

TODO