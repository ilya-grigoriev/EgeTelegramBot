import json

import requests
from loguru import logger

from config_for_parsing import headers_for_get_tasks_of_subjects


def get_json_of_tasks_for_subject(*, subject_id: int, n_tasks: int) -> list[
    dict]:
    json_data = {
        'subjectId': str(subject_id),
        'levelIds': [],
        'themeIds': [],
        'typeIds': [],
        'id': '',
        'favorites': 0,
        'answerStatus': 0,
        'themeSectionIds': [],
        'published': 0,
        'extId': '',
        'fipiCode': '',
        'docId': '',
        'isAdmin': False,
        'loadDates': [],
        'isPublished': False,
        'pageSize': n_tasks,
        'pageNumber': 1,
    }

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
