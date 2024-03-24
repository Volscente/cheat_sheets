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

# Log Multiple Parameters
# Log model's hyperparameters
mlflow.log_params({'<parameter_1>': <value_1>,
                   '<parameter_2>': <value_2>})
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

### Log Plots Artifact
``` python
# Define a folder name for the EDA Plots
eda_plots_folder = 'eda_plots'

# Create an 'eda_plots' folder
if eda_plots_folder not in os.listdir():
    os.mkdir(eda_plots_folder)
    
# NOTE: Inside the mlflow.start_run()
# Create the Features Box Plots
X_train.plot(kind='box', 
             subplots=True, 
             layout=(2, 4), 
             figsize=(16, 9), 
             title='Features Box Plots')

# Save the plot
plt.savefig('./{}/features_box_plots.png'.format(eda_plots_folder))

# Log the eda_plots_folder and tracking it
mlflow.log_artifacts(eda_plots_folder)
```
**NOTE:** It is possible to do the same thing, but with .CSV files of the train & test data.