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

## Login
Ensure to login with your account through:
```
gcloud auth application-default login
```

# Authentication

## List
This command shows the current available users and the currently active one.
```
gcloud auth list
```