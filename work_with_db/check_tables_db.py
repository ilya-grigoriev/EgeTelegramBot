import sqlite3
from parse_data.config_for_parsing import path_dir, subjects_en
from work_with_db.config_for_db import file_path
from work_with_db.create_db_or_tables import create_tables, create_db
import traceback
import os
from loguru import logger


def check_existing_tables_db(*, file_path: str) -> None:
    if os.path.isfile(file_path):
        con = None
        try:
            con = sqlite3.connect(file_path)
            cursor = con.cursor()
            for subject in subjects_en:
                try:
                    cursor.execute(f'SELECT count(id) FROM {subject}')
                except sqlite3.OperationalError:
                    create_tables(db_file_path=file_path,
                                  tables_name=[subject])
        except Exception as e:
            logger.error(traceback.format_exc(e))
        finally:
            if con:
                con.close()


if __name__ == '__main__':
    check_existing_tables_db(file_path=file_path)
