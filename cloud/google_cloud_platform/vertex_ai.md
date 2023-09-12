# Jobs
## Custom Training
- Enable the Vertex AI API (*Enable All Recommended APIs*)
- Create a dataset in BigQuery
- Create and populate a table in BigQuery dataset
- Create an ML Dataset in Vertex AI
- Add the data to the ML Dataset in Vertex by connecting to BigQuery table
- Clicks on `Generate Statistics` to analyze the data (optional)
- Create a Workbench instance
- Inside the Jupyterlab instance. From the launcher create a new Terminal and run the following commands to create the project structure:
```bash
mkdir -p /home/jupyter/titanic/trainer
touch /home/jupyter/titanic/setup.py /home/jupyter/titanic/trainer/__init__.py /home/jupyter/titanic/trainer/task.py
```
- Populate the `task.py` file with the following code:

<br>

<details>
  <summary>Click me</summary>

```python
from google.cloud import bigquery, bigquery_storage, storage
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import classification_report, f1_score
from typing import Union, List
import os, logging, json, pickle, argparse
import dask.dataframe as dd
import pandas as pd
import numpy as np
# feature selection. The FEATURE list defines what features are needed from the training data
# as well as the types of those features. We will perform different feature engineering depending on the type.
# List all column names for binary features: 0,1 or True,False or Male,Female etc
BINARY_FEATURES = [
    'sex']
# List all column names for numeric features
NUMERIC_FEATURES = [
    'age',
    'fare']
# List all column names for categorical features
CATEGORICAL_FEATURES = [
    'pclass',
    'embarked',
    'home_dest',
    'parch',
    'sibsp']
ALL_COLUMNS = BINARY_FEATURES+NUMERIC_FEATURES+CATEGORICAL_FEATURES
# define the column name for label
LABEL = 'survived'
# Define the index position of each feature. This is needed for processing a
# numpy array (instead of pandas) which has no column names.
BINARY_FEATURES_IDX = list(range(0,len(BINARY_FEATURES)))
NUMERIC_FEATURES_IDX = list(range(len(BINARY_FEATURES), len(BINARY_FEATURES)+len(NUMERIC_FEATURES)))
CATEGORICAL_FEATURES_IDX = list(range(len(BINARY_FEATURES+NUMERIC_FEATURES), len(ALL_COLUMNS)))
def load_data_from_gcs(data_gcs_path: str) -> pd.DataFrame:
    '''
    Loads data from Google Cloud Storage (GCS) to a dataframe
            Parameters:
                    data_gcs_path (str): gs path for the location of the data. Wildcards are also supported. i.e gs://example_bucket/data/training-*.csv
            Returns:
                    pandas.DataFrame: a dataframe with the data from GCP loaded
    '''
    # using dask that supports wildcards to read multiple files. Then with dd.read_csv().compute we create a pandas dataframe
    # Additionally I have noticed that some values for TotalCharges are missing and this creates confusion regarding TotalCharges as the data type.
    # to overcome this we manually define TotalCharges as object.
    # We will later fix this abnormality
    logging.info("reading gs data: {}".format(data_gcs_path))
    return dd.read_csv(data_gcs_path, dtype={'TotalCharges': 'object'}).compute()
def load_data_from_bq(bq_uri: str) -> pd.DataFrame:
    '''
    Loads data from BigQuery table (BQ) to a dataframe
            Parameters:
                    bq_uri (str): bq table uri. i.e: example_project.example_dataset.example_table
            Returns:
                    pandas.DataFrame: a dataframe with the data from GCP loaded
    '''
    if not bq_uri.startswith('bq://'):
        raise Exception("uri is not a BQ uri. It should be bq://project_id.dataset.table")
    logging.info("reading bq data: {}".format(bq_uri))
    project,dataset,table =  bq_uri.split(".")
    bqclient = bigquery.Client(project=project[5:])
    bqstorageclient = bigquery_storage.BigQueryReadClient()
    query_string = """
    SELECT * from {ds}.{tbl}
    """.format(ds=dataset, tbl=table)
    return (
        bqclient.query(query_string)
        .result()
        .to_dataframe(bqstorage_client=bqstorageclient)
    )
def clean_missing_numerics(df: pd.DataFrame, numeric_columns):
    '''
    removes invalid values in the numeric columns        
            Parameters:
                    df (pandas.DataFrame): The Pandas Dataframe to alter
                    numeric_columns (List[str]): List of column names that are numeric from the DataFrame
            Returns:
                    pandas.DataFrame: a dataframe with the numeric columns fixed
    '''
    for n in numeric_columns:
        df[n] = pd.to_numeric(df[n], errors='coerce')
    df = df.fillna(df.mean())
    return df
def data_selection(df: pd.DataFrame, selected_columns: List[str], label_column: str) -> (pd.DataFrame, pd.Series):
    '''
    From a dataframe it creates a new dataframe with only selected columns and returns it.
    Additionally it splits the label column into a pandas Series.
            Parameters:
                    df (pandas.DataFrame): The Pandas Dataframe to drop columns and extract label
                    selected_columns (List[str]): List of strings with the selected columns. i,e ['col_1', 'col_2', ..., 'col_n' ]
                    label_column (str): The name of the label column
            Returns:
                    tuple(pandas.DataFrame, pandas.Series): Tuble with the new pandas DataFrame containing only selected columns and lablel pandas Series
    '''
    # We create a series with the prediciton label
    labels = df[label_column].astype(int)
    data = df.loc[:, selected_columns]
    return data, labels
def pipeline_builder(params_svm: dict, bin_ftr_idx: List[int], num_ftr_idx: List[int], cat_ftr_idx: List[int]) -> Pipeline:
    '''
    Builds a sklearn pipeline with preprocessing and model configuration.
    Preprocessing steps are:
        * OrdinalEncoder - used for binary features
        * StandardScaler - used for numerical features
        * OneHotEncoder - used for categorical features
    Model used is SVC
            Parameters:
                    params_svm (dict): List of parameters for the sklearn.svm.SVC classifier
                    bin_ftr_idx (List[str]): List of ints that mark the column indexes with binary columns. i.e [0, 2, ... , X ]
                    num_ftr_idx (List[str]): List of ints that mark the column indexes with numerical columns. i.e [6, 3, ... , X ]
                    cat_ftr_idx (List[str]): List of ints that mark the column indexes with categorical columns. i.e [5, 10, ... , X ]
                    label_column (str): The name of the label column
            Returns:
                     Pipeline: sklearn.pipelines.Pipeline with preprocessing and model training
    '''
    # Defining a preprocessing step for our pipeline.
    # it specifies how the features are going to be transformed
    preprocessor = ColumnTransformer(
        transformers=[
            ('bin', OrdinalEncoder(), bin_ftr_idx),
            ('num', StandardScaler(), num_ftr_idx),
            ('cat', OneHotEncoder(handle_unknown='ignore'), cat_ftr_idx)], n_jobs=-1)
    # We now create a full pipeline, for preprocessing and training.
    # for training we selected a linear SVM classifier
    clf = SVC()
    clf.set_params(**params_svm)
    return Pipeline(steps=[ ('preprocessor', preprocessor),
                          ('classifier', clf)])
def train_pipeline(clf: Pipeline, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.DataFrame, np.ndarray]) -> float:
    '''
    Trains a sklearn pipeline by fiting training data and labels and returns the accuracy f1 score
            Parameters:
                    clf (sklearn.pipelines.Pipeline): the Pipeline object to fit the data
                    X: (pd.DataFrame OR np.ndarray): Training vectors of shape n_samples x n_features, where n_samples is the number of samples and n_features is the number of features.
                    y: (pd.DataFrame OR np.ndarray): Labels of shape n_samples. Order should mathc Training Vectors X
            Returns:
                    score (float): Average F1 score from all cross validations
    '''
    # run cross validation to get training score. we can use this score to optimize training
    score = cross_val_score(clf, X, y, cv=10, n_jobs=-1).mean()
    # Now we fit all our data to the classifier.
    clf.fit(X, y)
    return score
def process_gcs_uri(uri: str) -> (str, str, str, str):
    '''
    Receives a Google Cloud Storage (GCS) uri and breaks it down to the scheme, bucket, path and file
            Parameters:
                    uri (str): GCS uri
            Returns:
                    scheme (str): uri scheme
                    bucket (str): uri bucket
                    path (str): uri path
                    file (str): uri file
    '''
    url_arr = uri.split("/")
    if "." not in url_arr[-1]:
        file = ""
    else:
        file = url_arr.pop()
    scheme = url_arr[0]
    bucket = url_arr[2]
    path = "/".join(url_arr[3:])
    path = path[:-1] if path.endswith("/") else path
    return scheme, bucket, path, file
def pipeline_export_gcs(fitted_pipeline: Pipeline, model_dir: str) -> str:
    '''
    Exports trained pipeline to GCS
            Parameters:
                    fitted_pipeline (sklearn.pipelines.Pipeline): the Pipeline object with data already fitted (trained pipeline object)
                    model_dir (str): GCS path to store the trained pipeline. i.e gs://example_bucket/training-job
            Returns:
                    export_path (str): Model GCS location
    '''
    scheme, bucket, path, file = process_gcs_uri(model_dir)
    if scheme != "gs:":
            raise ValueError("URI scheme must be gs")
    # Upload the model to GCS
    b = storage.Client().bucket(bucket)
    export_path = os.path.join(path, 'model.pkl')
    blob = b.blob(export_path)
    blob.upload_from_string(pickle.dumps(fitted_pipeline))
    return scheme + "//" + os.path.join(bucket, export_path)
def prepare_report(cv_score: float, model_params: dict, classification_report: str, columns: List[str], example_data: np.ndarray) -> str:
    '''
    Prepares a training report in Text
            Parameters:
                    cv_score (float): score of the training job during cross validation of training data
                    model_params (dict): dictonary containing the parameters the model was trained with
                    classification_report (str): Model classification report with test data
                    columns (List[str]): List of columns that where used in training.
                    example_data (np.array): Sample of data (2-3 rows are enough). This is used to include what the prediciton payload should look like for the model
            Returns:
                    report (str): Full report in text
    '''
    buffer_example_data = '['
    for r in example_data:
        buffer_example_data+='['
        for c in r:
            if(isinstance(c,str)):
                buffer_example_data+="'"+c+"', "
            else:
                buffer_example_data+=str(c)+", "
        buffer_example_data= buffer_example_data[:-2]+"], \n"
    buffer_example_data= buffer_example_data[:-3]+"]"
    report = """
Training Job Report    
Cross Validation Score: {cv_score}
Training Model Parameters: {model_params}
Test Data Classification Report:
{classification_report}
Example of data array for prediciton:
Order of columns:
{columns}
Example for clf.predict()
{predict_example}
Example of GCP API request body:
{{
    "instances": {json_example}
}}
""".format(
    cv_score=cv_score,
    model_params=json.dumps(model_params),
    classification_report=classification_report,
    columns = columns,
    predict_example = buffer_example_data,
    json_example = json.dumps(example_data.tolist()))
    return report
def report_export_gcs(report: str, report_dir: str) -> None:
    '''
    Exports training job report to GCS
            Parameters:
                    report (str): Full report in text to sent to GCS
                    report_dir (str): GCS path to store the report model. i.e gs://example_bucket/training-job
            Returns:
                    export_path (str): Report GCS location
    '''
    scheme, bucket, path, file = process_gcs_uri(report_dir)
    if scheme != "gs:":
            raise ValueError("URI scheme must be gs")
    # Upload the model to GCS
    b = storage.Client().bucket(bucket)
    export_path = os.path.join(path, 'report.txt')
    blob = b.blob(export_path)
    blob.upload_from_string(report)
    return scheme + "//" + os.path.join(bucket, export_path)
# Define all the command-line arguments your model can accept for training
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Input Arguments
    parser.add_argument(
        '--model_param_kernel',
        help = 'SVC model parameter- kernel',
        choices=['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'],
        type = str,
        default = 'linear'
    )
    parser.add_argument(
        '--model_param_degree',
        help = 'SVC model parameter- Degree. Only applies for poly kernel',
        type = int,
        default = 3
    )
    parser.add_argument(
        '--model_param_C',
        help = 'SVC model parameter- C (regularization)',
        type = float,
        default = 1.0
    )
    parser.add_argument(
        '--model_param_probability',
        help = 'Whether to enable probability estimates',
        type = bool,
        default = True
    )
    '''
    Vertex AI automatically populates a set of environment variables in the container that executes
    your training job. Those variables include:
        * AIP_MODEL_DIR - Directory selected as model dir
        * AIP_DATA_FORMAT - Type of dataset selected for training (can be csv or bigquery)
    Vertex AI will automatically split selected dataset into training, validation and testing
    and 3 more environment variables will reflect the location of the data:
        * AIP_TRAINING_DATA_URI - URI of Training data
        * AIP_VALIDATION_DATA_URI - URI of Validation data
        * AIP_TEST_DATA_URI - URI of Test data
    Notice that those environment variables are default. If the user provides a value using CLI argument,
    the environment variable will be ignored. If the user does not provide anything as CLI argument
    the program will try and use the environment variables if those exist. Otherwise will leave empty.
    '''   
    parser.add_argument(
        '--model_dir',
        help = 'Directory to output model and artifacts',
        type = str,
        default = os.environ['AIP_MODEL_DIR'] if 'AIP_MODEL_DIR' in os.environ else ""
    )
    parser.add_argument(
        '--data_format',
        choices=['csv', 'bigquery'],
        help = 'format of data uri csv for gs:// paths and bigquery for project.dataset.table formats',
        type = str,
        default =  os.environ['AIP_DATA_FORMAT'] if 'AIP_DATA_FORMAT' in os.environ else "csv"
    )
    parser.add_argument(
        '--training_data_uri',
        help = 'location of training data in either gs:// uri or bigquery uri',
        type = str,
        default =  os.environ['AIP_TRAINING_DATA_URI'] if 'AIP_TRAINING_DATA_URI' in os.environ else ""
    )
    parser.add_argument(
        '--validation_data_uri',
        help = 'location of validation data in either gs:// uri or bigquery uri',
        type = str,
        default =  os.environ['AIP_VALIDATION_DATA_URI'] if 'AIP_VALIDATION_DATA_URI' in os.environ else ""
    )
    parser.add_argument(
        '--test_data_uri',
        help = 'location of test data in either gs:// uri or bigquery uri',
        type = str,
        default =  os.environ['AIP_TEST_DATA_URI'] if 'AIP_TEST_DATA_URI' in os.environ else ""
    )
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
    args = parser.parse_args()
    arguments = args.__dict__
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    logging.info('Model artifacts will be exported here: {}'.format(arguments['model_dir']))
    logging.info('Data format: {}'.format(arguments["data_format"]))
    logging.info('Training data uri: {}'.format(arguments['training_data_uri']) )
    logging.info('Validation data uri: {}'.format(arguments['validation_data_uri']))
    logging.info('Test data uri: {}'.format(arguments['test_data_uri']))
    '''
    We have 2 different ways to load our data to pandas. One is from Cloud Storage by loading csv files and
    the other is by connecting to BigQuery. Vertex AI supports both and
    here we created a code that depending on the dataset provided. We will select the appropriate loading method.
    '''
    logging.info('Loading {} data'.format(arguments["data_format"]))
    if(arguments['data_format']=='csv'):
        df_train = load_data_from_gcs(arguments['training_data_uri'])
        df_test = load_data_from_bq(arguments['test_data_uri'])
        df_valid = load_data_from_gcs(arguments['validation_data_uri'])
    elif(arguments['data_format']=='bigquery'):
        print(arguments['training_data_uri'])
        df_train = load_data_from_bq(arguments['training_data_uri'])
        df_test = load_data_from_bq(arguments['test_data_uri'])
        df_valid = load_data_from_bq(arguments['validation_data_uri'])
    else:
        raise ValueError("Invalid data type ")
    #as we will be using cross validation, we will have just a training set and a single test set.
    # we will merge the test and validation to achieve an 80%-20% split
    df_test = pd.concat([df_test,df_valid])
    logging.info('Defining model parameters')    
    model_params = dict()
    model_params['kernel'] = arguments['model_param_kernel']
    model_params['degree'] = arguments['model_param_degree']
    model_params['C'] = arguments['model_param_C']
    model_params['probability'] = arguments['model_param_probability']
    df_train = clean_missing_numerics(df_train, NUMERIC_FEATURES)
    df_test = clean_missing_numerics(df_test, NUMERIC_FEATURES)
    logging.info('Running feature selection')    
    X_train, y_train = data_selection(df_train, ALL_COLUMNS, LABEL)
    X_test, y_test = data_selection(df_test, ALL_COLUMNS, LABEL)
    logging.info('Training pipelines in CV')   
    y_train = y_train.astype('int')
    y_test = y_test.astype('int')
    clf = pipeline_builder(model_params, BINARY_FEATURES_IDX, NUMERIC_FEATURES_IDX, CATEGORICAL_FEATURES_IDX)
    cv_score = train_pipeline(clf, X_train, y_train)
    logging.info('Export trained pipeline and report')   
    pipeline_export_gcs(clf, arguments['model_dir'])
    y_pred = clf.predict(X_test)
    test_score = f1_score(y_test, y_pred, average='weighted')
    logging.info('f1score: '+ str(test_score))    
    report = prepare_report(cv_score,
                        model_params,
                        classification_report(y_test,y_pred),
                        ALL_COLUMNS,
                        X_test.to_numpy()[0:2])
    report_export_gcs(report, arguments['model_dir'])
    logging.info('Training job completed. Exiting...')
```

