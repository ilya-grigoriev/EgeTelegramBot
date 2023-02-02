"""This module is designed for creating logger."""
import os.path

import loguru
from parse_data.config_for_parsing import PATH_DIR

file_path = f"{PATH_DIR}\\out.log"
if not os.path.isfile(file_path):
    with open(file_path, mode="w", encoding="utf-8") as file:
        file_out = file
else:
    with open(file_path, mode="a", encoding="utf-8") as file:
        file_out = file
my_logger = loguru.logger
my_logger.add(file_out)
