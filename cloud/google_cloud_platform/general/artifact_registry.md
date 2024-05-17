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
3. 
