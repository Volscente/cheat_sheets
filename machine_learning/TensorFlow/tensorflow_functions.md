# Tensors
## Constant Tensor
``` python
# Create a Tensor from 0.0 to 9.0
X = tf.constant(range(10), dtype=tf.float32)
```
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
# Dataset API
## Create Dataset from Tensor
``` python
# Create a Tensor from 0.0 to 9.0
X = tf.constant(range(10), dtype=tf.float32)

# Create the Tensor Label with the formula 2x + 10
Y = 2 * X + 10

# Create the Dataset
dataset = tf.data.Dataset.from_tensor_slices((X, Y))

# Add 2 epochs of 3 batches each
batch_size = 3
epochs = 2
dataset = dataset.repeat(epochs).batch(batch_size, drop_remainder=True)
```
# Layers Preprocessing API
## TextVectorization
It transforms a batch of strings into an encoded representation that can be read by an Embedding or Dense layer.
``` python
tf.keras.layers.TextVectorization(
  max_tokens=None, # Maximum number of tokens to use
  standardize='lower_and_strip_punctation', # Standardization to apply: lowercase and remove punctation
  splti='whitespace', # How to strip tokens
  ngrams=None,
  output_mode='int',
  output_sequence-length=None,
  pad_to_max_tokens=False,
  vocabulary=None
)
```
If applied to a Dataset object, it can create a Vocabulary.
## Normalization
Normalize the given columns (axis=1) into a Normal Distribution.
``` python
tf.keras.layers.Normalization(
  axis=1,
  mean=None,
  variance=None
)
```
