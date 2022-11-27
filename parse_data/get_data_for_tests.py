import requests
from loguru import logger
from config_for_parsing import headers_for_get_tasks_of_subjects, \
    headers_for_get_subject_ids


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
    if response.status_code == 200:
        logger.info('Get tasks for subject from json')
        data = response.json().get('tasks')
        return data
    else:
        logger.error(f"Connection is failed. URL: {url}")


if __name__ == '__main__':
    print(get_json_of_subject_ids())
