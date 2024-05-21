# Introduction
## Resources
- [Documentation](https://www.kubeflow.org/docs/)
- [Slack Community](https://www.kubeflow.org/docs/about/community/)

## Definition
It is a complete Machine Development Framework based on Kubernetes, with the aim of working with different platforms (GCP, AWS and Azure) and technologies (Scikit-Learn, PyTorch, TensorFlow, Jupyter Notebook, XGBoost, HuggingFace and Horvod).

![Kubeflow Components](./../images/kubeflow_image_1.svg)

## Installation
### Minikube
This is the [Reference Documentation](https://dagshub.com/blog/how-to-install-kubeflow-locally/).

1. Install `minikube` to run Kubernetes (K8s) clusters locally
```bash
brew install minikube
```
2. Install `kubectl` to execute K8s commands to send to K8s clusters
```bash

brew install kubectl
```

3. Install `kustomize` to create template-free YAML files
```bash
brew install kustomize
```

4. Start a Kubernetes cluster
```bash
minikube start
```
**NOTE:** For any problem, delete the `$HOME/.kube/config` file.

5. Install Kubeflow Pipelines on the cluster
```bash
# env/platform-agnostic-pns hasn't been publically released, so you will install it from master
export PIPELINE_VERSION=2.0.5
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
```
6. Check if the Kubeflow dashboard works
```bash
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

Navigate to http://localhost:8080/.

**NOTE:** This installation seems to have problems with K8s minikube deployment.
  
## Kubeflow on GCP
Kubeflow is specifically designed to work with Kubernetes underneath. The pipelines implemented with Kubeflow can natively run on top of a Kubernetes cluster. Moreover, Vertex AI Pipeline is another level of abstractation that allows us to easily manage Kubeflow Pipelines.

## Alternative Technologies
- TFX
- Metaflow

# Building Pipelines
## DSL
It allows to build components and pipelines in order to create a DAG (Direct Acyclic Graph).

## Components
They are defined by the `@dsl.component` decorator and are the building blocks of a Kubeflow Pipeline. Each component run in a dedicated container.

There are three types of Components:
- **Built-in** - Such components are already defined and available [here](https://github.com/kubeflow/pipelines/tree/master/components)
- **Lightweight Python** - Defined through Python functions and `@dsl.component` decorator
- **Custom/Containerized Python** - Such components are built on top of Python components and are designed to loosening the hard requirements of
Lightweight Python components. Thanks to custom components, Python components can rely on modules and imports outside the function.

### Lightweight Python Components Limitations
- They can not use anything defined outside the function
- Each library used should be imported inside the component, since it runs in a dedicated container
  - It possible to overcome this problem by using the `packages_to_install` argument in the dectorator
  ```python
  @dsl.component(packages_to_install=['numpy==1.21.6'])
  def function_name():
    ...
  ```
  
Most of these limitations are fixed through the usage of **Custom Components**.
  
### Custom/Containerized Python Components Process

**Import from Other Modules**

- Create a `/src` directory
- Create your custom Python module (e.g. `/src/add_two_numbers.py`)
- Now define your component under `/src/my_component.py`
- Import in `/src/my_component.py` the custom Python module
```python
from kfp import dsl
from add_two_numbers import compute_sum

@dsl.component
def my_component_function(a: int, b: int) -> int:
    return compute_sum(a, b)
```

<br>
**Base Image**
It is possible to specify a base Docker image from a Docker registry
```python
@dsl.component(base_image="us-central1-docker.pkg.dev/project-id/artifact-registry-docker-registry/image-name@sha256:421bc4d1c48a739d0555672872163092bad2f0599e92cd0ef419e6c241270a8e")
def custom_component() -> str:

    return 'custom_component'
```


<br>

**Modify Decorator**

It is also possible to specify a `target_image` in the decorator, to tag the built container image:
```python
@dsl.component(base_image='python:3.7',
               target_image='gcr.io/my-project/my-component:v1')
def my_component_function(a: int, b: int) -> int:
    return compute_sum(a, b)
```

<br>

**Build Component**

```bash
kfp component build src/ --component-filepattern my_component.py --no-push-image
```


## Pipelines
### Definition
They are defined by the `@dsl.pipeline` decorator and combine several components together.

```python
@dsl.pipeline
def addition_pipeline(x: int, y: int) -> int:
    task1 = add(a=x, b=y)
    task2 = add(a=task1.output, b=x)
    return task2.output
```

### Arguments
The `@dsl.pipeline` can receive the following optional arguments:
- `name` is the name of the pipeline
- `description` is the description of the pipeline
- `pipeline_root` s the root path of the remote storage destination within which the tasks in your pipeline will create outputs
- `display_name` is a human-readable name for the pipeline

```python
@dsl.pipeline(name='pythagorean-theorem-pipeline',
              description='Solve for the length of a hypotenuse of a triangle with sides length `a` and `b`.',
              pipeline_root='gs://my-pipelines-bucket',
              display_name='Pythagorean pipeline.')
def pythagorean(a: float, b: float) -> float:
    pass
```

### Pipelines as Components
A Pipeline component can be used as a component in another pipeline:
```python
from kfp import dsl

@dsl.component
def square(x: float) -> float:
    return x ** 2

@dsl.component
def add(x: float, y: float) -> float:
    return x + y

@dsl.component
def square_root(x: float) -> float:
    return x ** .5

@dsl.pipeline
def square_and_sum(a: float, b: float) -> float:
    a_sq_task = square(x=a)
    b_sq_task = square(x=b)
    return add(x=a_sq_task.output, y=b_sq_task.output).output

@dsl.pipeline
def pythagorean(a: float = 1.2, b: float = 1.2) -> float:
    sq_and_sum_task = square_and_sum(a=a, b=b)
    return square_root(x=sq_and_sum_task.output).output
```

### Control Flow
```python
from kfp import dsl

@dsl.pipeline
def my_pipeline():
    coin_flip_task = flip_three_sided_coin()
    with dsl.If(coin_flip_task.output == 'heads'):
        print_comp(text='Got heads!')
    with dsl.Elif(coin_flip_task.output == 'tails'):
        print_comp(text='Got tails!')
    with dsl.Else():
        print_comp(text='Draw!')
```

## Compiler
The `kfp.compiler.Compiler()` object is used to compile to the domain-specific language (DSL) 
objects to a self-contained pipeline `YAML` file.

```python
compiler.Compiler().compile(addition_pipeline, 'pipeline.yaml')
```

Afterwards, the `YAML` file can be submitted to a KFP-conformant backend for execution (Check the **Run** section).

## Run
In order to run a Pipeline on GCP Vertex AI:
- Upload the `.YAML` file directly from the UI
- Use the SDK
```python
# Instance a Kubeflow Client where to submit the pipeline (e.g., GCP Vertex AI)
client = Client(host='<endpoint>')

# Create the pipeline
run = client.create_run_from_pipeline_package(
    './../compiled_pipelines/example_pipeline.yaml',
    arguments={'recipient': 'World'})
```
- CLI
```commandline
kfp run create --experiment-name my-experiment --package-file path_to_the_pipeline_yaml_file
```

**NOTE:** It will require a Cloud Storage bucket where to output the `output_json` with information about the pipeline's run execution exit status.

# Features
## Continuous Training
A Pipeline execution can be conditioned to trigger under certain circumstances: the evaluation metrics surpass predefined thresholds.
