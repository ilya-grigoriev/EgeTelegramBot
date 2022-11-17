import json

import loguru as loguru
import requests
from bs4 import BeautifulSoup
import config
from format_data import format_tasks
from parse_sites import parse_tests
from get_data_for_site import get_response_from_site
from loguru import logger


def get_url_of_themes(sample: str, url: str):
    response, status_code = get_response_from_site(url, cookies=config.cookies)
    response.encoding = 'utf-8'

    if status_code == 200:
        bs = BeautifulSoup(response.content, 'html.parser')
        themes_body = bs.find_all('td', attrs={'coursebody'})
        themes = []
        for theme in themes_body:
            href = theme.find('a')['href']
            total_url = f'{sample}{href}'
            themes.append(total_url)
        return themes


def get_url_of_tests(sample: str, content: requests.Response.content):
    bs = BeautifulSoup(content, 'html.parser')
    urls = bs.find_all('span', attrs={'class': 'prob_nums'})
    formatted_urls = []
    for url in urls:
        href = url.findNext()['href']
        total_url = f'{sample}{href}'
        formatted_urls.append(total_url)
    return formatted_urls


def get_json_of_subject_ids() -> list[dict]:
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'http://os.fipi.ru/home/1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    url = 'http://os.fipi.ru/api/dictionaries'
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()['subjects']
        return data
    else:
        logger.error(f"Connection is failed. URL: {url}")


def get_json_of_tasks_for_subject(subject_id: int, n_tasks: int) -> list[dict]:
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://os.fipi.ru',
        'Pragma': 'no-cache',
        'Referer': 'http://os.fipi.ru/tasks/1/a',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sessionId': '99822373-c237-221c-5dba-5beb02f99661',
    }

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
    response = requests.post(url, headers=headers, json=json_data,
                             verify=False)
    if response.status_code == 200:
        data = response.json().get('tasks')
        with open('test.json', mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        return data
    else:
        logger.error(f"Connection is failed. URL: {url}")


def create_session(urls: list) -> requests.Session:
    session = requests.Session()
    for url in urls:
        get_response_from_site(url, cookies=session.cookies, session=session)
    return session


if __name__ == '__main__':
    # get_subject_ids()
    print(format_tasks(get_json_of_tasks_for_subject(1, 2)))
