from get_data_for_tests import get_json_of_tasks_for_subject
from format_data import format_tasks, format_data_for_db
from work_with_db.insert_data import insert_tasks
from get_data_for_tests import get_json_of_subject_ids
from loguru import logger


def parse_data_and_update_db(*, subject_name: str) -> None:
    subjects = get_json_of_subject_ids()
    current_subject_id = None
    for subject in subjects:
        if subject['name'] == subject_name:
            current_subject_id = subject['id']
            logger.info('Set name for subject')
            break
    if current_subject_id:
        tasks = format_tasks(
            get_json_of_tasks_for_subject(subject_id=current_subject_id,
                                          n_tasks=10))
        logger.info('Tasks formatted')
        for task in tasks:
            formatted_task = format_data_for_db(task=task)
            insert_tasks(subject=subject_name, data=formatted_task)


if __name__ == '__main__':
    parse_data_and_update_db(subject_name='Русский язык')
