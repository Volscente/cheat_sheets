# Introduction
## Resources
- [Documentation](https://www.kubeflow.org/docs/)
- [Slack Community](https://www.kubeflow.org/docs/about/community/)

## Definition
It is a complete Machine Development Framework based on Kubernetes, with the aim of working with different platforms (GCP, AWS and Azure) and technologies (Scikit-Learn, PyTorch, TensorFlow, Jupyter Notebook, XGBoost, HuggingFace and Horvod).

![Kubeflow Components](./../images/kubeflow_image_1.svg)

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
- **Python** - Defined through Python functions and `@dsl.component` decorator
- **Custom/Containerized Python** - Such components are built on top of Python components and are designed to loosening the hard requirements of
Python components. Thanks to custom components, Python components can rely on modules and imports outside the function.

### Python Components Limitations
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
They are defined by the `@dsl.pipeline` decorator and combine several components together.

```python
@dsl.pipeline
def addition_pipeline(x: int, y: int) -> int:
    task1 = add(a=x, b=y)
    task2 = add(a=task1.output, b=x)
    return task2.output
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
