from parse_data.format.format_data_for_database import format_data_for_db
from parse_data.get_data.get_data_for_db import get_data_from_json
from parse_data.typing_for_parsing import data_from_json
from work_with_db.insert_data import insert_tasks


def format_tasks(tasks: data_from_json, subject_name: str) -> None:
    if tasks:
        for task in tasks:
            task_data = get_data_from_json(task=task)
            if task_data:
                formatted_task = format_data_for_db(task=task_data)
                insert_tasks(subject=subject_name, data=formatted_task)
