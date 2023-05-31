# Features
## Define Feature Types
``` python
# Specify the type of two columns 'square_footage' and 'house_type'
features_columns = [
  tf.feature_column.numeric_column('square_footage'),
  tf.feature_column.categorical_column_with_vocabulary_list('house_type', ['house', 'apartment'])
]
```
## Feature Crosses
``` python
# Specify the type of two columns 'square_footage' and 'house_type'
crossed_ploc = tf.feature_column.crossed_column([fc_bucketized_plat, fc_bucketized_plon], hash_bucket_size=NBUCKETS * NBUCKETS)
```
