"""This module help to create database or tables of database."""
import traceback

from logger_for_project import my_logger
from work_with_db.config_for_db import code_for_creating_table
from parse_data.config_for_parsing import subjects_en


def create_tables(*, conn, tables_name=subjects_en):
    """
    Create tables of database.

    Parameters
    ----------
    conn: psycopg2.connection
        Connection to PostgreSQL.
    tables_name: str, default=subjects_en
        Name of tables (default, subjects_en from config_for_db.py).
    """
    try:
        cursor = conn.cursor()
        for table in tables_name:
            code = code_for_creating_table.format(table)
            cursor.execute(code)
    except Exception as e:
        conn.rollback()
        my_logger.error(traceback.format_exc(e))
    else:
        conn.commit()


if __name__ == "__main__":
    pass
