"""
This module implements a Logger object to
log information according to the configuration file
"""
# Import Standard Libraries
import logging.config
import pathlib
import yaml


def get_logger(logger_name: str,
               configuration_file_path: pathlib.Path) -> logging.Logger:
    """
    Set the configuration for the logging module and return the requested logger

    Args:
        logger_name: String name of the logger to retrieve from configuration file
        configuration_file_path: pathlib.Path location of the configuration file

    Returns:
        logging.Logger logger object
    """

    if configuration_file_path.exists():

        # Read the log_configuration file
        with open(configuration_file_path, 'r', encoding='utf-8') as file:
            log_config = yaml.safe_load(file.read())

        # Set logging configuration file
        logging.config.dictConfig(log_config)

        # Retrieve the requested logger
        logger = logging.getLogger(logger_name)

    else:

        raise FileNotFoundError(
            f'get_logger - File {configuration_file_path.as_posix()} not found'
        )

    return logger
