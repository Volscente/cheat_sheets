# Introduction
## Definition
It offers a centralized repository for organizing, storing and serving ML features through a BigQuery table. 
Since it is a shared repository, it can be re-used across different use cases.

## Benefits
- Features are hard to share and reuse
- Hard to reliably serving them in production with low latency
- Inadvertent skew in feature values between training and serving (training data are different from the ones 
that are then used in production)
- 
## Terminology
- Entity Type - It is a collection of semantically related features (e.g. `Vendor` for all the features related
to a vendor object)
- Feature Ingestion - It is the process of importing feature values computed by the feature engineering jobs into the
Feature Store
- Feature Serving - It is the process of exporting stored feature values for training or inference (Batch Serving or Online Serving)

# Create a Feature Store
## Set Up Features
- Create a **BigQuery Table** or view with the features
  - Such table has to include a `feature_timestamp` for keeping track the latest non-null features set version
  - Each row is a complete feature values set, in which each column is a feature
  - Each row has a `entity_id` ID column
- Create **Feature Group** 
  - Vertex AI Feature Store page 
  - Point to the previously defined *BigQuery Table*
- Create **Features**
  - It is possible to create multiple *Features* for a *Feature Group*
  - Each feature is associated with a specific column in the *BigQuery Table*