# Datetime

## Convert Column to Datetime
``` python
data['<new_column>'] = pd.to_datetime(data['<column>'], format='%d-%m-%Y')
```

## Concatenate Year and Month
``` python
# Compute the 'Year_month' column with the first day
data['year_month'] = pd.to_datetime(data['<datatime_column>']).dt.to_period('M')
```

# Group By

## Range of Intervals
``` python
# Number of Intervals
n_intervals = 10

# Define the Year_Birth intervals
year_birth_intervals = pd.cut(data_cleaned_outliers['Year_Birth'],
                              np.linspace(data_cleaned_outliers['Year_Birth'].min(),
                                          data_cleaned_outliers['Year_Birth'].max(),
                                          n_intervals,
                                          dtype=np.int32))

# Fll NaN values in the Income with the mean of the group
data_filled['Income'] = data_cleaned_outliers.groupby([year_birth_intervals,
                                                       data_cleaned_outliers['Education'],
                                                       data_cleaned_outliers['Marital_Status']])['Income'].apply(lambda x: x.fillna(x.mean()))
```

## Top 10 Size Groups
``` python
data_grouped = data.groupby(['<column_name>']).size().to_frame().sort_values([0], ascending = False).head(10).reset_index()
```


# DataFrame

## Add Row from List
``` python
# Update 'performance' DataFrame
performance.loc['logistic_regression'] = [accuracy_lr, precision_lr, recall_lr, f1_lr]
```

## Strip Column Names
``` python
# Remove spaces from column names
data.columns = data.columns.str.strip()
```

## NaN Values
``` python
# Number of missing values in each column of data
missing_val_count_by_column = (data.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])
```

## Count Duplicates
``` python
data[data['<column_name>'].duplicated()]
```
