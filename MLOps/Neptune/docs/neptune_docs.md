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

## Quickstart
```python
import neptune

# Connect to Neptune and create a run
run = neptune.init_run()

run['test/f1_score'] = 0.01

for _ in range(100):
    run['train/accuracy'] = append(0.90)

run['paramters'] = {
    'batch_size': 64,
    'dropout': 0.5
}

run['data/train_version'].track_files('train/images')

run['model/weights'].upload('my_model.pkl')

run.stop()
```