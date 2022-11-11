from io import StringIO
from urllib.request import urlretrieve
from config import headers

import requests
from bs4 import BeautifulSoup


def get_content_from_site(url: str, mode='get') -> (
        requests.Response | None, str | None):
    response = None
    status_code = None
    if mode == 'get':
        response: requests.Response = requests.get(url, headers=headers)
        status_code = response.status_code
    return response.content, status_code


def parse_tests(urls: list, sample: str) -> list:
    tests = []
    for url in urls:
        content, status_code = get_content_from_site(url)
        if content and status_code == 200:
            bs = BeautifulSoup(content, 'html.parser')

            problem = bs.find('div', attrs={'class': 'pbody'})
            condition = problem.select('p.left_margin:not(:empty)')[0].text
            image_of_problem = None
            if problem.find('img'):
                src_image_of_problem = problem.find('img')['src']
                total_url = f'{sample}{src_image_of_problem}'
                path_image = urlretrieve(total_url)[0]
                with open(path_image) as file:
                    image_of_problem = StringIO(file.read())
            tests.append((condition, image_of_problem, url))
    return tests
