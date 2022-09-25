# Regression

## SMAPE
```python
# Define function to compute the SMAPE
def smape(y_true, y_pred):
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 200.0
    diff = np.abs(y_true - y_pred) / denominator
    diff[denominator == 0] = 0.0
    return np.nanmean(diff)
```
**NOTE:** For predictions coming from XGB, there's the need to reshape the Dataframe
```python
# Get number of sold predictions
predictions_xgb = pipe_xgb.predict(X_test).reshape(-1, 1) # Reshape is necessary for the SMAPE function
```
