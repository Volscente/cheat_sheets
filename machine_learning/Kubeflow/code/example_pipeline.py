# Import Standard Libraries
from kpf import dsl, compiler
from kpf.client import Client

@dsl.component
def example_component(name: str) -> str:
    """
    This implement a component, the building block of a pipeline
    """

    return f'Hello, {name}!'

def example_pipeline(name: str) -> str:
    """
    This implement a pipeline, composed by several components
    """

    example_component_task = example_component(name=name)

    return example_component_task.output

# Compile the pipeline into a .YAML file
compiler.Compiler().compile(example_pipeline, './../compiled_pipelines/example_pipeline.yaml')

# Instance a Kubeflow Client where to submit the pipeline (e.g., GCP Vertex AI)
client = Client(host='<endpoint>')

# Create the pipeline
run = client.create_run_from_pipeline_package(
    './../compiled_pipelines/example_pipeline.yaml', 
    arguments={'recipient': 'World'})