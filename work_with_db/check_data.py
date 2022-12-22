import sqlite3
import traceback

from loguru import logger

from work_with_db.typing_for_work_with_db import db_path
from parse_data.config_for_parsing import subjects_en
from parse_data.format.parse_data_and_update_database import \
    parse_data_and_update_db
from parse_data.config_for_parsing import translation_from_eng


def check_data_of_tables(*, db_file_path: db_path):
    con = None
    try:
        con = sqlite3.connect(db_file_path)
        cursor = con.cursor()
        for subject in subjects_en:
            response = cursor.execute(f'SELECT count(id) FROM {subject}')
            count_id_in_table = response.fetchone()[0]
            if count_id_in_table == 0:
                subject_ru = translation_from_eng.get(subject)
                if subject_ru:
                    parse_data_and_update_db(subject_name=subject_ru,
                                             n_tasks=100)
    except Exception as e:
        logger.error(traceback.format_exc(e))
    finally:
        if con:
            con.close()
