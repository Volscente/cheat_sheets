# Introduction

##  Definitions

### Streaming

One interesting definition of streaming data is: _"A type of data processing engine that is designed with infinite datasets in mind."_. This is very different from just saying "low latency" data. It is not the same concept.

### Dataset Cardinality

If we are talking about "infinite" datasets, we are referring to their "Cardinality", namely their size. We could also talk about "Bound" and "Unbound" datasets.

### Dataset Constitution

Another important aspect of a dataset is its "Constitution": Table (holistic view of the data at a specific point in time) and Stream (element-by-element view of the evolution of the data).

## Rationale

Why do we want to use streaming data?

- Streaming data offers lower latency for business data analysis on top of such data. You essentially got the data faster, maybe even in real time! Think about financial use cases.
- Streaming data are actually how most of our systems work nowadays. Offline or bulk transational systems are just simplification of actual stream systems.
