# Hyperparameters Tuning
## GridSearch
``` python
# LightGBM hyperparameters
hyperparameters_lgb_gs = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'rmse'
}

# LightGBM hyperparameters space
hyperparameters_space_lgb_gs = {
    'lightgbm__num_leaves': np.arange(10, 60, 10),
    'lightgbm__learning_rate': np.linspace(0.001, 1, 5),
    'lightgbm__n_estimators': np.arange(50, 1000, 100)
}
%%time

# Start MLflow Run
with mlflow.start_run(experiment_id=mlflow_experiment_id, 
                      run_name='LightGBM with GridSearch'):

    # Define the model
    model_lgb_gs = lgb.LGBMRegressor(**hyperparameters_lgb_gs)

    # Define the pipeline
    pipe_lgb_gs = Pipeline([
        ('data_preprocessing', data_preprocessor),
        ('lightgbm', model_lgb_gs)
    ])
    
    # Define GridSearch
    # NOTE: GridSearchCV tries to maximise its score, that's why we need the Negative RMSE
    grid_search_lgb_gs = GridSearchCV(estimator=pipe_lgb_gs, 
                                      param_grid=hyperparameters_space_lgb_gs, 
                                      cv=3, 
                                      n_jobs=2, 
                                      scoring='neg_root_mean_squared_error', 
                                      verbose=3)

    # Search the best hyperparameters
    grid_search_lgb_gs.fit(X_train, 
                           np.ravel(y_train))

    # Retrieve the best model
    best_model_lgb_gs = grid_search_lgb_gs.best_estimator_
    
    # Retrieve best model's parameters
    best_parameters_lgb_gs = best_model_lgb_gs['lightgbm'].get_params()
    
    print("Model's Best Hyperparameters:")
    pprint.pprint(best_parameters_lgb_gs)
    print('\n')
    
    # Get predictions
    predictions_lgb_gs = best_model_lgb_gs.predict(X_test)

    # Compute metrics
    rmse_lgb_gs = round(mean_squared_error(y_test, predictions_lgb_gs), 2)
    
    # Log model's evaluation metrics
    mlflow.log_metrics({'RMSE': rmse_lgb_gs})
    
    # Log model's features
    mlflow.log_params({'Features': features, 'Hyperparameters': best_parameters_lgb_gs})

    print('RMSE: {}'.format(rmse_lgb_gs))
    print('\n')
    ```
