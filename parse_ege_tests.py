from urllib.request import urlopen, urlretrieve
from io import StringIO

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}


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


def get_url_of_tests(sample: str, content: requests.Response.content):
    bs = BeautifulSoup(content, 'html.parser')
    urls = bs.find_all('span', attrs={'class': 'prob_nums'})
    formatted_urls = []
    for url in urls:
        href = url.findNext()['href']
        total_url = f'{sample}{href}'
        formatted_urls.append(total_url)
    return formatted_urls


def get_data_of_url() -> list:
    page_n = 1
    while True:
        response = requests.post(
            f'https://ege.sdamgia.ru/search?keywords=1&cb=1&search=5.1.1 Треугольник&page={page_n}',
            headers=headers)
        if response.status_code == 200:
            content = response.content.decode('utf-8')  # форматируем кириллицу
            urls = get_url_of_tests('https://ege.sdamgia.ru', content)
            parse_tests(urls, 'https://ege.sdamgia.ru')
        page_n += 1
        break


def get_problems() -> list:
    get_data_of_url()


if __name__ == '__main__':
    get_problems()
