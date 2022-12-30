import requests
from logger_for_project import logger
from parse_data.typing_for_parsing import data_subjects
from typing import Any
from parse_data.config_for_parsing import headers_for_get_subject_ids


def get_json_of_subject_ids() -> data_subjects | Any:
    url = 'http://os.fipi.ru/api/dictionaries'
    response = requests.get(url, headers=headers_for_get_subject_ids,
                            verify=False)
    if response.status_code == 200:
        logger.info('Get subject ids from json')
        data = response.json()['subjects']
        return data
    else:
        logger.error(f"Connection is failed. URL: {url}")
        return None
