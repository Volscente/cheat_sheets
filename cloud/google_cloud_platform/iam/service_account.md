# Introduction
It allows to manage Service Accounts from Python.

## Import
```
from google.oauth2 import service_account
```

# Credentials
## Service Account Info
Requirements:
- Create a Service Account
- Store the Service Account Keys as a Secret in the Secret Manager
``` python
# Import Standar Libraries
from google.cloud import secretmanager
from google.oauth2 import service_account

# Create the Secret Manager client
secret_manager_client = secretmanager.SecretManagerServiceClient()

# Retrieve the service_account_info as a dictionary
service_account_info = json.loads(secret_manager_client.access_secret_version(name='projects/{}/secrets/{}/versions/{}'.format(project_id, service_account_secret_name, service_account_secret_version)).payload.data.decode("utf-8"))

# Retrieve Service Account credentials
service_account_credentials = service_account.Credentials.from_service_account_info(service_account_info)
```

## Assign Role
From the gcloud shell:
```bash
sudo gcloud projects add-iam-policy-binding my-project-id --member="serviceAccount:712912383210-compute@developer.gserviceaccount.com" --role="roles/artifactregistry.reader"
```
