# Dataflow & Apache Beams
## Definition
Dataflow is a service that is used to extract and transformed the data to finally load them into a data storage service, 
like BigQuery.
## Terminology
- Transform - It is a step of a Dataflow pipeline
- PCollections - It is an object that represents the input/output of a Transform (They do not store data in memory)
- Runner - The engine that executes the pipeline (e.g. Apache Spark)
## Dataflow Pipeline
```python
import apache_beam as beam

def main():

    pipeline = beam.Pipeline(argv=sys.argv)

    (pipeline
        | 'Read' >> beam.io.ReadFromText('gs://<input_path_cloud_storage>')
        | 'CountWords' >> beam.FlatMap(lambda line: count_words(line))
        | 'Write' >> beam.io.WriteToText('gs://<output_path_cloud_storage>')
    )

    pipeline.run()
```