</details>

<br>

- Copy the following code to `setup.py`:
```python
from setuptools import find_packages
from setuptools import setup
REQUIRED_PACKAGES = [
    'gcsfs==0.7.1',
    'dask[dataframe]==2021.2.0',
    'google-cloud-bigquery-storage==1.0.0',
    'six==1.15.0'
]
setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(), # Automatically find packages within this directory or below.
    include_package_data=True, # if packages include any data files, those will be packed together.
    description='Classification training titanic survivors prediction model'
)
```
- Define the following variables:
```bash
export REGION="europe-west4"
export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
export BUCKET_NAME=$PROJECT_ID"-bucket"
```
- Create a bucket where to export the trained model:
```bash
gsutil mb -l $REGION "gs://"$BUCKET_NAME
```
- Install the required packages:
```bash
cd /home/jupyter/titanic
pip install setuptools
python setup.py install
```
- Verify that the training code works:
```bash
python -m trainer.task -v \
    --model_param_kernel=linear \
    --model_dir="gs://"$BUCKET_NAME"/titanic/trial" \
    --data_format=bigquery \
    --training_data_uri="bq://"$PROJECT_ID".titanic.survivors" \
    --test_data_uri="bq://"$PROJECT_ID".titanic.survivors" \
    --validation_data_uri="bq://"$PROJECT_ID".titanic.survivors"
```
- Create the Python package
```bash
cd /home/jupyter/titanic
python setup.py sdist
```
- Copy the created package to the bucket:
```bash
gsutil cp dist/trainer-0.1.tar.gz "gs://"$BUCKET_NAME"/titanic/dist/trainer-0.1.tar.gz"
```
- Create a Vertex AI Training by selecting the `Training` tab and then `Create`:
    - `Dataset` is the ML dataset
    - `Objective` is classificaiont
    - `Custom Training`
