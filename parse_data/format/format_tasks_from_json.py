import asyncio
from typing import List, Optional

from parse_data.format.format_data_for_database import format_data_for_db
from parse_data.get_data.get_data_for_db import get_data_from_json
from parse_data.typing_for_parsing import data_from_json
from work_with_db.create_data.insert_data import insert_tasks


def format_and_insert_tasks(tasks: data_from_json, subject_name: str,
                            task_ids_in_db: List = list()) -> None:
    if tasks:
        formatted_tasks = []
        for task in tasks:
            if task.get('id') not in task_ids_in_db:
                task_data = get_data_from_json(task=task)
                if task_data:
                    formatted_task = format_data_for_db(task=task_data)
                    formatted_tasks.append(formatted_task)
        asyncio.get_event_loop().run_until_complete(
            insert_tasks(subject=subject_name,
                         values_for_inserting=formatted_tasks))
    task_ids_in_db.clear()
