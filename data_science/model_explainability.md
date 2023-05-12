# Model Comparison
``` python
# Sort dataframe by the metric
performance.sort_values('RMSE', inplace=True)

# Create figure
figure = plt.figure(tight_layout=True, figsize=(9, 6))

# Plot models' metrics
ax = sns.barplot(data=performance, 
                 x=performance.index.tolist(), 
                 y='RMSE')

# Set title
ax.set_title('Models Comparison', 
             fontsize=24)

plt.xticks(rotation=45)

plt.show()
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
