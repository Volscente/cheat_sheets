# General
## MLOps Definition
MLOps, short for Machine Learning Operations, is a set of practices that aims to integrate machine learning (ML) 
systems into the broader context of software **Development** and **Operations**, like in DevOps practices.

It is thus a combinations of the above mentioned two practices:
- Development (writing code)
- Operations (deploying the code)

MLOps seeks to streamline and automate the end-to-end ML lifecycle, ensuring the efficient development, deployment, 
monitoring, and maintenance of ML models.

## CI/CD
The DevOps practice is implemented in real practice through the CI/CD technologies. 

## Roles
- **Data Analyst** - Queries and analyse
- **Data Engineer** - Retrieve and clean data
- **Data Scientist** - Train models
- **Machine Learning Developer** - Create intelligent apps
- **Machine Learning Engineer** - Deploy models

## MLOps/ML Steps
1. Business Understanding and Problem Definition
2. Data Extraction
3. Data Analysis
4. Data Preparation
5. Model Training
6. Model Evaluation
7. Model Validation
8. Model Deployment/Serving
9. Model Monitoring

## Components
### Feature Store
It is a central storage solution for features that provides the following capabilities:
- Efficient sharing of features
- Reduced duplicate efforts
- Centralized management and serving of features
- Search and filter capabilities
- Managed solution for online serving at scale
- Mitigate training-serving skew
- Detect drift

# Levels
## Definition
Depending on the level of automation of the MLOps steps, there are different levels of MLOps.

## Level 0
Every step is performed manually.

## Level 1
It auitomates the training phase.

## Level 2
It automates the training, validation and deployment.

# Model Monitoring
## Definition
It is the step in which the deployed ML model is monitored in a real-world environment.
Monitoring machine learning models is crucial for ensuring their continued effectiveness and performance over time.

## Monitoring Metrics
### Data Drift
Data drift refers to the change in the distribution of input data over time. 
It occurs when the statistical properties of the incoming data to the model change significantly, 
potentially leading to degraded model performance. 
Monitoring data drift involves comparing the distribution of current data with the distribution of data used during model training

### Concept Drift
Concept drift occurs when the relationship between input features and the target variable changes over time. 
This could happen due to changes in user behavior, market trends, or other external factors.

### Model Performance Metrics
These include metrics such as accuracy, precision, recall, F1-score, ROC-AUC, etc., 
depending on the nature of the problem being solved.

### Prediction Confidence
Monitoring the confidence level or uncertainty associated with model predictions can provide insights into 
the model's reliability. Sudden changes in prediction confidence may indicate issues with model stability or data quality.

### Resource Utilization
Monitoring resource utilization metrics such as CPU usage, memory consumption, and 
inference latency helps ensure that the model is running efficiently and within acceptable performance bounds.