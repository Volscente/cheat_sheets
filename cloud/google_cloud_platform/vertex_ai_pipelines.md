# Introduction
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

# ML Pipelines
## Lifecycle
1. Define the ML pipeline by choosing the ML framework (Kubeflow or TFX) and define the pipeline components
2. Compile to generate the YAML file and upload it
3. Run the ML Pipeline
4. Monitor, visualise and analyse runs