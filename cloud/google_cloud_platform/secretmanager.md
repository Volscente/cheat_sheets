# Introduction
This package allows to programmatically interact with the GCP Project Secret Manager.

## Import
```
from google.cloud import secretmanager
```

# Secret Manager Service Client
## Instantiate
```
# Create the Secret Manager client
secret_manager_client = secretmanager.SecretManagerServiceClient()
```
**NOTE:** If no `credentials` argument is passed, it would be directly derived from the file: `$HOME/.config/gcloud/application_default_credentials.json`
and the Active Account (`gcloud auth list`)

## Read Secret
```
# Read the secret
secret = secret_manager_client.access_secret_version(request={"name": "projects/<project_number>/secrets/<secret_name>/versions/<version>"}).payload.data.decode("utf-8")
```