"""
This test module includes all the tests for the
module src.general_utils.general_utils
"""
# Import Standard Modules
import pathlib
import pytest
from google.cloud import bigquery

# Import Package Modules
from src.general_utils.general_utils import (
    read_configuration,
    read_file_from_path,
    read_bq_from_query,
    build_path_from_list,
    build_bigquery_query_parameters_from_dictionary
)
from tests.test_fixtures import (
    fixture_bigquery_client,
    fixture_dictionary_query_parameters,
    fixture_bigquery_parameters
)


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    (pathlib.Path(__file__).parents[1]
         / 'configuration'
         / 'config.yaml',
         'test_value',
     1),
])
def test_read_configuration(test_config_file: pathlib.Path,
                            test_config: str,
                            expected_value: int) -> bool:
    """
    Test the function src.general_utils.general_utils.read_configuration
    by reading test configuration entries

    Args:
        pathlib.Path: Configuration file path
        test_config: String configuration entry key
        expected_value: String configuration expected value

    Returns:
    """

    # Read configuration file
    config = read_configuration(test_config_file)

    assert config[test_config] == expected_value


@pytest.mark.parametrize('test_config_file, expected_error', [
    (pathlib.Path(__file__).parents[1]
         / 'configuration'
         / 'wrong_config.yaml',
     FileNotFoundError)
])
def test_read_configuration_exceptions(test_config_file: pathlib.Path,
                                       expected_error: FileNotFoundError) -> bool:
    """
    Test the exceptions to the function
    src.general_utils.general_utils.read_configuration

    Args:
        test_config_file: Wrong configuration file path
        expected_error: Exception instance

    Returns:
    """

    with pytest.raises(expected_error):
        read_configuration(test_config_file)


@pytest.mark.parametrize('input_path, expected_first_line', [
    (pathlib.Path(__file__).parents[1] /
         'queries' /
         'test_queries' /
         'test_access_bigquery_query.sql',
     '-- Query for testing purposes')
])
def test_read_file_from_path(input_path: pathlib.Path,
                             expected_first_line: str) -> bool:
    """
    Test the function src.general_utils.general_utils.read_file_from_path
    by reading a local file and compare the first line

    Args:
        input_path: pathlib.Path local file path
        expected_first_line: str of file first line

    Returns:
    """

    # Read the file
    file_read = read_file_from_path(input_path)

    assert file_read.partition('\n')[0] == expected_first_line


@pytest.mark.parametrize('input_path, expected_exception', [
    (pathlib.Path(__file__).parents[2] /
         'queries' /
         'test_queries' /
         'wrong_file.sql',
     FileNotFoundError)
])
def test_read_file_from_path_exceptions(input_path: pathlib.Path,
                                        expected_exception: Exception) -> bool:
    """
    Test the exceptions to the function
    src.general_utils.general_utils.read_file_from_path

    Args:
        input_path: pathlib.Path wrong local file path
        expected_exception: Exception instance

    Returns:
    """

    with pytest.raises(expected_exception):
        read_file_from_path(input_path)


@pytest.mark.parametrize('input_id, expected_status', [
    (1, 'OK')
])
def test_read_bq_from_query(fixture_bigquery_client: bigquery.Client,
                            fixture_dictionary_query_parameters: dict,
                            input_id: int,
                            expected_status: str) -> bool:
    """
    Test the function src.general_utils.general_utils.read_bq_from_query
    by comparing the retrieved data column value with the expected output

    Args:
        fixture_bigquery_client: bigquery.Client instance
        fixture_dictionary_query_parameters: dict query parameters
        input_id: int row id value
        expected_status: str row 'status' expected value

    Returns:
    """

    # Retrieve data from BigQuery
    data = read_bq_from_query(fixture_bigquery_client,
                              fixture_dictionary_query_parameters)

    assert data.loc[data['id'] == input_id, 'status'].iloc[0] == expected_status


@pytest.mark.parametrize('path_list, expected_absolute_path', [
    (
            [
                'queries',
                'test_queries',
                'test_access_bigquery_query.sql'
            ],
            pathlib.Path(__file__).parents[1] /
            'queries' /
            'test_queries' /
            'test_access_bigquery_query.sql'
    )
])
def test_build_path_from_list(path_list: list,
                              expected_absolute_path: pathlib.Path) -> bool:
    """
    Test the function src.general_utils.general_utils.build_path_from_list
    by comparing built absolute path with the expected ome

    Args:
        path_list: list of relative path sub-folders
        expected_absolute_path: pathlib.Path expected built absolute path

    Returns:
    """

    # Build the absolute path
    absolute_path = build_path_from_list(path_list)

    assert absolute_path.resolve() == expected_absolute_path.resolve()


def test_build_bigquery_query_parameters_from_dictionary(
        fixture_dictionary_query_parameters: dict,
        fixture_bigquery_parameters: bigquery.ArrayQueryParameter
) -> bool:
    """
    Test the function
    src.general_utils.general_utils.build_bigquery_query_parameters_from_dictionary
    by comparing the values of the bigquery.ArrayQueryParameter with the original
    dictionary values

    Args:
        fixture_dictionary_query_parameters: dict query parameters
        fixture_bigquery_parameters: bigquery.ArrayQueryParameter BigQuery built query parameter

    Returns:
    """

    # Build the BigQuery query parameters from dictionary
    bigquery_parameter = build_bigquery_query_parameters_from_dictionary(
        fixture_dictionary_query_parameters['query_parameters']
    )[0]

    assert bigquery_parameter.name == fixture_bigquery_parameters.name \
           and bigquery_parameter.type_ == fixture_bigquery_parameters.type_ \
            and bigquery_parameter.value == fixture_bigquery_parameters.value
