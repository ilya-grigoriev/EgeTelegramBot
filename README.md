[![Build status](https://github.com/Ilya-Grigoriev/EgeTelegramBot/actions/workflows/checks.yaml/badge.svg?branch=main)](https://github.com/Ilya-Grigoriev/EgeTelegramBot/actions/workflows/checks.yaml)

# Ege Telegram Bot

Этот бот предназначен для решения задач ЕГЭ с сайта [РЕШУЕГЭ](https://ege.sdamgia.ru/).

# Технологии бота

Этот бот написан на библиотеке [aiogram](https://github.com/aiogram/aiogram). В качестве базы данных используется PostgreSQL, работа с которой осуществляется с помощью библиотеки [psycopg2](https://github.com/psycopg/psycopg2).

# Запуск бота

1. Скачайте все необходимые зависимости:

```python
pip install -r requirements.txt
```

2. Создайте файл `.env` и скопируйте в него переменные из файла `.env.example`.
   После этого заполните значения переменных:
    - USER_DB - имя пользователя в PostgreSQL.
    - PASSWORD_DB - пароль пользователя в PostgreSQL.
    - HOST_DB - хост для PostgreSQL (по умолчанию 127.0.0.1).
    - PORT_DB - порт для PostgreSQL (по умолчанию 5432).
    - TOKEN - токен бота в Telegram.
3. Запустите файл `main.py`. Начнётся парсинг задач с сайтов и добавление данных в базу данных, после чего запустится бот (придётся немного подождать).
