# Theory

## Definition
It is an ensemble method, which combines the predictions of several models, that is called "Gradient Boosting".

## Process
Gradient boosting is a method that goes through cycles to iteratively add models into an ensemble.

It begins by initializing the ensemble with a single model, whose predictions can be pretty naive.

Then, we start the cycle:

- First, we use the current ensemble to generate predictions for each observation in the dataset. 
To make a prediction, we add the predictions from all models in the ensemble.
- These predictions are used to calculate a loss function (like mean squared error, for instance).
- Then, we use the loss function to fit a new model that will be added to the ensemble. Specifically, 
we determine model parameters so that adding this new model to the ensemble will reduce the loss. 
(Side note: The "gradient" in "gradient boosting" refers to the fact that we'll use gradient descent on 
the loss function to determine the parameters in this new model.)
- Finally, we add the new model to ensemble, and ...
- ... repeat!

![img_4.png](../images/data_science/img_4.png)

## Parameters

### n_estimators
It specifies how many times to go through the modeling cycle described above. 
It is equal to the number of models that we include in the ensemble.