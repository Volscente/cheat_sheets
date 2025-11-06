# Import
## BigQuery
The following will details how to import data from BigQuery into a PostgreSQL instance in Cloud SQL.

Step 1: Prepare the data in a dedicated BigQuery table.

> [!NOTE]
> In case the original table is too big, this is a good place
> where starting a fresh table through an ad-hoc query. Possible name of the layer would be **raw_**

Step 2: Export the table in **raw_** into a Google Cloud Storage Bucket.
```bash
bq extract --destination_format=CSV dh-global-sales-data-dev:dim_mds_model_data.talabat_items_data gs://dh-menu-digitalisation-service-data-storage/talabat-items-data/bigquery_export.csv
```

> [!NOTE]
> In case the table contains nested schema, the export would not succeeed.

step 3: Grant the Cloud SQL Service Account access to the GCS Bucket

```bash
# Retrieve service account
gcloud sql instances describe mds-postgresql-prod --format="value(serviceAccountEmailAddress)"

# Grant access to the GCS Bucket
gsutil iam ch serviceAccount:p433987166697-7gismu@gcp-sa-cloud-sql.iam.gserviceaccount.com:roles/storage.objectViewer gs://dh-menu-digitalisation-service-data-storage
```

Step 4: Create the table with the Schema

> [!NOTE]
> Generate it by taking the first 5 rows of the CSV file and ask ChatGPT to generate the query with the schema.

Step 5: Export without header
It is mandatory for the uploading in Cloud SQL to remove the CSV header

```bash
bq extract \
  --destination_format=CSV \
  --field_delimiter="," \
  --print_header=false \
  dh-global-sales-data-dev:dim_mds_model_data.talabat_items_data \
  gs://dh-menu-digitalisation-service-data-storage/talabat-items-data/bigquery_export_no_header.csv
```
