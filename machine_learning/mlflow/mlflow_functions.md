# Tracking Functions
## MLflow UI
To access the MLflow Trakcing UI, navigate into the directory that contains the folder `mlruns` and type `mlflow ui` 

## Experiment
### Create Experiment
``` python
# Define experiment name
mlflow_experiment_name = '<experiment_name>'

# Create experiment or retrieve already existing experiment
try:
    mlflow_experiment_id = mlflow.create_experiment(name=mlflow_experiment_name)
except Exception as e:
    mlflow_experiment_id = mlflow.get_experiment_by_name(mlflow_experiment_name).experiment_id
```

## Run
### Start
``` python
# Start the run with an optional name
mlflow.start_run(run_name='<run_name>')
```

### End
``` python
# End the current MLflow Run
mlflow.end_run()
```

## Logging
### Log Parameters
``` python
# Log Parameter
mlflow.log_param('<parameter_name>', <value>)
```

### Log Metrics
``` python
# Log Metric
mlflow.log_metric('<metric_name>', <value>)
```

### Set Tag
``` python
# Set a Run Tag
mlflow.set_tag('<rag_name>', <value>)
```

### Save Models
``` python
# Save SKlearn model
mlflow.sklearn.log_model(<model>, '<model_name>')
```