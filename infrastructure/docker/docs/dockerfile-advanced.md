## Multi-stage Builds
### Definition
There is a pratice for Dockerfile called **Builder Pattern**, which involves using two Docker images.
One to perform a build and another to ship the results of the first build without the penalty of the build-chain and tooling in the first image.

This pattern involves maintaining several files, while with Multi-stage build we can keep everything in the same Dockerfile.

With multi-stage builds, you use multiple FROM statements in your Dockerfile. 
Each FROM instruction can use a different base, and each of them begins a new stage of the build. 
You can selectively copy artifacts from one stage to another, leaving behind everything you don't want in the final image.

The following Dockerfile has two separate stages: one for building a binary, and another where the binary gets copied from the first stage into the next stage.
Everything happens in the same Dockerfile. One stage is the builder, while the second one is the runner.

```Dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.25
WORKDIR /src
COPY <<EOF ./main.go
package main

import "fmt"

func main() {
  fmt.Println("hello, world")
}
EOF
RUN go build -o /bin/hello ./main.go

FROM scratch
COPY --from=0 /bin/hello /bin/hello
CMD ["/bin/hello"]
```

### Usage
Another possibility would be to use the Builder image in order to get already a filesystem where some software are already installed, so that we can copy them
directly into the Runner image. Below we just use a uv Docker image to copy the binary instead of installing it from the beginning:

```Dockerfile
# Use a dedicated uv image to just grab the binary (Multi-stage build - Builder image)
FROM astral-sh/uv:0.5.21 AS uv_bin

# Runner image (Multi-stage build)
FROM python:3.13-slim-bookworm

# Copy uv binary from the builder image
COPY --from=uv_bin /uv /usr/local/bin/uv
```

## Best Practices
### Debian Clean Indices
When you run apt-get update, Debian downloads a bunch of index files (the "lists") telling it which software versions are available. These lists can take up 30MB–100MB. The Purpose: Once your software is installed, you don't need those lists anymore. Deleting them in the same RUN command ensures they never get saved into a Docker "layer," keeping your final image lightweight.
```Dockerfile
# Install curl for healthchecks and delete apt-get update indices
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*
```

### Bytecode Compilation
Python is an interpreted language, but it doesn't read .py files directly. It first translates them into Bytecode (.pyc).
Normally: This happens the first time you run the app.
In Docker: By setting UV_COMPILE_BYTECODE=1, uv does this during the build. The Benefit: Your app starts up instantly. It doesn't have to "warm up" by compiling files on the first request.

```Dockerfile
# Enable bytecode compilation (.pyc) for faster startup and disable dev deps
ENV UV_COMPILE_BYTECODE=1
ENV UV_NO_DEV=1
```

## Errors
### uv Workspaces
Using uv workspaces might require to specify in the Dockerfile `CMD` the specific package you're using in the workspace.

`CMD ["uv", "run", "--package", "backend", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]`

In the example above, we need to specify which package `uv run` should look into in order to find the dependency `uvicorn`.
Without the part `--packge backend`, the `CMD` would look in the root `pyproject.toml`, not founding the dependency.

In addition, the invocation of the `main.py` should happen like `backend.main:app`, assuming that the structure is: `repository_folder/backend/src/backend/main.py:app`.
