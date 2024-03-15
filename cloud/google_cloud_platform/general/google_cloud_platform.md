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

# AI Development Layers
## Introduction
The Google Cloud Platform is organised in different layers:
- **AI Foundations** - It includes the essential Cloud services for `Compute`, `Storage` and `Data & AI Products` (suitable for everyone)
- **AI Development** - It includes *ML options* for developing end-to-end models (`Pre-trained APIs`, `BigQuery ML`, `AutoML` and `Custom Training`) and *ML workflows*, like `Vertex AI`(suitable for Data Scientists and ML Engineers)
- **AI Solutions** - It includes vertical and horizontal solutions for `GenAI` (suitable for business users)

## AI Development - ML Options
- **Pre-Trained APIs** - It provides already trained models, imeediately available to use (good for non-technical people)
- **BigQuery ML** - It allows to create models through SQL language
- **AutoML** - It is a no-code solution for building ML models in Vertex AI
- **Custom Training** - Through Vertex AI Workbench and Vertex AI Pipelines

## AI Development - ML Workflows
- **Data Preparation** - It includes data upload and feature engineering (data can be streaming or in batch).
- **Model Development** - It includes model training and model evaluation
- **Model Serving** - It includes model deploynment and model monitoring

### Data Preparation
#### Feature Engineering
Consider also the difference between **Legacy Features** (old features that were added because they were valuable at the time. But since then, better features have been added, which have made them redundant) and **Bundled Features** (Feature added as a part of a bundle, which collectively are valuable, but individually may not be).

#### Data Leakage
Information about the label ara somehow leaking into the training data.

## Model Deploynment Options
- **Endpoint** - It is suited for immediate results with low latency (online predictions). Performance is measured in QPS (Queries Per Second).
- **Batch Predictions** - It is suited when no immediate response is needed
- **Offline Predictions** - It is suited when the model has to be deployed off the cloud

**NOTE:** In order to optimise the cost, one can adopt an hybrid solution. Compute batch predictions for top 20% users, in order to reduce latency. The rest 80% is served through online predictions.

## Inference
- **REST/HTTP API** - Online predictions
- **Cloud Machine Learning Engine** - Batch predictions
- **Dataflow** - Batch and streaming pipelines

## MLOps
It combines ML development with operations, just like DevOps. It aims to solve production challenges like CI, CT and CD (Continuous Integration, Training and Delivery).
In Vertex AI Pipelines, it is supported the usage of *Kubeflow* and *TensorFlow Extended* for implementing MLOps best practices.

## Generative AI
### Model Garden
It a single entrypoint to discover pre-trained Google GenAI models.
They are divided in three categories:
- **Foundation Models** - Multi-task models that can be tuned for specific tasks
- **Task-Specific Solutions** - Models trained to solve specific problems
- **Fine-Tunable Models** - Open source models that can be fine-tuned by using custom notebooks or pipelines

### Generative AI Studio
It allows to fast development and testing GenAI models.
Prompting types:
- **Zero-shot Prompting** - Providing a single command to the LLM without any example
- **One-shot Prompting** - Providing a single example of the task to the LLM
- **Few-shot Prompting** - Providing a few examples fo the task to the LLM

### AI Solutions
- **Vertical Solutions** - Solve specific problems within certain industries
- **Horizontal Solutions** - Solve similar problems across different industries

# Google Cloud Infrastructure
## Regions and Zone
Each resource in GCP is organised in:
1. **Multi-Region** - Like North-US
2. **Region** - Like north-us
3. **Zones** - Like north-us1a, north-us1b and north-us1c   

Such division is not necesseraly related to a physical division.

## Connect to GCP
In order to use any GCP service, the host has to pass through an **Edge Points of Presence** (POPs) or use an **Edge Nodes** (Google Global Cache or GGC). The latest are sometimes referred also as **Content Delivery Network (CDN)**. All of such terms are usually referring to the same thing. The main difference between POP and Edge Nodes is that the latter ones contain a cache of the most common and static information. So that it's easier to access them.

The above POPs, Edge Nodes or CNDs represent points where the Google's network is connected to the rest of the Internet via peering. Such connection is made possible through an ISP (Internet Service Provider).

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

# Distributed Training
## Architectures
### Data Parallelism
It is a model-agnostic in which each training is ran on a different device, with different data non-overlapping samples. Approaches:
- **Synchronous**: model's parameters are computed on each single device and then exchanged to aggregate them (AllReduce - avg) for the next training iteration. The gradient computation becomes the main overhead in the process. Suitable for dense models.
- **Asynchronous**: no device waits for the model's parameters update. The gradients are shared as peers or through central *Parameter Servers*. The workers fetch and update gradients from the Parameter Servers independently. The risk is that workers get out of sync and thus not converging. It is suitable for model that use sparse data, contain fewer features and consume less memory.

### Model Parallelism
Data are not splitted among devices, instead different parts of the model are used on each device. Then the results are stacked together to have the final model results. For example, different Layers to different GPUs.

