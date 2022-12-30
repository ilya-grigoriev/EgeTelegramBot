import os
import sqlite3
import traceback

import psycopg2
from logger_for_project import logger
from work_with_db.config_for_db import code_for_creating_table
from parse_data.config_for_parsing import subjects_en


def create_tables(*, conn, tables_name=subjects_en):
    try:
        cursor = conn.cursor()
        for table in tables_name:
            code = code_for_creating_table.format(table)
            cursor.execute(code)
    except Exception as e:
        conn.rollback()
        logger.error(traceback.format_exc(e))
    else:
        conn.commit()


if __name__ == '__main__':
    pass
