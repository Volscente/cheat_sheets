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
got_pneumonia	age	weight	male	took_antibiotic_medicine	...
False	65	100	False	False	...
False	72	130	True	False	...
True	58	100	False	True	...

People take antibiotic medicines after getting pneumonia in order to recover. 
The raw data shows a strong relationship between those columns,
but took_antibiotic_medicine is frequently changed after the value for got_pneumonia is determined. 
This is target leakage.
