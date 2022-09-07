# Introduction

## Definition
Data leakage (or leakage) happens when your training data contains information about the target, 
but similar data will not be available when the model is used for prediction. 
This leads to high performance on the training set (and possibly even the validation data), 
but the model will perform poorly in production.

## types

### Target Leakage
**Target leakage** occurs when your predictors include data that will not be available at the time you make predictions. 
It is important to think about target leakage in terms of the timing or chronological order that data becomes available, 
not merely whether a feature helps make good predictions.

Example:

![img_5.png](../images/data_science/img_5.png)

People take antibiotic medicines after getting pneumonia in order to recover. 
The raw data shows a strong relationship between those columns,
but took_antibiotic_medicine is frequently changed after the value for got_pneumonia is determined. 
This is target leakage.


### Train-Test Contamination
A different type of leak occurs when you aren't careful to distinguish training data from validation data.

Recall that validation is meant to be a measure of how the model does on data that it hasn't considered before. 
You can corrupt this process in subtle ways if the validation data affects the preprocessing behavior. 
This is sometimes called **train-test contamination**.

For example, imagine you run preprocessing (like fitting an imputer for missing values) before calling `train_test_split()`. 
The end result? Your model may get good validation scores, giving you great confidence in it, 
but perform poorly when you deploy it to make decisions.

After all, you incorporated data from the validation or test data into how you make predictions, 
so the may do well on that particular data even if it can't generalize to new data. 
This problem becomes even more subtle (and more dangerous) when you do more complex feature engineering.

If your validation is based on a simple train-test split, exclude the validation data from any type of fitting, 
including the fitting of preprocessing steps. This is easier if you use scikit-learn pipelines. 
When using cross-validation, it's even more critical that you do your preprocessing inside the pipeline!