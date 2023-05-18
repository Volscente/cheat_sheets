# Create DataFrame
## Read Data from CSV
``` python
# Define local data file paths
data_file_path = Path(os.path.abspath('')).parents[0] / 'data' / 'data.csv'

# Read data
data = pd.read_csv(data_file_path, parse_dates=['date'], index_col=0)
```
# Options
## Set Pandas Options
``` python
# Set Pandas Options
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', None)
```

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

## Select Row & Columm by Index
``` python
data[<index_value>, '<column_name>']
```

## Filter by Largest value
``` python
# Retrieve top "n" rows filtered by the largest value in the columns 'column_1' and 'column_2'
data.nlargest(n, ['column_1', 'column_2'])
```

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

## Fetch Rows
``` python
for index, row in data.sample(10).iterrows():
    print(row['column_name'])
    print('\n')
```

## Condition on String Contain
``` python
# String Contains
mss_changes.loc[mss_changes['single_rejection_reason'].str.contains('menu_management_pandora'), 'main_rejection_reason'] = 1

# String NOT Contains
mss_changes.drop(mss_changes[~mss_changes['single_rejection_reason'].str.contains('menu_management_pandora')], inplace=True)
```

## Drop Rows based on a Condition
``` python
# Drop all the rows in which the column does not contain the word
data.drop(data[~data['<column_namw>'].str.contains('<word>')], inplace=True)
```

## Map Column Values
``` python
# Define mapping dictionary
dictionary = {
  'A': 'a', 
  'B': 'b'
}

# Map values in the column '<column_name>' based on '<dictionary>'
data['<column_name>'] = data['<column_name>'].map(dictionary)
```

## Map Column Values by Substring
``` python
# Define mapping dictionary
dictionary = {
  'dog': 'Animal Topic', 
  'cat': 'Animal Topic'
}

# Map values in the column '<column_name>' based on '<dictionary>'
for key in dictionary.keys():

    # Use the 'key' of the dictionary as a substring to identify the corresponding category to map
    data.loc[data['<column_name>'].str.contains(key), '<mapping_column_name>'] = dictionary[key]
```

## Numpy Select - Fill a Column based on Multiple Conditions
``` python
import numpy as np

# Define the conditions for the `HouseAgeClass` categories
house_age_class_conditions = {
    'young': california_housing_train['HouseAge'] <= 17,
    'middle': (california_housing_train['HouseAge'] > 17) &  (california_housing_train['HouseAge'] < 52),
    'old': california_housing_train['HouseAge'] == 52
}

# Define a categorical variable called `HouseAgeClass`
california_housing_train['HouseAgeClass'] = np.select(house_age_class_conditions.values(), 
                                                      house_age_class_conditions.keys())
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

# Pandas GBQ

## Read Data through Query
``` python
# Import Standard Libraries
import pandas_gbq

# Read vp_users SQL Query
with open(query_path) as file:
    query = file.read()
    
# Read Data
data = pandas_gbq.read_gbq(query,
                           project_id=project_id)
```

# Where Function

## Fill Column based on Condition
``` python
data['endofmonth'] = np.where((data['day'] >= 27) & (data['day'] <= 31), 1, 0)
```

# Convert to Other Dtypes

## Convert Two Columns into a Dictionary
``` python
dict(zip(df.column_1, df.column_2))
```

# Common Errors

## SettingWithCopyWarning
The error is due to the fact that Pandas is not able to distinguish whenever you're using the original DataFrame or a view.
It can be easily solved by passing a copy of the original DataFrame and not directly the original.

# MultiIndex
## Select Index Level
``` python
# Retrieve first level of a multi-index DataFrame
data.index.get_level_values(0)
```
