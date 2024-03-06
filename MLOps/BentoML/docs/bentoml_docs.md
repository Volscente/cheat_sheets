# Introduction
## Definition
It is a unified AI application framework.
It provides an end-to-end solution for streamlining the deployment process, incorporating everything for model serving, application packaging, and production deployment.

## Bento Archive File
Everything can be enclosed into an archive file called *Bento*, all the necessary packages and dependencies.
Each Bento contains an auto-generated Dockerfile for CD.

## Features
### Model Registration
BentoML offers a centralized Model Store to save all the models.

### Service Creation
Create *BentoML Services* by defining a `service.py` file.

A BentoML Service is defined by a `@bentoml.service` decorator on a Class.
```python
@bentoml.service(
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)
class Summarization:
    def __init__(self) -> None:
        # Load model into pipeline
        self.pipeline = pipeline('summarization')
    
    @bentoml.api
    def summarize(self, text: str = EXAMPLE_INPUT) -> str:
        result = self.pipeline(text)
        return result[0]['summary_text']
```

In each service, one or more APIs can be defined as function with the `@bentoml.api` decorator.

### Deployment
Before deploying the AI application, create a bentofile.yaml file, detailing all necessary build configurations such as Python dependencies and Docker settings.

The application can be then containerised into a Docker image.