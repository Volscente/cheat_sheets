# Setup & Requirements
## Service Account
You should add the role `Storage Admin` with `Full control of GCS resources` to the default service account.

# CLI Commands
## Create
```bash
gcloud storage buckets create gs://qwiklabs-gcp-03-633e0dea4408
```

## Copy File
```bash
gcloud storage cp basic_pipeline.json gs://qwiklabs-gcp-03-633e0dea4408/pipeline-input/basic_pipeline.json
```

# UI
## Create from .json
- Go to the `Vertex AI > Pipelines > Create Run`
- Select `Import from Cloud Storage`
- Select the .json file

