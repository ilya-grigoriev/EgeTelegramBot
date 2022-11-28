import requests
from loguru import logger

from config_for_parsing import headers_for_get_subject_ids


def get_json_of_subject_ids() -> list[dict]:
    url = 'http://os.fipi.ru/api/dictionaries'
    response = requests.get(url, headers=headers_for_get_subject_ids,
                            verify=False)
    if response.status_code == 200:
        logger.info('Get subject ids from json')
        data = response.json()['subjects']
        return data
    else:
        logger.error(f"Connection is failed. URL: {url}")