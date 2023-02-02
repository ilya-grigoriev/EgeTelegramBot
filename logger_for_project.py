"""This module is designed for creating logger."""
import loguru
from parse_data.config_for_parsing import PATH_DIR

file_path = f"{PATH_DIR}\\out.log"
my_logger = loguru.logger
my_logger.add(file_path)
