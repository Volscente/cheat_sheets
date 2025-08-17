# Introduction
## Definition
Metaflow is a human-friendly Python library that makes it straightforward to develop, deploy, 
and operate various kinds of data-intensive applications, in particular those involving data science and ML.
Metaflow was originally developed at Netflix to boost the productivity of data scientists who work on a wide 
variety of projects, from classical statistics to state-of-the-art deep learning.

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

# Next
## Commands
```bash
# Execute locally
python flow.py run
```
