# Introduction
## Definition
Neptune.ai is an experiment tracker framework that offers:
- Data versioning
- Experiment tracking
- Model versioning

## Architecture
There are two main components:
- **Python SDK** - It allows to interact with Neptune.ai framework
- **Neptune Server** - It offers the Neptune Web Interface

### Neptune Web Interface
It is organised in:
- **Workspace** - It is usually one
- **Projects** - It is like the experiments in MLflow, where in a single project you can compare several runs
- **Runs** - It is a single experiment executions