import os.path

import loguru
from parse_data.config_for_parsing import path_dir

file_path = f"{path_dir}\\out.log"
if not os.path.isfile(file_path):
    file = open(file_path, mode="w")
else:
    file = open(file_path, mode="a")
my_logger = loguru.logger
my_logger.add(file)
