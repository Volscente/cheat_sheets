# Introduction
## Definition
It offers a centralized repository for organizing, storing and serving ML features. 
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