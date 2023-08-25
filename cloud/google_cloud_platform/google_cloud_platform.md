# Services
## Data Analysis
### Analytics Hub
Analytics Hub exchanges data analytics assets across organizations to address challenges of data reliability and cost. Essentially, Analytics Hub makes it convenient for you to build a data ecosystem.

There are three roles in Analytics Hub:
- Data Publisher
- Exchange Administrator
- Data Subscriber

The main components of Analytics Hub are:
- Exchanges: collections of data and analytics designed to be shared
- Shared Datasets: BigQuery tables/views made available by the data publisher (ideal for cross-projects and cross-organizational sharing)

# Data Preparation
### Dataprep
It has three connection types:
- Upload/Download - From local files
- Cloud Storage - From Google Cloud Storage
- BigQuery - From BigQuery tables

# Processes
## Data Preprocessing
The available options are:
- BigQuery
- Dataflow - It is based on Apache Beam and works well with unstructured data. It can also be used in combination with Pandas
- Dataproc - It works well with Apach Spark infrastructure
- Dataprep - It automatically detects data types and suggests transformations (e.g. missing values, outliers, etc.)