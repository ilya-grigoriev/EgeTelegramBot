headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://fipi.ru/ege/otkrytyy-bank-zadaniy-ege',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

headers_for_get_tasks_of_subjects = {
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

headers_for_get_subject_ids = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://os.fipi.ru/home/1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

translation_from_telegram = {
    'russian': 'Русский язык',
    'math': 'Математика профильная'
}

translation_for_db = {
    'Русский язык': 'russian',
    'Математика профильная': 'math'
}

json_data = {
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
    'pageNumber': 1,
}

path_dir = '\\'.join(str(__file__).rsplit('\\')[:-2])
subjects = ['Русский язык', 'Математика профильная']
