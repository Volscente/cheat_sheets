# Introduction
The library offers several methods to manage and communicate with a BigQuery instance.

Installation:
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

## BigFrames
### Read Data
```python
# Import Standard Libraries
import pandas as pd
import bigframes.pandas as bf

# Setup BigFrames Options
bf.options.bigquery.project = 'project_id'
bf.options.bigquery.location = 'location'
bf.options.display.progress_bar = True

# Define the query
query = """
SELECT *
FROM `{dataset_id}.{table_name}`
""".format(dataset_id=dataset_id, table_name=table_name)

data_bigframes = bf.read_gbq(query)
data_dataframe = data_bigframes.to_pandas()
```

### Upload Pandas DataFrame
```python
# Import Standard Libraries
import pandas as pd
import bigframes.pandas as bf

# Setup BigFrames Options
bf.options.bigquery.project = 'project_id'
bf.options.bigquery.location = 'location'
bf.options.display.progress_bar = True

# Read data
data = pd.read_csv('./local_data.csv')

# Convert to BigFrames
data_to_upload = bf.read_pandas(data)

# Upload the row
data_to_upload.to_gbq(
    destination_table=f'{dataset_id}.{mds_labels_table_id}',
    if_exists='append'
)
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
  <dataset_name>.<model_name> 
  
OPTIONS (model_type='linear_reg',
         input_label_cols=['<target_column>']) AS
         
SELECT
  <feature_1,
  feature_2,
  ...>
  
FROM
  <dataset_name>.<table_data_name>
```
## Evaluate Model
``` sql
SELECT
  *,
  SQRT(loss) AS rmse
FROM
  ML.TRAINING_INFO(MODEL <dataset_name>.<model_name>)
```
```sql
SELECT
  *
FROM
  ML.EVALUATE(MODEL <dataset_name>.<model_name>)
```

## Compute Predictions
```sql
SELECT
  *
FROM
  ML.PREDICT(MODEL `<dataset_name>.<model_name>`)
```

## Feature Engineering
### Datetime Extract
```sql
CREATE OR REPLACE MODEL
  <dataset_name>.<model_name> 
  
OPTIONS (model_type='linear_reg',
         input_label_cols=['<target_column>']) AS
         
SELECT

  <features>,
  
  EXTRACT(
    DAYOFWEEK
      FROM <date_feature>) AS dayofweek,

FROM
  <dataset_name>.<table_data_name>
```
**NOTE:** You can change the element to extract from `DAYOFWEEK` to also `HOUR`.
### Concat
```sql
CREATE OR REPLACE MODEL
  <dataset_name>.<model_name> 
  
OPTIONS (model_type='linear_reg',
         input_label_cols=['<target_column>']) AS
         
SELECT

  <features>,
  
  CONCAT(
    CAST(
        EXTRACT(
          DAYOFWEEK
          FROM pickup_datetime) AS STRING), 
    CAST(
        EXTRACT(
          HOUR
          FROM pickup_datetime) AS STRING)
  ) AS hourofday,

FROM
  <dataset_name>.<table_data_name>
```

# Query Utils
## String
```
SELECT
  SPLIT(labels.menu_image_urls[OFFSET(0)], '/')[1] AS image_url
FROM `table.labels_dataset` AS labels
WHERE 
  labels.language IS NULL
```

# Recovery
## Recover deleted table
```bash
bq cp curated_mds_model_data.evaluation_results_v2@-3600000 curated_mds_model_data.evaluation_results_v2_backup
```
