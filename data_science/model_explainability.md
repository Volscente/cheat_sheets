# Feature Importance 
``` python
# Compute the feature importance
feature_importance = sorted(list(zip(pipe_xgb_cv_hp.feature_names_in_,
                                     pipe_xgb_cv_hp['xgb_classifier'].feature_importances_)),
                            key=lambda x: x[1], reverse=True)

# Transform it into a DataFrame
feature_importance_df = pd.DataFrame(feature_importance,
                                     columns= ['Feature', 'Importance'])

# Plot the feature importance
ax = sns.barplot(data=feature_importance_df, 
                 x='Feature', 
                 y='Importance')

# Set title
ax.set_title('Feature Importance', 
             fontsize=20, 
             fontweight='bold')

plt.xticks(fontsize=8, 
           rotation=45)

plt.show()
```

# Model Metric Comparison
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
