# Introduction
## Resources
- [Create a build configuration file](https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration#yaml)
- [Substituting variable values](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values)
- [Build container images](https://cloud.google.com/build/docs/building/build-containers)
- [Cloud builders](https://cloud.google.com/build/docs/cloud-builders)
- [Using community-contributed builders and custom builders](https://cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders)
- [Configure user-specified service accounts](https://cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts)

## Scope
It is a service dedicated to build Docker images or Vertex AI Pipeline templates.

In general, any kind of build can be executed here.

## Process
1. Create a Service Account. This would be used to trigger the Cloud Build build instance on Google Cloud Platform
2. Create a Cloud Storage bucket where to store the logs
3. Create the Artifact Registry for Docker Images and/or Kubeflow pipelines
4. Define the `cloudbuild.yml`
5. Submit the build to Google Cloud Build

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

## Step 4 - Cloudbuild.yml Example
```yml
# Build the Docker image for the pyhon container used in the Kubeflow Pipeline
# Configurations of the python container are in the Dockerfile
steps:
- id: build-pipeline-docker-image
  name: 'gcr.io/cloud-builders/docker' # Container image name
  args:
    - build
    - --file
    - ./Dockerfile.my_project
    - --tag
    - $LOCATION-docker.pkg.dev/$PROJECT_ID/$_IMAGE_REPOSITORY_NAME/my-project-docker-image:$TAG_NAME
    - --tag
    - $LOCATION-docker.pkg.dev/$PROJECT_ID/$_IMAGE_REPOSITORY_NAME/my-project-docker-imag:$_MODEL_VERSION
    - '.'
# Compile the Kubeflow pipeline as specified in the pipelines/pipelines.py file
# Providing also the pipeline arguments
# NOTES: "images" field does not refer to this step. This step just runs the "pipelines.py" main function.
- id: compile-pipelines
  name: 'python:3.12' # Container image name
  script: |
    pip install kfp==2.7.0 &&\
    python pipelines/pipelines.py \
      --python_image_name=$LOCATION-docker.pkg.dev/$PROJECT_ID/$_IMAGE_REPOSITORY_NAME/my-project-docker-image:$TAG_NAME \
      --pipeline_repository_name=https://$LOCATION-kfp.pkg.dev/$PROJECT_ID/$_PIPELINE_REPOSITORY_NAME \
      --tag=$TAG_NAME \
      --model_version=$_MODEL_VERSION \
      --project_id=$PROJECT_ID \
# Specify the image location on the artifact registry for the step "build-pipeline-docker-image"
images:
- $LOCATION-docker.pkg.dev/$PROJECT_ID/$_IMAGE_REPOSITORY_NAME/mds-evaluation-image:$TAG_NAME
substitutions:
  _IMAGE_REPOSITORY_NAME: my-project-docker-registry # default
  _PIPELINE_REPOSITORY_NAME: kf-my-project-pipelines # default
  _COMPONENT: cool-project-name # default
  _MODEL_VERSION: latest # default
# Use a specific service account
logsBucket: 'gs://my-project-google-cloud-storage-bucket/cloud_build_logs'
serviceAccount: 'projects/$PROJECT_ID/serviceAccounts/project-service-account@e-company-name.iam.gserviceaccount.com'
options:
    dynamicSubstitutions: true
    automapSubstitutions: true
    logging: GCS_ONLY
# Specify the Cloud Build tags
tags: [$_COMPONENT, $_MODEL_VERSION]
```

## Step 5 - Submit the build to Google Cloud Build
```bash
#!/bin/bash
# Trigger the Google Cloud Build pipeline as defined in /pipelines/cloudbuild.yaml to build and push
# The Docker image for the Kubeflow Pipeline and the Kubeflow Pipeline Vertex AI template

# Read variables
source ./scripts/env.sh

# Define substitutions for triggering the Google Cloud Build
SUBSTITUTIONS=\
_IMAGE_REPOSITORY_NAME=$IMAGE_REPOSITORY_NAME,\
_PIPELINE_REPOSITORY_NAME=$PIPELINE_REPOSITORY_NAME,\
TAG_NAME=$TAG_NAME,\
_COMPONENT=$COMPONENT,\
_MODEL_VERSION=$MODEL_VERSION

# Trigger the Google Cloud Build
gcloud builds submit \
    --config ./pipelines/cloudbuild_evaluation_pipeline.yaml \
    --region=$LOCATION \
    --project=$PROJECT_ID \
    --substitutions=$SUBSTITUTIONS
```
