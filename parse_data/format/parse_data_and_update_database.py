from logger_for_project import logger
from parse_data.format.format_tasks_from_json import format_and_insert_tasks
from parse_data.get_data.get_data_of_tasks import get_json_of_tasks_for_subject
from parse_data.get_data.get_data_of_subject_ids import get_json_of_subject_ids
from parse_data.get_data.get_subject_id import get_subject_id_from_json
from work_with_db.get_data.select_data import select_tasks


def parse_data_and_update_db(*, subject_name: str, n_tasks: int,
                             is_data_in_table: bool = False) -> None:
    subjects = get_json_of_subject_ids()
    current_subject_id = get_subject_id_from_json(subjects=subjects,
                                                  subject_name=subject_name)
    if current_subject_id != -1:
        tasks = get_json_of_tasks_for_subject(subject_id=current_subject_id,
                                              n_tasks=n_tasks)
        if is_data_in_table:
            tasks_in_table = select_tasks(subject=subject_name)
            task_ids_in_table = tuple(map(lambda x: x[0], tasks_in_table))
            format_and_insert_tasks(tasks=tasks, subject_name=subject_name,
                                    task_ids_in_db=task_ids_in_table)
        else:
            format_and_insert_tasks(tasks=tasks, subject_name=subject_name)
        logger.info('Tasks formatted')


if __name__ == '__main__':
    parse_data_and_update_db(subject_name='Математика профильная', n_tasks=10)
