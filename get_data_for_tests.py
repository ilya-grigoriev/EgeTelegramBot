import requests
from bs4 import BeautifulSoup
from config import headers
from parse_sites import parse_tests

def get_url_of_themes(url: str):

def get_url_of_tests(sample: str, content: requests.Response.content):
    bs = BeautifulSoup(content, 'html.parser')
    urls = bs.find_all('span', attrs={'class': 'prob_nums'})
    formatted_urls = []
    for url in urls:
        href = url.findNext()['href']
        total_url = f'{sample}{href}'
        formatted_urls.append(total_url)
    return formatted_urls


def get_data_of_url(url) -> list:
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
