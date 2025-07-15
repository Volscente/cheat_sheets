# Introduction
## Scope
It is a service dedicated to build Docker images or Vertex AI Pipeline templates.

In general, any kind of build can be executed here.

## Process
1. Create a Service Account. This would be used to trigger the Cloud Build build instance on Google Cloud Platform
2. Create a Cloud Storage bucket where to store the logs
3. Create the Artifact Registry for Docker Images and/or Kubeflow pipelines

# Steps
## Prerequisites
Define a `env.sh` where to store all the variables.

```bash
#!/bin/bash
export PROJECT_ID=my_project
export LOCATION=us-central1
export IMAGE_REPOSITORY_NAME=docker-images-repo-name
export PIPELINE_REPOSITORY_NAME=kf-pipelines-repo-name
export TAG_NAME=latest
```

## Step 3 - Create Artifact Registry
```bash
# Read variables from env.sh
source ./scripts/env.sh

# Create artifact registry for Docker images
gcloud artifacts repositories create \
    $IMAGE_REPOSITORY_NAME  \
    --repository-format=docker \
    --location=$LOCATION \
    --project=$PROJECT_ID

# Create artifact registry for Kubeflow pipelines
gcloud artifacts repositories create \
    $PIPELINE_REPOSITORY_NAME  \
    --repository-format=KFP \
    --location=$LOCATION \
    --project=$PROJECT_ID
```