- Define Training environment
    - Pre-built container
    - Model framework: Scikit-learn
    - Model framework version: 0.23
    - Package location: gs://YOUR-BUCKET-NAME/titanic/dist/trainer-0.1.tar.gz
    - Python module: trainer.task
    - BigQuery project for exporting data: YOUR-PROJECT-ID

## Hyperparameters Tuning
- Enable the Vertex AI API (*Enable All Recommended APIs*)
- Create a Notebook
- Create folder structure:
```bash
mkdir horses_or_humans
cd horses_or_humans
```
- Create Dockerfile
```bash
touch Dockerfile
```
- Copy the following code to `Dockerfile`:
```dockerfile
FROM gcr.io/deeplearning-platform-release/tf2-gpu.2-9
WORKDIR /
# Installs hypertune library
RUN pip install cloudml-hypertune
# Copies the trainer code to the docker image.
COPY trainer /trainer
# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "-m", "trainer.task"]
```
- Define the model training code:
```bash
mkdir trainer
touch trainer/task.py
```
- Copy the following code to `trainer/task.py`:

<br>

<details>
  <summary>Click me</summary>

```python
import tensorflow as tf
import tensorflow_datasets as tfds
import argparse
import hypertune
NUM_EPOCHS = 10
def get_args():
  '''Parses args. Must include all hyperparameters you want to tune.'''
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--learning_rate',
      required=True,
      type=float,
      help='learning rate')
  parser.add_argument(
      '--momentum',
      required=True,
      type=float,
      help='SGD momentum value')
  parser.add_argument(
      '--num_neurons',
      required=True,
      type=int,
      help='number of units in last hidden layer')
  args = parser.parse_args()
  return args
def preprocess_data(image, label):
  '''Resizes and scales images.'''
  image = tf.image.resize(image, (150,150))
  return tf.cast(image, tf.float32) / 255., label
def create_dataset():
  '''Loads Horses Or Humans dataset and preprocesses data.'''
  data, info = tfds.load(name='horses_or_humans', as_supervised=True, with_info=True)
  # Create train dataset
  train_data = data['train'].map(preprocess_data)
  train_data  = train_data.shuffle(1000)
  train_data  = train_data.batch(64)
  # Create validation dataset
  validation_data = data['test'].map(preprocess_data)
  validation_data  = validation_data.batch(64)
  return train_data, validation_data
def create_model(num_neurons, learning_rate, momentum):
  '''Defines and complies model.'''
  inputs = tf.keras.Input(shape=(150, 150, 3))
  x = tf.keras.layers.Conv2D(16, (3, 3), activation='relu')(inputs)
  x = tf.keras.layers.MaxPooling2D((2, 2))(x)
  x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(x)
  x = tf.keras.layers.MaxPooling2D((2, 2))(x)
  x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
  x = tf.keras.layers.MaxPooling2D((2, 2))(x)
  x = tf.keras.layers.Flatten()(x)
  x = tf.keras.layers.Dense(num_neurons, activation='relu')(x)
  outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
  model = tf.keras.Model(inputs, outputs)
  model.compile(
      loss='binary_crossentropy',
      optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate, momentum=momentum),
      metrics=['accuracy'])
  return model
def main():
  args = get_args()
  train_data, validation_data = create_dataset()
  model = create_model(args.num_neurons, args.learning_rate, args.momentum)
  history = model.fit(train_data, epochs=NUM_EPOCHS, validation_data=validation_data)
  # DEFINE METRIC
  hp_metric = history.history['val_accuracy'][-1]
  hpt = hypertune.HyperTune()
  hpt.report_hyperparameter_tuning_metric(
      hyperparameter_metric_tag='accuracy',
      metric_value=hp_metric,
      global_step=NUM_EPOCHS)
if __name__ == "__main__":
    main()
```

