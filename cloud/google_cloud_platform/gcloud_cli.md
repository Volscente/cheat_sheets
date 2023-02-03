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

## Set Project
Set the default project
```
gcloud config set project <project_id>
```