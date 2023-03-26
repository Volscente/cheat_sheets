# Plot Training & Test Loss
```python
# Construct model_metric DataFrame
model_metrics = pd.DataFrame({'Training Loss': train_loss, 
                              'Testing Loss': test_loss, 
                              'Training Accuracy': train_accuracy, 
                              'Testing Accuracy': test_accuracy}, 
                             index=np.arange(1, epochs + 1))
                             
# Plot Training & Test Loss
figure, ax = plt.subplots(figsize=(9, 9))

sns.lineplot(
    data=model_metrics, 
    x=model_metrics.index.tolist(), 
    y='Training Loss', 
    label='Training Loss')

sns.lineplot(
    data=model_metrics, 
    x=model_metrics.index.tolist(), 
    y='Testing Loss', 
    label='Testing Loss')

ax.set_ylabel('Loss', 
              fontweight='bold')

ax.set_xlabel('Epochs', 
              fontweight='bold')

ax.set_title('Training & Test Loss', 
             fontsize=14)

plt.xticks(model_metrics.index.tolist())

plt.show()                            
```

# Regression

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

# Classification

## Confusion Matrix
``` python
from sklearn.metrics import confusion_matrix

# Compute confusion matrix
test_data_confusion_matrix = confusion_matrix(test_data['label'], test_data['prediction'])

# Plot confusion matrix
ax = sns.heatmap(test_data_confusion_matrix, 
                 annot=True,
                 cmap=sns.light_palette("seagreen", as_cmap=True),
                 fmt='g')

ax.set_ylabel('True Label', 
              fontweight='bold')

ax.set_xlabel('Predicted Label', 
              fontweight='bold')

ax.set_title('Confusion Matrix', 
             fontsize=14)

plt.show()
```
