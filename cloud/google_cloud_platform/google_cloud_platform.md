# AI Development on Google Cloud Platform
## Principles
Google focuses on AI by following seven principles:
- AI should ne socially beneficial
- AI should avoid creating and reinforcing unfair bias
- AI should be built and tested for safety
- AI should be accountable for people
- AI should incorporate privacy design principles
- AI should uphold high standards of scientific excellence
- AI should be made available to users that accord with these principles

## AI Development Layers
### Introduction
The Google Cloud Platform is organised in different layers:
- **AI Foundations** - It includes the essential Cloud services for `Compute`, `Storage` and `Data & AI Products` (suitable for everyone)
- **AI Development** - It includes *ML options* for developing end-to-end models (`Pre-trained APIs`, `BigQuery ML`, `AutoML` and `Custom Training`) and *ML workflows*, like `Vertex AI`(suitable for Data Scientists and ML Engineers)
- **AI Solutions** - It includes vertical and horizontal solutions for `GenAI` (suitable for business users)

### AI Development - ML Options
- **Pre-Trained APIs** - It provides already trained models, imeediately available to use (good for non-technical people)
- **BigQuery ML** - It allows to create models through SQL language
- **AutoML** - It is a no-code solution for building ML models in Vertex AI
- **Custom Training** - Through Vertex AI Workbench and Vertex AI Pipelines

### AI Development - ML Workflows
- **Data Preparation** - It includes data upload and feature engineering (data can be streaming or in batch)
- **Model Development** - It includes model training and model evaluation
- **Model Serving** - It includes model deploynment and model monitoring

### Model Deploynment Options
- **Endpoint** - It is suited for immediate results with low latency (online predictions)
- **Batch Predictions** - It is suited when no immediate response is needed
- **Offline Predictions** - It is suited when the model has to be deployed off the cloud

## MLOps
It combines ML development with operations, just like DevOps. It aims to solve production challenges like CI, CT and CD (Continuous Integration, Training and Delivery).
In Vertex AI Pipelines, it is supported the usage of *Kubeflow* and *TensorFlow Extended* for implementing MLOps best practices.

# Google Cloud Infrastructure
## GCP Layers
- **Networking and Security** - It provides the basis for every other service
- **Compute and Storage** - These two resources are decoupled, so that they can scale independently
- **Data and AI Products** - It does not neet to worry about the udnerlying infrastructure

## TPU (Tensor Processing Unit)
It is a Google custom-developed application-specific integrated circuit (ASIC). It's a domain-specific hardware for matrix multiplication. It's faster and energy efficents.

## Storage Transactional vs Analytical Workloads
- **Transactional** - It is used when fast inserts and updates are required for structured data. It targets only specific rows.
- **Analytical** - It is used when complex queries are required over all the rows of the database.

# Compute and Storage Services
## Compute
### Compute Engine
It is an `IaaS` that provides compute, storage and network resource just like a normal hardware machine. This grants the maximum flexibility.

### Google Kubernetes Engine (GKE)
It runs containerized applications.

### App Engine
It is a fully `PaaS`.

### Cloud Functions
It executes codes in response to an event (it's serverless).

### Cloud Run
It is a fully managed platform that allows to run request or event-driven stateless workloads.

## Storage
### Cloud Storage
Unstructured data. It comes with 4 different storage types:
- Standard (for hot data)
- Nearline (data access monthly)
- Coldline (data access every 90 days)
- Archive (for backup and disaster recovery. Data access once per year)

### Cloud Bigtable
Structured analytical NoSQL.

### Cloud SQL
Structured transactional local SQL.

### Cloud Spanner
Structured transactoinal global SQL.

### Firestore
Structured transactional NoSQL.

### BigQuery
Structured analytical SQL.

# Data and AI Products 
## Ingestion and Process
### Pub/Sub
### Dataflow
### Dataproc
### Cloud Data Fusion

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

## Data Preparation
### Dataprep
It has three connection types:
- Upload/Download - From local files
- Cloud Storage - From Google Cloud Storage
- BigQuery - From BigQuery tables

Each flow is implemented as a sequence of recipies, which are data processing steps. It then convert them into a Dataflow pipeline.

# Processes
## Data Preprocessing
The available options are:
- BigQuery
- Dataflow - It is based on Apache Beam and works well with unstructured data. It can also be used in combination with Pandas
- Dataproc - It works well with Apach Spark infrastructure
- Dataprep - It automatically detects data types and suggests transformations (e.g. missing values, outliers, etc.)