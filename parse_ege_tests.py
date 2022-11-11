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


def parse_site(content: requests.Response.content) -> list:
    bs = BeautifulSoup(content, 'html.parser')


def get_data_of_url() -> list:
    page_n = 1
    while True:
        response = requests.post(
            f'https://ege.sdamgia.ru/search?keywords=1&cb=1&search=5.1.1 Треугольник&page={page_n}',
            headers=headers)
        if response.status_code == 200:
            content = response.content.decode('utf-8')  # форматируем кириллицу
            parse_site(content)
        page_n += 1


def get_tests() -> list:
    get_data_of_url()


if __name__ == '__main__':
    get_tests()
