# Introduction
The Google Cloud CLI is the best way to manage your Google projects/services through the command line.

## Installation
This is the [Documentation Reference](https://cloud.google.com/sdk/docs/install-sdk) for installing the gcloud CLI.

Once the `tar.gz` is extracted, move the entire folder into the desired location. Finally, run the following commands to
install it:
```
# Navigate into the directory
cd google-cloud-sdk

# Install the gcloud CLI
./install.sh
```

## Initialisation
After installing the gcloud CLI, you need to initialise it through the following command:
```
gcloud init
```

## Account Login
Ensure to login with your account through:
```
gcloud auth application-default login
```
The credentials would be logged into the following file `$HOME/.config/gcloud/application_default_credentials.json`

# Authentication

## List
This command shows the current available users and the currently active one.
```
gcloud auth list
```

## Project Login
Authenticate your current active account (`gcloud auth list`) into the specified project:
```
# Authenticate to the project
gcloud auth login --project=<project_id>
```

# Secret Manager
## Documentation
Refer to [this documentation](https://cloud.google.com/secret-manager/docs/reference/libraries).

## Access Secret
```
# Access the latest version of the secret
gcloud secrets versions access latest --secret=<secret_name>
```

# Configuration

## Project
```bash
# Get default project
gcloud config project get

# Set default project
gcloud config set project <project_id>
```

# Vertex AI
## Custom Jobs
You can run the following command to create a Docker image locally, even without a Dockerfile, to test your Python code:
```bash
gcloud beta ai custom-jobs local-run \
    --base-image=BASE_IMAGE_URI \
    --work-dir=WORKING_DIRECTORY \
    --script=SCRIPT_PATH \
    --output-image-url=OUTPUT_IMAGE_NAME \
    --  \
    --arg1=value1 \
```
- `BASE_IMAGE_URI`: The URI of the base image to use for the Docker image. It must be a URI to a Docker image in a registry.
- `WORKING_DIRECTORY`: The directory to use as the working directory for the Docker image. The lowest level directory that contains all the files needed to run the training script.
- `SCRIPT_PATH`: The path to the training script, relative to the working directory.
- `OUTPUT_IMAGE_NAME`: The name of the output Docker image.
- `--`: The double dash is used to separate the gcloud command from the arguments to pass to the Docker image.

It is also possible to use a `Cloud Build` configuration file to build the Docker image:
```yaml
steps:
  - name: 'gcr.io/kaniko-project/executor:latest'
    args:
    - --destination=$_REGISTRY/$PROJECT_ID/$_TRAINER_NAME:$TAG_NAME
    - --dockerfile=$_DOCKERFILE
    - --cache=true
    - --cache-ttl=168h
substitions:
  _REGISTRY: eu.gcr.io
  _TRAINER_NAME: my_job
  _DOCKERFILE: Dockerfile
  _TAG_NAME: latest
timeout: 3600s
```
Then, run the following command to build the Docker image:
```bash
