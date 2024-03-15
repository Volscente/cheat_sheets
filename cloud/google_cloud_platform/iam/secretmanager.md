# Introduction
This package allows to programmatically interact with the GCP Project Secret Manager.

## Import
```
from google.cloud import secretmanager
```

# Secret Manager Service Client
## Instantiate
``` python
# Create the Secret Manager client
secret_manager_client = secretmanager.SecretManagerServiceClient()
```
**NOTE:** If no `credentials` argument is passed, it would be directly derived from the file: `$HOME/.config/gcloud/application_default_credentials.json`
and the Active Account (`gcloud auth list`)

## Read Secret
``` python
# Import Standard Libraries
import json
from google.oauth2 import service_account

# Secret's Information
project_id = '<project_id>'
secret_name = '<secret_name>'
secret_version = <secret_version>

# Retrieve the secret as a dictionary
secret = json.loads(secret_manager_client.access_secret_version(name='projects/{}/secrets/{}/versions/{}'.format(project_id, secret_name, secret_version)).payload.data.decode("utf-8"))
```
