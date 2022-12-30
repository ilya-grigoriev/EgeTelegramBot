import traceback

import psycopg2.errors
from logger_for_project import logger
from parse_data.config_for_parsing import translation_from_eng, subjects_en, \
    n_tasks
from parse_data.format.parse_data_and_update_database import \
    parse_data_and_update_db


def check_data_of_tables(*, conn) -> None:
    try:
        cursor = conn.cursor()
        for subject in subjects_en:
            subject_ru = translation_from_eng.get(subject)
            cursor.execute(f'SELECT count(id_task) FROM {subject}')
            parse_data_and_update_db(subject_name=subject_ru, n_tasks=n_tasks)
    except psycopg2.errors.InFailedSqlTransaction:
        conn.rollback()
    except Exception as e:
        logger.error(traceback.format_exc(e))
