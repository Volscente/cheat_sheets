# Architectures

## Lambda Architecture

### Definition

The basic idea is that you run a streaming system alongside a batch system, both performing essentially the same calculation. The streaming system gives you low-latency, inaccurate results (either because of the use of an approximation algorithm, or because the streaming system itself does not provide correctness), and some time later a batch system rolls along and provides you with correct output.

### Drawbacks

Maintaining a Lambda System is very hard, because you need to maintain two different versions of your pipeline. Jay Kreps actually criticised the Lambda Architecture, proposed by Nathan Marz (Twitter).

The critic from Kreps consists in the issue of repeatability in the context of using a replayable system like Kafka. He basically said that a well designed Kafka Architecture could have some the problem way more elegantly.

## Cloud Dataflow

### Concept

There’s no reason the types of clever insights that make batch systems the efficiency heavyweights they are today couldn’t be incorporated into a system designed for unbounded data, providing users flexible choice between what we typically consider to be high-latency, higher-efficiency “batch” processing and low-latency lower-efficiency “streaming” processing. This is effectively what we’ve done at Google with Cloud Dataflow by providing both batch and streaming runners under the same unified model.

Essentially, the old conception that batch systems have a better quality is just a false myth. They use better processing that can be as well applied to streaming processing.
