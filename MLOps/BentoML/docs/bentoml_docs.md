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

A service can be run through the following command.
```shell
bentoml serve service:<service_class_name>
```

### Deployment
Before deploying the AI application, create a bentofile.yaml file, detailing all necessary build configurations such as Python dependencies and Docker settings.

The application can be then containerised into a Docker image.

# Services
## Definition
They are the instrument by which serving models through BentoML.

## Implementation
### Services
Each service is defined by the `@bentoml.service` decorator for a class. Each class is a service.

Service configuration can be specified in the decorator
```python
@bentoml.service(
    resources={"memory": "500MiB"},
    traffic={"timeout": 10},
)
class Summarization:
    pass
```

### APIs
One service can have several APIs defined as functions inside the class. Each API is defined by
the `@bentoml.api` decorator.

API route can be specified in the decorator
```python
@bentoml.api(route="/custom/url/name")
def summarize(self, text: str) -> str:
    result = self.pipeline(text)
    return result[0]['summary_text']
```

## Testing Services
A service can be started locally through `bentoml serve <service:class_name>`.

It would be available at http://localhost:3000/<class_name>. 