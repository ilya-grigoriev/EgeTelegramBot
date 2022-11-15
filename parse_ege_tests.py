from get_data_for_tests import get_url_of_themes, set_cookies


def main():
    url = 'http://ege.fipi.ru/os11/xmodules/qprint/index.php'
    urls_for_getting_cookies = ['https://fipi.ru/ege', url]
    set_cookies(urls_for_getting_cookies)
    themes = get_url_of_themes(url, url)
    print(themes)


if __name__ == '__main__':
    main()
