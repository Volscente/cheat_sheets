# Tracking Functions
## Run
### Start
``` python
# Start the run
mlflow.start_run()
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

### Save Models
``` python
# Save SKlearn model
mlflow.sklearn.log_model(<model>, '<model_name>')
```