</details>

<br>

- Define the following variables:
```bash
PROJECT_ID='qwiklabs-gcp-01-f3f530bf53ff'
IMAGE_URI="gcr.io/$PROJECT_ID/horse-human:hypertune"
```
- Build the Docker image:
```bash
docker build ./ -t $IMAGE_URI
```
- Push the Docker image to Container Registry:
```bash
docker push $IMAGE_URI
```
- Go to the `Training`section in Vertex AI
- Leave `Dataset` as `No managed dataset`
- Select `Custom Training`
- In `Training container` select `Custom container` and select the `Container image URI` you just created from the `Container Registry`
- Configure the hyperparameters as the parameters you defined in the `get_args()` function:
    - `learning_rate` (log scaling)
    - `momentum`
    - `num_neurons`
- Continue to configure and then start training

## Hyperparameters Tuning with Vertex Vizier
It is a multi-objective optimization algorithm. In the following code we want to minimise `y1=r*sin(theta)` and maximise `y2=r*cos(theta)`.

<details>
  <summary>Click me</summary>

```python
# Parameter configuration
param_r = {
    "parameter_id": "r", 
    "double_value_spec": {
        "min_value": 0, 
        "max_value": 1
    }
}

param_theta = {
    "parameter_id": "theta",
    "double_value_spec": {
        "min_value": 0, 
        "max_value": 1.57
    }
}

# Define the metrics y1 and y2
metric_y1 = {
    "metric_id": "y1", 
    "goal": "MINIMIZE"
}

metric_y2 = {
    "metric_id": "y2", 
    "goal": "MAXIMIZE"
}

# Put all the parameters and metrics together in a Study Configuration
study = {
    "display_name": 'STUDY_DISPLAY_NAME',
    "study_spec": {
        "algorithm": "RANDOM_SEARCH",
        "parameters": [
            param_r,
            param_theta,
        ],
        "metrics": [
            metric_y1, 
            metric_y2],
    }
}

from google.cloud import aiplatform_v1beta1

REGION = "us-central1"
PROJECT_ID = "qwiklabs-gcp-00-866bdf7714fe"

# Create the study using study configuration and send request through VizierServiceClient
vizier_client = aiplatform_v1beta1.VizierServiceClient(
    client_options=dict(api_endpoint="{REGION}-aiplatform.googleapis.com")
)

study = vizier_client.create_study(
    parent="projects/{PROJECT_ID}/locations/{REGION}",
    study=study)

STUDY_ID = study.name

# Define how to compute metrics
import math

# r * sin(theta)
def Metric1Evaluation(r, theta):
    """Evaluate the first metric on the trial."""
    return r * math.sin(theta)

# r * cos(theta)
def Metric2Evaluation(r, theta):
    """Evaluate the second metric on the trial."""
    return r * math.cos(theta)

def CreateMetrics(trial_id, r, theta):
    print(("=========== Start Trial: [{}] =============").format(trial_id))

    # Evaluate both objective metrics for this trial
    y1 = Metric1Evaluation(r, theta)
    y2 = Metric2Evaluation(r, theta)
    print(
        "[r = {}, theta = {}] => y1 = r*sin(theta) = {}, y2 = r*cos(theta) = {}".format(
            r, theta, y1, y2
        )
    )
    metric1 = {"metric_id": "y1", "value": y1}
    metric2 = {"metric_id": "y2", "value": y2}

    # Return the results for this trial
    return [metric1, metric2]

# Define trial parameters
client_id = "client1"
suggestion_count_per_request = 5
max_trial_id_to_stop = 4

# Run the Trials
trial_id = 0
while int(trial_id) < max_trial_id_to_stop:

    # Get the trials
    suggest_response = vizier_client.suggest_trials(
        {
            "parent": STUDY_ID,
            "suggestion_count": suggestion_count_per_request,
            "client_id": client_id,
        }
    )

    # Evaluate the trials
    for suggested_trial in suggest_response.result().trials:

        trial_id = suggested_trial.name.split("/")[-1]
        trial = vizier_client.get_trial({"name": suggested_trial.name})

        if trial.state in ["COMPLETED", "INFEASIBLE"]:
            continue

        for param in trial.parameters:
            if param.parameter_id == "r":
                r = param.value
            elif param.parameter_id == "theta":
                theta = param.value
        print("Trial : r is {}, theta is {}.".format(r, theta))

        # Store your measurement and send the request
        vizier_client.add_trial_measurement(
            {
                "trial_name": suggested_trial.name,
                "measurement": {
                    # TODO
                    "metrics": CreateMetrics(suggested_trial.name, r, theta)
                },
            }
        )

        response = vizier_client.complete_trial(
            {"name": suggested_trial.name, "trial_infeasible": False}
        )

# List all the pareto-optimal trails
optimal_trials = vizier_client.list_optimal_trials({"parent": STUDY_ID})

print("optimal_trials: {}".format(optimal_trials))
```

