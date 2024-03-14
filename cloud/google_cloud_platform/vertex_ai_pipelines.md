# Introduction
## Resources
- [Colab Example](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/lightweight_functions_component_io_kfp.ipynb)

## Definition
Vertex AI Pipelines lets you automate, monitor, 
and govern your machine learning (ML) systems in a serverless manner by using ML pipelines to orchestrate your ML workflows. 
You can batch run ML pipelines defined using the Kubeflow Pipelines (Kubeflow Pipelines) or 
the TensorFlow Extended (TFX) framework. Both frameworks require to compile the pipeline as a YAML file and submit it.

## ML Pipelines
An **ML Pipeline** is a portable description of an MLOps workflow as a series of steps called *pipeline tasks*.

An ML Pipline is a DAG (Directed Acyclic Graph) of containerized pipeline tasks, that are interconnected
using input-output dependencies.

## Pipeline Components
A pipeline component is a self-contained set of code that performs a specific step of an ML workflow.

It consists of:
- Inputs
- Outputs
- Logic (executable code)

There can be either predefined or custom components.

## Pipeline Task
It is the instantiation of a pipeline component. It is the actual execution of that pipeline component in the ML pipeline.

## Pipeline Run
It is the execution of an ML pipeline. 
All the artifacts generated in a Pipeline Run are stored into *Vertex ML Metadata*.

## Vertex AI Experiments
THey are a collection of Pipelines Runs.

# ML Pipelines
## Lifecycle
1. Define the ML pipeline by choosing the ML framework (Kubeflow or TFX) and define the pipeline components
2. Compile to generate the YAML file and upload it
3. Run the ML Pipeline
4. Monitor, visualise and analyse runs

## Submit Pipeline Run
### Requirements
Set the `GOOGLE_APPLICATION_CREDENTIALS` to the corresponding `JSON` file.
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
```

### Uploading YAML File
After the Pipeline has been compiled into a `YAML` file, it can be uploaded into Vertex AI Pipeline in order to
create a Pipeline Run.
```python
import google.cloud.aiplatform as aip

# Initialise AI Platform object
aip.init(
    project=project_id,
    location=PROJECT_REGION,
)

# Prepare the pipeline job
job = aip.PipelineJob(
    display_name="automl-image-training-v2",
    template_path="image_classif_pipeline.yaml",
    pipeline_root=pipeline_root_path,
    parameter_values={
        'project_id': project_id
    }
)

```