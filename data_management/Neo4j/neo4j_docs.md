# Introduction
## Definition
A Graph Database is suitable when data are highly interconnected and the queries become more and more complex to read and maintain.

## Components
### Nodes
They are used to represent elements (e.g., a Person).

### Lables
They are assigned to notes and are used to group them (e.g., `Person` or `Car`).

### Relationships
They express a connection between nodes and they have a single **direciton** and **type**.

**NOTE:** A node can also have a relationship with itself.

### Properties
They are key-value pairs that can be assigned to a node or to a relationship. Neo4j supports different data types, but no nesting properties are supported.

# Installation
## Download
Download the Neo4j desktop version from the [Officla Download Link](https://neo4j.com/download/).

## Editions
- **Community** - It has some limitations (no role-based security and one single property uniqueness constraints), but it can be used under GPL-3.0.
- **Neo4j AuraDB** - It is the cloud based version.
- **Enterprise** - Unlimited graph size, role-based security and more advanced constraints options.

**NOTE:** Neo4j Bloom is a natural language interface for querying and visualize data inside a graph.

# Neo4j Browser
## Start
It can be accessed through the Neo4j Desktop application or through browser localhost:7474 upon starting the graph.