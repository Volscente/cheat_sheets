# GCP
## Build & Publish Docker Image to Artifact Registry
1. Create a Drone Repository from the Drone Home Page
2. Create a Service Account on GCP with the following roles and permissions:
```
  base_roles = [
    "roles/artifactregistry.reader",
    "roles/artifactregistry.writer",
  ]
  permissions = [
    "iam.roles.get",
    "iam.roles.list",
    "resourcemanager.projects.getIamPolicy",
    "resourcemanager.projects.setIamPolicy",
    "orgpolicy.policy.get",
    "storage.managedFolders.create",
    "storage.managedFolders.delete",
    "storage.managedFolders.get",
    "storage.managedFolders.list",
    "storage.objects.create",
    "storage.objects.delete",
    "storage.objects.get",
    "storage.objects.list",
    "storage.objects.update",
    "storage.multipartUploads.create",
    "storage.multipartUploads.abort",
    "storage.multipartUploads.listParts",
    "storage.buckets.create",
    "storage.buckets.get",
    "storage.buckets.list",
  ]
```
3. Generate SA JSON keys and store them in a Drone secret.
4. Define the Drone pipeline as below
```yml
# <Docstring>
kind: pipeline
type: docker
name: default

# Trigger the build on Git Push and Git PR
trigger:
  event:
    - push
    - pull_request

steps:
- name: publish-docker-image
  image: plugins/gcr # Name of the Drone plugin
  settings:
    registry: europe-west3-docker.pkg.dev # This is the first part of GCP Artifact Registry
    repo: <GCP_PROJECT_ID>/<ARTIFACT_REGISTRY_REPOSITORY_NAME>/${DRONE_REPO} # 
    dockerfile: ./docker/<DOCKERFILE_NAME>.dockerfile
    json_key:
      from_secret: <SA_KEYS_DRONE_SECRET>
    tags:
      - ${DRONE_TAG}
```

   
