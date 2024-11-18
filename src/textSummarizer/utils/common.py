import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging.coustom_log import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yamlfile:
            data = yaml.safe_load(yamlfile)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_derectory: list, verbose = True):
    for path in path_to_derectory:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"Directory {path} created successfully")


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the given file in a human-readable format."""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" {size_in_kb} KB"
