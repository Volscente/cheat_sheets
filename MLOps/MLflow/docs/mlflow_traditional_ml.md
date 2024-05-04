# Hyperparameters Tuning
## Child Runs
One of the core features is the concept of *child runs* in MLflow. 
When performing hyperparameter tuning, each iteration (or trial) in Optuna/Hyperopt/GridSearchCV can be considered 
a *child run*. This allows to group all the runs under one primary *parent run*, ensuring that the MLflow UI remains 
organized and interpretable. Each child run will track the specific hyperparameters used and the resulting metrics, 
providing a consolidated view of the entire optimization process.

