import os
import sqlite3
import traceback
from loguru import logger
from work_with_db.config_for_db import code_for_creating_tables, file_path
from work_with_db.typing_for_work_with_db import db_path
from parse_data.config_for_parsing import subjects_en


def create_db() -> db_path:
    if not os.path.isfile(file_path):
        file = open(file=file_path, mode='w')
        file.close()
    return file_path


def create_tables(*, db_file_path: str, tables_name=subjects_en):
    con = None
    try:
        con = sqlite3.connect(db_file_path)
        cursor = con.cursor()
        for table in tables_name:
            cursor.execute(code_for_creating_tables.format(table))
    except Exception as e:
        logger.error(traceback.format_exc(e))
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    file_path = create_db()
    create_tables(db_file_path=file_path)
