from get_data_for_tests import get_url_of_themes


def main():
    url = 'http://ege.fipi.ru/os11/xmodules/qprint/index.php'
    themes = get_url_of_themes(url)


if __name__ == '__main__':
    main()