## TensorFlow Distruted Strategies
It is an API that takes care of distributed training.

# Hybrid Cloud
## Definition
It is used when part of your code is on the cloud, but another is not. The reasons might be:
- On-premises resources not yet migrated
- Multiple cloud providers

## Requirements
- **Composability** - It is the ability of build together a set of microservices/resources to construct a full ML pipeline.
- **Portability** - Port the code anywhere.
- **Scalability** - Scale your requirements at glance.

# Computer Vision
## Applications
- **Image classification** - single object image
- **Semantic segmentation** - assign a label to each ROI in the image. E.g., clouds, sunflower, etc.
- **Instance segmentation** - highlihts objects
- **Image classification with localization** -  detect and object and the location through a bounding box
- **Object recognition** - detects an object without locations
- **Object detection** - It is like Image classification with localization
- **Pattern recognition**s
- **Facial recognition**
- **Edge detection**

## Google Solutions
- **AutoML Vision** - It allows to train a Computer Vision model without any code
- **Vision API** - It is a pre-built model available through REST API

## Model Parameters Computation Examples
It is important to know the number of model parameters when dealing with computer vision, since this number can become quite big.
- **Linear Model** - [Height * Width * Number Classes] (weights) + Number Classes (Bias)
- **Dense Layer with 300 Neurons** - [Height * Width * 300 (weights)] + 300 (Bias)
- **Convolutional 2D Layer with 10 Filters, Kernel Size 3 and Strides 1** -  10 (filters) * 9 (classes) + 10 (bias for eachfilters)

The usage of CNN reduces drastically the number of required model parameters.

## Data Scarcity
Since CNNs require tons of data, data scarcity might be a problem. It can be addressed by:
- **Data Augmentation**
    - It is important to generate data points for which you are fairly sure about the corresponding class. Ambuiguity in the generated data can result in the model not converging.
    - It is important to reflect about what features of the data point to change. Alterating the color of an image representing a Fungi, might alter its label too and thus the model's performance. Or think about the color sequence of a Flag, that's not possible to flip horizontally.
    - `tf.image` provides several functions to perform data augmentation, like `tf.image.stateless_random_<method>`.
    - It is also possible to define a custom augmentation function `def augmentation_function` and then use `tf.data.map` to apply that function to each data point. Since data points are independent, this process can be parallelized through `tf.py_function` in each GPU.
    - Also Keras offers data augmentation layers.
- **Transfer Learning**
    - It tackles the problem of Data Scarcity by not adding more data, but by decreasing the need of data by initialising the parameters with better values. 
    - This approach will remove the last few layers of the Neural Network, since they are the ones more closed to the specific task of the original trained model, and re-train them with the new specific problem's data. 
    - It is not possible to say where to cut the NN layers, so it's a best practice to cut just after the last Convolutional Layer. 
    - Two possible approaches:
        - Leave the original layers' weights unchanged and not train them &rarr; good when there are not much data &rarr; risk of overfitting
        - Change also original layers' weights and train them &rarr; good when you have more data

# Natural Language Processing
## Applications
- **Text-to-Speech and Speech-to-Text**
- **Text Classification** - It includes also Sentiment Analysis
- **Entity Extraction**
- **Machine Translation**
- **Interactive Conversation**

## Model Types
- **One-to-Sequence** - It is given with an image and it returns, for example, a description
- **Sequence-to-one** - It is given with a text and it returns, for example, a label for that text (e.g., the topic, the sentiment, etc.)
- **Sequence-to-Sequence** - It is a classical translator or LLM

## Google Pre-Build NLP APIs
### Dialogflow
It is a Natural Language Understanding (NLU) platform to design and integrate a conversational user interface. In can ingest/output both audio and text.

It offers two types of services:
- **Dialogflow Essentials (ES)** - It provides a standard agent type, suitable for small and simple agents.
- **Dialogflow Customer Experience (CX)** - It provides an advanced agent suitable for large and complex agents.

### Natural Language API
It is a set of pre-trained models that allow to easily apply NLU to applications. It includes:
- Sentiment analysis
- Entity analysis
- Entity sentiment analysis
- Content classification
- Syntax analysis

### Healthcare Natural Language API
It provides real-time analysis of insights stored in unstructured medical text.

## Google Solutions
### Contact Center AI (CCAI)
It aims to introduce AI in Contact Centers, in order to increase the operational efficiency with minimum AI expertise.
It combines:
- Dialogflow
- Agent Assist
- Insights

### Document AI
It takes unstructured data and provides structured data, easier to understand. For example, it can takes an image and returns a structured JSON file.

Human reviews can be added to further improve the accuracy.

A general or a specialized processor can be selected to better address the particular task. Specialized processors can be built yourself or from Google

## AutoML
It has three objectives for NLP:
- Classification
- Entity Extraction
- Sentiment Analysis