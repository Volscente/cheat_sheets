### Multi-stage Builds
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
