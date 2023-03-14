# Introduction
## Definition
MLflow is an open source platform for managing machine learning workflows.

## Terminology
### Run
A run is a collection of parameters, metrics, labels, and artifacts related to the training process of a machine learning model.

### Experiment
An experiment is the basic unit of MLflow organization. All MLflow runs belong to an experiment. 
For each experiment, you can analyze and compare the results of different runs, 
and easily retrieve metadata artifacts for analysis using downstream tools. 
Experiments are maintained on an MLflow tracking server

# MLflow Tracking
## Definition
It allows to record machine learning model training sessions and allows to query them.
It is composed by an API and a user interface component.

## Tracking Components
- **Source** - It can be the name of the file that launches the run. 
If using MLflow project, it can be the name of the project and the entry point of the run
- **Code Version** - In MLflow project, it's the Git commit hash
- **Parameters** - Key-value input parameters that you want to track
- **Artifacts** - They are output files like images, models (pickle) or parquet files
- **Start and End Time**
- **Metrics** - Key-value metrics containing numeric values. It allows to visualise the full history of each metric.

## Tracking UI
It allows to visualise, compare and search runs. Additionally, it lets you download metadata or artifacts for runs, 
which you can input for analysis in other tools. MLflow logs information about runs in an mlruns directory; 
in order to view the data, you can run the MLflow UI one directory above the mlruns folder.

Notable features of the tracking UI include listing and comparison of runs by experiments, 
and downloading the results of your runs. Additionally, you can search runs by metric value or parameters, 
as well as visualize metrics of each run.