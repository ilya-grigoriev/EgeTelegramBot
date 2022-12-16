import json

import requests
from loguru import logger
from parse_data.typing_for_parsing import data_from_json
from typing import Any
from config_for_parsing import headers_for_get_tasks_of_subjects, json_data


def get_json_of_tasks_for_subject(*, subject_id: int,
                                  n_tasks: int) -> data_from_json | Any:
    json_data.update(
        {
            'subjectId': str(subject_id),
            'pageSize': n_tasks
        }
    )
    url = 'http://os.fipi.ru/api/tasks'

    response = requests.post(url, headers=headers_for_get_tasks_of_subjects,
                             json=json_data,
                             verify=False)

    with open('test.json', mode='w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False)

    if response.status_code == 200:
        logger.info('Get tasks for subject from json')
        data = response.json().get('tasks')
        return data
    else:
        logger.error(f"Connection is failed. URL: {url}")
        return None
