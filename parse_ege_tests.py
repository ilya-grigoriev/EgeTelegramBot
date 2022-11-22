import asyncio

from get_data_for_tests import get_json_of_tasks_for_subject
from format_data import format_tasks, format_data_for_db, format_data_from_db
from work_with_db import insert_data, select_data


async def main_2():
    return await select_data('Русский язык')


def main():
    tasks = format_tasks(get_json_of_tasks_for_subject(1, 100))
    for task in tasks:
        formatted_task = format_data_for_db(task)
        insert_data('Русский язык', formatted_task)
    # print(asyncio.run(main_2()))


if __name__ == '__main__':
    main()
