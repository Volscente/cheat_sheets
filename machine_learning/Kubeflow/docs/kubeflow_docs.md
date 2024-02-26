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
- **Custom** - Such components are built on top of Python components and are designed to loosening the hard requirements of
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
  
### Custom Components Process
- Create a `/src` directory
- Create your custom Python module (e.g. `/src/add_two_numbers.py`)
- Now define your component under `/src/my_component.py`
- Import in `/src/my_component.py` the custom Python module
```python
from kpf import dsl
from add_two_numbers import compute_sum

@dsl.component
def my_component_function(a: int, b: int) -> int:
    return compute_sum(a, b)
```

## Pipielines
They are defined by the `@dsl.pipeline` decorator and combine several components together.

## Compiler
The `kfp.compiler.Compiler()` object is used to compile a the domai-specific language (DSL) objects to a self-contained pipeline `YAML` file.

Afterwards, the `YAML` file can be submitted to a KFP-conformant backend for execution.