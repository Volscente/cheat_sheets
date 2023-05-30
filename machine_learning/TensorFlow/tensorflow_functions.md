# Features
## Define Feature Types
``` python
# Specify the type of two columns 'square_footage' and 'house_type'
features_columns = [
  tf.feature_column.numeric_column('square_footage'),
  tf.feature_column.categorical_column_with_vocabulary_list('house_type', ['house', 'apartment'])
]
```
