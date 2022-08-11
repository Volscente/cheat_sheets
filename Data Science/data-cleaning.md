# Cleaning Outliers

## Interquartile Range (IQR)

``` python
# Define the list of columns for which compute the IQR
iqr_columns = ['Year_Birth', 
               'Income', 
               'MntWines', 
               'MntFruits', 
               'MntMeatProducts', 
               'MntFishProducts', 
               'MntSweetProducts', 
               'MntGoldProds', 
               'NumDealsPurchases', 
               'NumWebPurchases',
               'NumCatalogPurchases', 
               'NumWebVisitsMonth']

# Compute Q1 and Q3
q1 = data[iqr_columns].quantile(0.25)
q3 = data[iqr_columns].quantile(0.75)

# Compute the IQR
iqr = q3 - q1

# Compute the lower and upper filtering bounds
lower_filtering_bound = q1 - 1.5*iqr
upper_filtering_bound = q3 + 1.5*iqr

# Filter outliers
data_cleaned_outliers = data[~((data[iqr_columns] < lower_filtering_bound) |(data[iqr_columns] > upper_filtering_bound)).any(axis=1)].reset_index(drop=True)
```

# Fill NaN Values

## Drop Columns


## Imputation
Next, we use SimpleImputer to replace missing values with the mean value along each column.

Although it's simple, filling in the mean value generally performs quite well (but this varies by dataset).
While statisticians have experimented with more complex ways to determine imputed values (such as regression imputation,
for instance), the complex strategies typically give no additional benefit once you plug the results into sophisticated 
machine learning models.

Fit the imputer only on the training data.
``` python
from sklearn.impute import SimpleImputer

# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
```