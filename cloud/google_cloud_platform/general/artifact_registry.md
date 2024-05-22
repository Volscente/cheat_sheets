# Docker
## Tag & Push Images
1. Build the Dockerfile locally
```bash
# Command
docker image build -f <relative-path-to-Dockerfile> -t <image-name>:<tag> .

# Example
docker image build -f ./docker/Dockerfile -t super-cool-project:1.0.3 .
```
2. Re-tag the image for GCP
```bash
# Command
docker tag <alread-tagged-image-name>:<already-tag> <location>-docker.pkg.dev/<project-id>/<artifact-registry-name>/<image-name>:<tag>

# Example
docker tag super-cool-project:1.0.3 us-central1-docker.pkg.dev/my-project/super-cool-docker-registry/super-cool-project:1.0.3
```
3. Authenticate in GCP
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```
**NOTE:** Ensure to be already authenticated in gcloud

4. Push the image to GCP Artifact Registry
```bash
# Example
docker push us-central1-docker.pkg.dev/my-project/super-cool-project-registry/super-cool-project:1.0.3
```
5. Check the pushed images
```bash
gcloud artifacts docker images list us-central1-docker.pkg.dev/my-project/super-cool-docker-registry
```