</details>

<br>

# Pipeline
This chain of modular components covers all the steps of Machine Learning process, from data collection to model deployment. A Machine Learning Orchestrator is responsible for the execution of the pipeline. The Orchestrator is a service that schedules and runs the pipeline.

The Pipelines can be built either with TFX or Kubeflow SDK.

Usually the output model of a Vertex AI Pipeline is store in a Cloud Storage Bucket.

## Requirements
Activate the Cloud Shell and run the following commands:
```bash
gcloud services enable compute.googleapis.com         \
                       containerregistry.googleapis.com  \
                       aiplatform.googleapis.com  \
                       cloudbuild.googleapis.com \
                       cloudfunctions.googleapis.com
```

Install the following packages:
```bash
pip install kfp google-cloud-aiplatform google-cloud-pipeline-components
```

## Imports
```python
# Load necessary libraries
from typing import NamedTuple
import kfp
from kfp import dsl
from kfp.v2 import compiler
from kfp.v2.dsl import (Artifact, Dataset, Input, InputPath, Model, Output,
                        OutputPath, ClassificationMetrics, Metrics, component)
from kfp.v2.google.client import AIPlatformClient
from google.cloud import aiplatform
from google_cloud_pipeline_components import aiplatform as gcc_aip
```


## Sample components
```python
@component(base_image="python:3.9", output_component_file="first-component.yaml")
def product_name(text: str) -> str:
    return text
```
- base_image: container base image
- output_component_file: destination .yaml file of the compiled component

