# Introduction

##  Definitions

### Streaming

One interesting definition of streaming data is: _"A type of data processing engine that is designed with infinite datasets in mind."_. This is very different from just saying "low latency" data. It is not the same concept.

### Dataset Cardinality

If we are talking about "infinite" datasets, we are referring to their "Cardinality", namely their size. We could also talk about "Bound" and "Unbound" datasets.

### Dataset Constitution

Another important aspect of a dataset is its "Constitution": Table (holistic view of the data at a specific point in time) and Stream (element-by-element view of the evolution of the data).

### Data Correctness

Even streaming systems should have a mechanism for checkpointing data to a spefici time, in order to be able to restore them in case of a machine failure.

## Rationale

Why do we want to use streaming data?

- Streaming data offers lower latency for business data analysis on top of such data. You essentially got the data faster, maybe even in real time! Think about financial use cases.
- Streaming data are actually how most of our systems work nowadays. Offline or bulk transational systems are just simplification of actual stream systems.

## Time Processing

### Why it is Important?

It is important to have good tools for reasoning about time when dealing with unbounded datasets.

### Time Domains

There are typically two domains we care about

- Even Time - It is the time at which an event occurs.
- Processing Time - It is the time at which the event is observed by the system.

In an ideal world, these two times should always be equal.
