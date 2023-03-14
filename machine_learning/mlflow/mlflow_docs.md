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