# Datetime

## Convert Column to Datetime
``` python
data['<new_column>'] = pd.to_datetime(data['<column>'], format='%d-%m-%Y')
```

## Extract day, month, year, day of the week and year_month information
``` python
# Compute the 'Year_month' column with the first day
train_data['date_day'] = train_data['date_datetime'].dt.day
train_data['date_month'] = train_data['date_datetime'].dt.month
train_data['date_year'] = train_data['date_datetime'].dt.year
train_data['date_dayofweek'] = train_data['date_datetime'].dt.dayofweek
train_data['date_year_month'] = pd.to_datetime(train_data['date_datetime']).dt.to_period('M')
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

# List Column

## Transform into a Series
``` python

# Transform a Pandas DataFrame list column to a series
def transform_list_column_to_series(series):
 return pd.Series([x for _list in series for x in _list])
 
# Apply the function
transform_list_column_to_series(data[“favorite_fruits”]).value_counts()

## OUTPUT ##
apple         5
blueberry     4
watermelon    4
strawberry    4
raspberry     3
pear          3
banana        2
pineapple     2
mango         2
peach         2
orange        2
maracuja      1
```

## Transform List Column into a DataFrame
``` python
fruits["favorite_fruits"].apply(pd.Series)
```