from loguru import logger

from parse_data.format.format_tasks_from_json import format_tasks
from parse_data.format.format_data_for_database import format_data_for_db
from parse_data.get_data.get_data_of_tasks import get_json_of_tasks_for_subject
from parse_data.get_data.get_data_of_subject_ids import get_json_of_subject_ids
from work_with_db.insert_data import insert_tasks


def parse_data_and_update_db(*, subject_name: str, n_tasks: int) -> None:
    subjects = get_json_of_subject_ids()
    current_subject_id = None
    for subject in subjects:
        if subject['name'] == subject_name:
            current_subject_id = subject['id']
            logger.info('Set id for subject')
            break
    if current_subject_id:
        tasks = format_tasks(
            get_json_of_tasks_for_subject(subject_id=current_subject_id,
                                          n_tasks=n_tasks), current_subject_id)
        logger.info('Tasks formatted')
        for task in tasks:
            formatted_task = format_data_for_db(subject_id=current_subject_id,
                                                task=task)
            insert_tasks(subject=subject_name, data=formatted_task)
