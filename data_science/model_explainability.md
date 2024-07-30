# Model Comparison
## Single Metric
``` python
# Sort dataframe by the metric
performance.sort_values('RMSE', inplace=True)

# Create figure
figure = plt.figure(tight_layout=True, figsize=(9, 6))

# Plot models' metrics
ax = sns.barplot(data=performance, 
                 x='RMSE', 
                 y=performance.index.tolist())

# Set title
ax.set_title('Models Comparison', 
             fontsize=24)

# Set tick rotation
plt.xticks(rotation=45)

# Plot with tight layout
plt.tight_layout()
```

## Multiple Metrics
```python
# Create figure
figure = plt.figure(tight_layout=True, figsize=(16, 6))

# Melt the dataframe
melted_performance = pd.melt(performance.reset_index(names='Models'), id_vars='Models', var_name='Metric', value_name='Value')

# Plot models' metrics
ax = sns.barplot(data=melted_performance,
                 x='Models',
                 y='Value', 
                 hue='Metric')


# Set labels
ax.set_xlabel('Models', fontsize=20, weight='bold')
ax.set_ylabel('Metric Value', fontsize=20, weight='bold')

# Retrieve legend information
handles = ax.get_legend_handles_labels()[0]
labels = ax.get_legend_handles_labels()[1]
ax.legend().remove()

# Set the legend
figure.legend(handles, 
              labels, 
              loc='center', 
              bbox_to_anchor=(0.5, 1.03), 
              fontsize=12,
              ncol=len(metrics))

# Set figure Title
figure.suptitle('Model Comparison',
                fontweight='bold',
                fontsize=24)

# Plot with tight layout
plt.tight_layout()
```

# Feature Importance 
``` python
# Define figure and axes
figure, ax = plt.subplots(2, 1, figsize=(16, 9))
ax = ax.flatten()

# Fetch all the trained models
for index, model_name in enumerate(models.keys()):
    
    # Retrieve feature names
    feature_names = models[model_name].feature_names_in_
    
    # Retrieve pipeline model's step name
    pipe_model_step_name = list(models[model_name].named_steps.keys())[-1]
    
    # Retrieve feature importances values
    try:
        # ree-based models
        feautre_importance_values = models[model_name].named_steps[pipe_model_step_name].feature_importances_
    except:
        # Regression-based models
        feautre_importance_values = models[model_name].named_steps[pipe_model_step_name].coef_.reshape(-1,)
        
    
    
    # Compute the feature importance
    feature_importance = sorted(list(zip(feature_names,
                                         feautre_importance_values)),
                                key=lambda x: x[1], reverse=True)

    # Transform it into a DataFrame
    feature_importance_df = pd.DataFrame(feature_importance,
                                         columns= ['Feature', 'Importance'])    
    
    # Plot the feature importance
    sns.barplot(data=feature_importance_df,
               x='Feature',
               y='Importance', 
               ax=ax[index])

    # Set title
    ax[index].set_title(model_name, 
                 fontsize=20, 
                 fontweight='bold')

    ax[index].set_xticklabels(feature_importance_df['Feature'],
                              fontsize=8,
                              rotation=45)

figure.suptitle('Feature Importance',
                fontweight='bold',
                fontsize=24)
    
plt.tight_layout()
    
plt.show()
```

# Learning Curves
``` python
# Define figure and axes
figure, ax = plt.subplots(1, 2, figsize=(12, 6))
ax = ax.flatten()

# Fetch all the trained models
for index, model_name in enumerate(models.keys()):

    # Plot the Learning Curve
    LearningCurveDisplay.from_estimator(models[model_name], 
                                        **learning_curves_display_paramters,
                                        ax=ax[index])
    
    # Retrieve legend information
    handles = ax[index].get_legend_handles_labels()[0]
    labels = ax[index].get_legend_handles_labels()[1]
    ax[index].legend().remove()
    
     # Set the title
    ax[index].set_title(model_name, fontsize=14)
    
# Set the legend
figure.legend(handles, 
              labels, 
              loc='upper center', 
              bbox_to_anchor=(0.5, 1.03), 
              fontsize=8,
              ncol=2)

figure.suptitle('Learning Curves',
                fontweight='bold',
                fontsize=24)
    
plt.tight_layout()
```

# Residuals
``` python
# Define figure and axes
figure, ax = plt.subplots(1, 2, figsize=(12, 6))
ax = ax.flatten()

# Fetch all the trained models
for index, model_name in enumerate(models.keys()):
    
    # Compute the predictions for the test set
    predictions = models[model_name].predict(X_test)
    
    # Reshape predictions
    predictions = predictions.reshape(-1, 1)
    
    # Compute the residuals
    residuals = y_test - predictions
    
    # Create the Pandas DataFrame
    residuals_df = pd.DataFrame({'Residuals': residuals.to_numpy().reshape(-1,), 
                                 'Predictions': predictions.reshape(-1,)})
    
    # Plot the residuals
    sns.residplot(x='Predictions', 
                  y='Residuals',
                  data=residuals_df, 
                  ax=ax[index],
                  lowess=True)

     # Set the title
    ax[index].set_title(model_name, fontsize=14)

figure.suptitle('Feature Importance',
                fontweight='bold',
                fontsize=24)

plt.tight_layout()
```

# Q-Q Plot
``` python
# Define figure and axes
figure, ax = plt.subplots(1, 2, figsize=(12, 6))
ax = ax.flatten()

# Fetch all the trained models
for index, model_name in enumerate(models.keys()):
    
    # Compute the predictions for the test set
    predictions = models[model_name].predict(X_test)
    
    # Reshape predictions
    predictions = predictions.reshape(-1, 1)
    
    # Compute the residuals
    residuals = y_test - predictions
    
    # Generate a QQ plot
    stats.probplot(residuals.to_numpy().reshape(-1,), 
                   plot=ax[index])
    
    ax[index].set_xlabel('Theoretical Quantiles')

    # Set the title
    ax[index].set_title(model_name, fontsize=14)
    
    
figure.suptitle('Q-Q Plots',
                fontweight='bold',
                fontsize=24)

plt.tight_layout()
```
