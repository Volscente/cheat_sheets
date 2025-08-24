# Introduction
## Definition
Metaflow is a human-friendly Python library that makes it straightforward to develop, deploy, 
and operate various kinds of data-intensive applications, in particular those involving data science and ML.
Metaflow was originally developed at Netflix to boost the productivity of data scientists who work on a wide 
variety of projects, from classical statistics to state-of-the-art deep learning.

## Resources
- [Tutorials](https://github.com/Netflix/metaflow/tree/master/metaflow/tutorials)

# Flows
## Steps
Execute the next step:

```python
@step
def join(self, inputs):
    print("Joining 🖇️")
    self.next(self.end)

@step
def end(self):
    print("Done! 🏁")
```
Execute two steps in parallel:

```python
import time
from metaflow import step, FlowSpec


class BranchFlow(FlowSpec):
    @step
    def start(self):
        print("Starting 👋")
        self.next(self.eat, self.drink)

    @step
    def eat(self):
        print("Pausing to eat... 🍜")
        time.sleep(10)
        self.next(self.join)

    @step
    def drink(self):
        print("Pausing to drink... 🥤")
        time.sleep(10)
        self.next(self.join)
```

 Loop steps:

 ```python
import time
from metaflow import step, FlowSpec


class ForeachFlow(FlowSpec):
    @step
    def start(self):
        self.data = ["Apple", "Orange"]
        self.next(self.process, foreach="data")

    @step
    def process(self):
        print("Processing:", self.input)
        self.fruit = self.input
        self.score = len(self.input)
        self.next(self.join)

    @step
    def join(self, inputs):
        print("Choosing the best fruit")
        self.best = max(inputs, key=lambda x: x.score).fruit
        print("Best fruit:", self.best)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    ForeachFlow()
```

## Parameters

```python
from metaflow import FlowSpec, step, Parameter


class ParameterizedFlow(FlowSpec):

    learning_rate = Parameter("lr", default=0.01)

    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        print("Learning rate value is {}".format(self.learning_rate))


if __name__ == "__main__":
    ParameterizedFlow()
```

## Docker Images
The decorator `@pypi_base` is used to freeze library dependencies for the entire flow:

```python
@pypi_base(packages={"datashader": "0.16.3", "pandas": "2.2.2", "pyarrow": "17.0.0"})
class NYCVizFlow(FlowSpec):
    pass
```

## Access Flows' Artifact
Create a Flow `ArtifactFlow`:
```python
from metaflow import FlowSpec, step


class ArtifactFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.create_artifact)

    @step
    def create_artifact(self):
        self.dataset = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.metadata_description = "created"
        self.next(self.transform_artifact)

    @step
    def transform_artifact(self):
        self.dataset = [[value * 10 for value in row] for row in self.dataset]
        self.metadata_description = "transformed"
        self.next(self.end)

    @step
    def end(self):
        print(
            "Artifact is in state `{}` with values {}".format(
                self.metadata_description, self.dataset
            )
        )


if __name__ == "__main__":
    ArtifactFlow()
```

Later on it's possible to access what was inside of it:
```python
from metaflow import Flow
run_artifacts = Flow("ArtifactFlow").latest_run.data
assert run_artifacts.dataset == [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
```


# Visualising Results
## Card Decorator
They are used to add reports to the flow's step.

It creates a "Card" artifact inside the MetaFlow UI, in order to store more information for a specific task inside the Flow.

# Next
## Commands
```bash
# Execute locally
python flow.py run
```
