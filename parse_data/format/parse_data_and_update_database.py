from loguru import logger

from parse_data.format.format_tasks_from_json import format_tasks
from parse_data.format.format_data_for_database import format_data_for_db
from parse_data.get_data.get_data_of_tasks import get_json_of_tasks_for_subject
from parse_data.get_data.get_data_of_subject_ids import get_json_of_subject_ids
from work_with_db.insert_data import insert_tasks
from parse_data.get_data.get_subject_id import get_subject_id_from_json


def parse_data_and_update_db(*, subject_name: str, n_tasks: int) -> None:
    subjects = get_json_of_subject_ids()
    current_subject_id = get_subject_id_from_json(subjects=subjects,
                                                  subject_name=subject_name)
    if current_subject_id:
        tasks = format_tasks(
            tasks=get_json_of_tasks_for_subject(subject_id=current_subject_id,
                                                n_tasks=n_tasks),
            subject_name=subject_name)
        logger.info('Tasks formatted')
        # for task in tasks:
        #     formatted_task = format_data_for_db(task=task)
        #     insert_tasks(subject=subject_name, data=formatted_task)


if __name__ == '__main__':
    parse_data_and_update_db(subject_name='Математика профильная', n_tasks=100)
