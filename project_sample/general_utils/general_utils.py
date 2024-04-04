"""
The module contains several general util functions with no
specific technology or SDK binding (e.g., Google SDK)
"""
# Import Standard Libraries
import os
import pathlib
import yaml
from google.cloud import bigquery
import pandas as pd


# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def read_configuration(config_file_path: pathlib.Path) -> dict:
    """
    Read and return the specified configuration file from the 'configuration' folder

    Args:
        config_file_path: pathlib.Path configuration file path to read

    Returns:
        configuration: Dictionary configuration
    """

    logger.info('read_configuration - Start')

    logger.info('read_configuration - Reading %s', config_file_path.as_posix())

    if config_file_path.exists():

        # Read configuration file
        with open(config_file_path, encoding='utf-8') as config_file:

            configuration = yaml.safe_load(config_file.read())

    else:

        raise FileNotFoundError(f'read_data - File {config_file_path.as_posix()} not found')

    logger.info('read_configuration - Successfully configuration file read from %s',
                config_file_path.as_posix())

    logger.info('read_configuration - End')

    return configuration


def read_file_from_path(file_path: pathlib.Path) -> str:
    """
    Read a file from local path

    Args:
        file_path: pathlib.Path local file path

    Returns:
        file_read: str read file
    """

    logger.info('read_file_from_path - Start')

    # Check if the file_path exists
    if file_path.exists():

        logger.info('read_file_from_path - Reading file from %s', file_path.as_posix())

        # Read file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_read = file.read()
    else:
        raise FileNotFoundError(f'Unable to locate file: {file_path.as_posix()}')

    logger.info('read_file_from_path - Successfully file read from %s', file_path.as_posix())

    logger.info('read_file_from_path - Start')

    return file_read


def read_bq_from_query(client: bigquery.Client,
                       query_config: dict,
                       ) -> pd.DataFrame:
    """
    Read the query from local path and retrieve data from BigQuery

    Args:
        client: bigquery.Client BigQuery client for connection
        query_config: Dictionary query configurations (path and parameters)

    Returns
        data: pd.DataFrame retrieved data
    """
    logger.info('read_bq_from_query - Start')

    # Retrieve query path
    query_path = build_path_from_list(query_config['query_path'])

    logger.info('read_bq_from_query - Reading query file: %s', query_path.as_posix())

    # Read local query file
    query = read_file_from_path(query_path)

    # Check if there are parameters
    if 'query_parameters' not in query_config.keys():

        logger.info('read_bq_from_query - Querying BigQuery without Parameters')

        # Read data from BigQuery
        data = client.query(query)

    else:

        # Retrieve BigQuery query parameters
        parameters = build_bigquery_query_parameters_from_dictionary(
            query_config['query_parameters']
        )

        logger.info('read_bq_from_query - Querying BigQuery with Parameters')

        # Read data from BigQuery with parameters
        data = client.query(query,
                            job_config=bigquery.QueryJobConfig(query_parameters=parameters))

    logger.info('read_bq_from_query - Successfully retrieve data')

    logger.info('read_bq_from_query - End')

    return data.to_dataframe()


def build_path_from_list(path_list: list) -> pathlib.Path:
    """
    Build absolute pathlib.Path from relative path list from project root

    Args:
        path_list: List of relative path from root

    Returns
        absolute_path: pathlib.Path absolute path
    """
    logger.info('build_path_from_list - Start')
    logger.info('build_path_from_list - Retrieve root path to the project folder')

    # Retrieve root path
    root_path = pathlib.Path(__file__).parents[2]

    # Initialise the returned absolute path
    absolute_path = root_path

    logger.info('build_path_from_list - Build the absolute path')

    # Build the absolute path to the target folder/file
    for folder in path_list:

        # Add the folder to the absolute path
        absolute_path = absolute_path / folder

    logger.info('build_path_from_list - End')

    return absolute_path


def build_bigquery_query_parameters_from_dictionary(query_parameters: dict) -> list:
    """
    Build BigQuery query parameters from a dictionary in which each key
    is a BigQuery Parameter like:
        name: <name_of_the_query_parameter>
        array_type: <type_of_the_parameter>
        value: <value_of_the_parameter>

    Args:
        query_parameters: dict parameters

    Returns
        bigquery_query_parameters: list BigQuery query parameters
    """

    logger.info('build_bigquery_query_parameters_from_dictionary - Start')

    # Initialise empty list BigQuery query parameters
    bigquery_query_parameters = []

    logger.info('build_bigquery_query_parameters_from_dictionary - Fetch BigQuery parameters')

    # Fetch all query parameters
    for query_parameter_key in query_parameters.keys():

        # Check if the ScalarQueryParameter or ArrayQueryParameter is required
        # The difference is in the type of values passed (No list: scalar, list: array)
        if isinstance(query_parameters[query_parameter_key]['value'], list):

            # Build the parameter
            bigquery_parameter = bigquery.ArrayQueryParameter(
                query_parameters[query_parameter_key]['name'],
                query_parameters[query_parameter_key]['type'],
                query_parameters[query_parameter_key]['value']
            )
        else:
            # Build the parameter
            bigquery_parameter = bigquery.ScalarQueryParameter(
                query_parameters[query_parameter_key]['name'],
                query_parameters[query_parameter_key]['type'],
                query_parameters[query_parameter_key]['value']
            )
        # Append to the list of parameters
        bigquery_query_parameters.append(bigquery_parameter)

    logger.info('build_bigquery_query_parameters_from_dictionary - End')

    return bigquery_query_parameters
