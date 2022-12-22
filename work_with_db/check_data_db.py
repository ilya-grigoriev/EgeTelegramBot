import sqlite3
import traceback

from loguru import logger

from parse_data.config_for_parsing import translation_from_eng, subjects_en
from work_with_db.typing_for_work_with_db import db_path
from parse_data.format.parse_data_and_update_database import \
    parse_data_and_update_db


def check_data_of_tables(*, db_file_path: db_path) -> None:
    con = None
    try:
        con = sqlite3.connect(db_file_path)
        cursor = con.cursor()
        for subject in subjects_en:
            subject_ru = translation_from_eng.get(subject)
            response = cursor.execute(f'SELECT count(id) FROM {subject}')
            response = response.fetchone()[0]
            if response == 0:
                parse_data_and_update_db(subject_name=subject_ru, n_tasks=100)
    except Exception as e:
        logger.error(traceback.format_exc(e))
    finally:
        if con:
            con.close()