**NOTE:** Once the compiled component is saved in a .yaml file, it can be loaded through:
```python
product_name_component = kfp.components.load_component_from_file('./first-component.yaml')
```

Another example:
```python
@component(packages_to_install=["emoji"])
def emoji(
    text: str,
) -> NamedTuple(
    "Outputs",
    [
        ("emoji_text", str),  # Return parameters
        ("emoji", str),
    ],
):
    import emoji
    emoji_text = text
    emoji_str = emoji.emojize(':' + emoji_text + ':', use_aliases=True)
    print("output one: {}; output_two: {}".format(emoji_text, emoji_str))
```
- packages_to_install: it specifies the package dependencies


## Create Pipeline
Put all the components together into a Pipeline
```python
@dsl.pipeline(
    name="hello-world",
    description="An intro pipeline",
    pipeline_root=PIPELINE_ROOT,
)
# You can change the `text` and `emoji_str` parameters here to update the pipeline output
def intro_pipeline(text: str = "Vertex Pipelines", emoji_str: str = "sparkles"):
    product_task = product_name(text)
    emoji_task = emoji(emoji_str)
    consumer_task = build_sentence(
        product_task.output,
        emoji_task.outputs["emoji"],
        emoji_task.outputs["emoji_text"],
    )
```
- pipeline_root: Google Bucket where to save the compiled pipeline

