# Import Standard Libraries
from kpf import dsl, compiler

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