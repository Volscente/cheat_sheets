# TensorFlow WALS Matrix Factorization
## Read Data (Users for an Item)
```python
# Import Standard Libraries
import tensorflow as tf

# Define the grouping strategy
# NOTE: `mapped_df` is a dataframe in which User ID is mapped from [0, n_users] as well as Item ID
grouped_by_items = mapped_df.groupby("itemId")

# Open the file to write the data into
with tf.python_io.TFRecordWriter("data/users_for_item") as ofp:

  # Fetch each item in the group and create an example with the features
  for item, grouped in grouped_by_items:

    example = tf.train.Example(features = tf.train.Features(feature = {
        "key": tf.train.Feature(int64_list = tf.train.Int64List(value = [item])), # User ID
        "indices": tf.train.Feature(int64_list = tf.train.Int64List(value = grouped["userId"].values)),
        "values": tf.train.Feature(float_list = tf.train.FloatList(value = grouped["rating"].values))
    }))
    
    ofp.write(example.SerializeToString())
```

## Decode TF Record Files
```python
def decode_example(protos, vocab_size):

    # Specify the schema of the TF Record files
    # NOTE: Take as example the item to users
    features = {
        'key': tf.FixedLenFeature([1], tf.int64), # Item id
        'indices': tf.VarLenFeature(dtype=tf.int64) # Users
        'values': tf.VarLenFeature(dtype=tf.float32) # Ratings
    }

    # Parse one single item at a time
    parsed_features = tf.parse_single_example(protos, features)

    # Convert the indices and values into a sparse tensor
    values = tf.sparse_merge(
        parsed_features['indices'], 
        parsed_features['values'], 
        vocab_size=vocab_size
    )


```

## Create Sparse Tensors
```python
def parse_tfrecords(filename, vocab_size):

  # Create list of files
  files = tf.gfile.Glob(os.path.join(args['input_path'], filename))

  # Create a TFRecords Datraset
  dataset = tf.data.TFRecordDataset(files)

  # Decode and create the dataset
  dataset = dataset.map(lambda x: decode_example(x, vocab_size))
  dataset = dataset.repeat(num_epochs)
  dataset = dataset.batch(args['batch_size'])
  dataset = dataset.map(lambda x: remap_keys(x))
  
  return dataset.make_one_shot_iterator().get_next()

def _input_fn():
  features = {
    WALSMatrixFactorization.INPUT_ROWS: parse_tfrecords('items_for_user', args['nitems'])
    WALSMatrixFactorization.INPUT_COLS: parse_tfrecords('users_for_item', args['nusers'])
  }

  return features, None
```

## Train
```python
# Import Standard Libraries
import tensorflow as tf

tf.contrib.learn.Experiment(

  # Define the WASL Matrix Settings
  tf.contrib.factorization.WALSMatrixFactorization(
    num_rows=args['nusers'],
    num_cols=args['nitems'],
    embedding_dimension=args['n_embeds'],
    model_dir=args['output_dir']
  ),

  # Define train and test data
  train_input_fn=read_dataset(tf.estimator.ModeKeys.TRAIN, args),
  eval_input_fn=read_dataset(tf.estimator.ModeKeys.EVAL, args),

  # Define Training Parameters
  train_steps=10,
  eval_steps=1,
  min_eval_frequency_steps=steps_in_epoch,
  export_strategies=tf.contrib.learn.utils.saved_model_export_utils.make_export_strategy(
    serving_input_fn= create_serving_input_fn(args  )
  )
)
```