## Compile Pipeline
```python
compiler.Compiler().compile(
    pipeline_func=intro_pipeline, package_path="intro_pipeline_job.json"
)
```
## Run Pipeline
```python
# Create API Client
api_client = AIPlatformClient(
    project_id=PROJECT_ID,
    region=REGION,
)

# Run pipeline
response = api_client.create_run_from_job_spec(
    job_spec_path="intro_pipeline_job.json"
)
```

## Best Practices
- **Assess Perfection** - Why did a pipeline produce an especially accurate model?
- **Compare Pipelines** - Which pipeline produced the most accurate model and parameters used?
- **System Governance** - Which version of the model is in production at a given time? (Use Pipeline Metadata).
- **Pipeline SDK** - Pipeline can orchestrate the ML Workflow in a Serveless Manner through Kubeflow SDK and TensorFlow Extended

**NOTE:** Components are chained with DSL (Domain-Specific Language) to create a Pipeline


# Model Deployment & Monitoring
## Deployment steps
- Define the machine type
- Define the model's input
- Automatic scaling
- Specify model performance (metrics) requirements and define when to re-train the model

## Monitoring Features (Best practices)
- **Skew detection** - It looks for the degree of distortion between your model training and production data. Use this as much as possible.
- **Data drift** - It looks for drift in production data
- **Alert thresholds** - Set a threshold for model's metrics
- **Model input** - Determine how to pass inputs to the model

**NOTE:** Model monitoring does not work with unstructured data