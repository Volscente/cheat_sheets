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
## Components
They are defined by the `@dsl.component` decorator and are the building blocks of a Kubeflow Pipeline.

## Pipielines
They are defined by the `@dsl.pipeline` decorator and combine several components together.

## Compiler
The `kfp.compiler.Compiler()` object is used to compile a the domai-specific language (DSL) objects to a self-contained pipeline `YAML` file.

Afterwards, the `YAML` file can be submitted to a KFP-conformant backend for execution.