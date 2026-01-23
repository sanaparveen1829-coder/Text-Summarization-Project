import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

        Raises:
        BoxValueError: If the YAML file is empty or cannot be parsed.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
                content = yaml.safe_load(yaml_file)
                logger.info(f"YAML file {path_to_yaml} loaded successfully")
                return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file {path_to_yaml} is empty or cannot be parsed")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
     
    """Returns the size of a file in kilobytes.

    Args:
        path (Path): The path to the file.
    Returns:
        str: The size of the file in kilobytes.
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"