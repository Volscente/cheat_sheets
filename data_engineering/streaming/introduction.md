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

In an ideal world, these two times should always be equal and events are processed as soon as they occur.

### Skeweness

In reality there is a skeweness between Event time and Processing time, due to:

- Resource limitation (e.g., CPU, network, etc.)
- Software causes such as distributed logic
- Features of the data themselves

The main limitation derived from such skeweness is that it is not safe to assume that an event occur when our system is able to process it. We therefore would never be able to know the prices time when the event occurs. This skeweness is not fixed over time, which results in even more problems.

### Windowing

One technique to cope with time skeweness is "Windowing": chopping up a dataset into finite pieces along temporal boundaries. Essentially creating windows of data points bounded by a specific time interval.

However this introduces some problem regarding the correctness and compelteness of the data inside each window. Maybe the series is not complete, or even not correct.

## Data Processing Patterns

### Data Processing

In this section we want to explore how to process data depending on what kind of data are we dealing with. The main division would be of course between Bounded Data and Unbounded Data.

We'll review some common patterns in order to processing such data.

### Bounded Data

The most typical data processing pattern for bounded data is the _Batch Processing_.
