# Introduction
The library offers several methods to manage and communicate with a BigQuery instance.
To install:
``` bash
pip install --user google-cloud-bigquery
```

# Python SDK
## Import
``` python
from google.cloud import bigquery
```

## Client
### Instantiate Client from Service Account Info
Requirements:
- Setup a Service Account for reading from BigQuery
- Create a Secret in the Secret Manager storing the Service Account keys
- Login through the gcloud CLI
``` python
# Import Standard Libraries
from google.cloud import bigquery
from google.cloud import secretmanager
from google.oauth2 import service_account

# Create the Secret Manager client
secret_manager_client = secretmanager.SecretManagerServiceClient()

# Retrieve the service_account_info as a dictionary
service_account_info = json.loads(secret_manager_client.access_secret_version(name='projects/{}/secrets/{}/versions/{}'.format(project_id, service_account_secret_name, service_account_secret_version)).payload.data.decode("utf-8"))

# Retrieve Service Account credentials
service_account_credentials = service_account.Credentials.from_service_account_info(service_account_info)

# Initialise the client
big_query_client = bigquery.Client(credentials=service_account_credentials, 
                                   project=service_account_credentials.project_id)
```

# CLI
## List Datasets
``` bash
bq ls -d
```
## Create Dataset
``` bash
bq --location=US mk --dataset \
   --description '<dataset_description>' \
   <project_id>:<dataset_name>
```
# BigQuery Machine Learning
## Create Model
``` sql
CREATE OR REPLACE MODEL
  <dataset_name>.<modeL-name> 
  
OPTIONS (model_type='linear_reg',
         input_label_cols=['<target_column>']) AS
         
SELECT
  <feature_1,
  feature_2,
  ...>
  
FROM
  <dataset_name>.<table_name>
```