from loguru import logger

from parse_data.format.format_tasks_from_json import format_tasks
from parse_data.get_data.get_data_of_tasks import get_json_of_tasks_for_subject
from parse_data.get_data.get_data_of_subject_ids import get_json_of_subject_ids
from parse_data.get_data.get_subject_id import get_subject_id_from_json


def parse_data_and_update_db(*, subject_name: str, n_tasks: int) -> None:
    subjects = get_json_of_subject_ids()
    current_subject_id = get_subject_id_from_json(subjects=subjects,
                                                  subject_name=subject_name)
    if current_subject_id != -1:
        tasks = get_json_of_tasks_for_subject(subject_id=current_subject_id,
                                              n_tasks=n_tasks)
        if tasks:
            format_tasks(tasks=tasks, subject_name=subject_name)
        logger.info('Tasks formatted')


if __name__ == '__main__':
    parse_data_and_update_db(subject_name='Математика профильная', n_tasks=10)
