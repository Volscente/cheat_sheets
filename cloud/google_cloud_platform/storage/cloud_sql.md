# Import
## BigQuery
The following will details how to import data from BigQuery into a PostgreSQL instance in Cloud SQL.

Step 1: Prepare the data in a dedicated BigQuery table.

> [!NOTE]
> In case the original table is too big, this is a good place
> where starting a fresh table through an ad-hoc query. Possible name of the layer would be **raw_**

Step 2: Export the table in **raw_** into a Google Cloud Storage Bucket.

> [!NOTE]
> In case the table contains nested schema, the export would not succeeed.
