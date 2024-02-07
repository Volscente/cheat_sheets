# GCP
## Google Build
### Submit Build
```bash
# Syntax
gcloud builds submit --region=<region> --tag gcr.io/<project_ID>/<image_name> .

# Example
gcloud builds submit --region=us-west2 --tag gcr.io/test_project_id/image_1 .

# Config
gcloud builds submit --config <config_build_file>
```

## GKE 
### Get Credentials
```bash
gcloud container clusters get-credentials <cluster_name> --zone <zone_name>
```

### Create Cluster
```bash
gcloud container clusters create-auto <name_of_clsuter> --location=us-central1
```

# Kubectl
## Deployments
### Create Deployment
```bash
kubectl create deplyment <name> --image <image>
```

### Expose Deployment
```bash
kubectl expose deployment <name> --port 80 --type LoadBalancer --target-port 8080
```