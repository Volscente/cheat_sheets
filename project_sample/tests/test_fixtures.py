"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest
from google.cloud import bigquery

# Import Package Modules
from src.general_utils.general_utils import read_configuration

# Read configuration file
configuration = read_configuration(pathlib.Path(__file__).parents[1]
                                   / 'configuration'
                                   / 'config.yaml')


@pytest.fixture
def fixture_bigquery_client(project_id: str = configuration['bigquery_project_id']) \
        -> bigquery.Client:
    """
    Fixture for a Google BigQuery client

    Args:
        project_id: str Google project ID

    Returns:
        bigquery_client: bigquery.Client object
    """
    # Initialise the BigQuery client
    bigquery_client = bigquery.Client(project=project_id)

    return bigquery_client


@pytest.fixture
def fixture_dictionary_query_parameters(
        test_dictionary_query_parameters: dict = configuration['test_dictionary_query_parameters']
) -> dict:
    """
    Fixture for a Dictionary Query Parameter with structure:
        name: <name_of_the_query_parameter>
        array_type: <type_of_the_parameter>
        value: <value_of_the_parameter>

    Args:
        test_dictionary_query_parameters: dict query parameters

    Returns:
        test_dictionary_query_parameter: dict query parameter
    """

    return test_dictionary_query_parameters


@pytest.fixture
def fixture_bigquery_parameters(
        dictionary_query_parameters: dict = configuration['test_dictionary_query_parameters']
) -> bigquery.ArrayQueryParameter:
    """
    Fixture for a BigQuery Query Parameter

    Args:
        dictionary_query_parameters: dict dictionary of query parameters

    Returns:
        bigquery_parameter: bigquery.ArrayQueryParameter BigQuery built query parameter
    """

    # Retrieve query parameters
    query_parameters = dictionary_query_parameters['query_parameters']

    # Retrieve parameter's variables
    parameter_name = query_parameters['test_parameter']['name']
    parameter_array_type = query_parameters['test_parameter']['type']
    parameter_value = query_parameters['test_parameter']['value']

    # Build the BigQuery query parameters
    bigquery_parameter = bigquery.ScalarQueryParameter(parameter_name,
                                                       parameter_array_type,
                                                       parameter_value)

    return bigquery_parameter
