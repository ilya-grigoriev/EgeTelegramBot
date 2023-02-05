"""This module help to create database or tables of database."""
import traceback
from typing import List

from psycopg2 import extensions

from logger_for_project import my_logger
from work_with_db.config_for_db import CODE_FOR_CREATING_TABLE
from parse_data.config_for_parsing import subjects_en


def create_tables(*, conn: extensions.connection, tables_name: List[str]) -> None:
    """
    Create tables of database.

    Parameters
    ----------
    conn : extensions.connection
        Psycopg2 connection to PostgreSQL.
    tables_name : List[str]
        List of table's name (default, subjects_en from config_for_db.py).
    """
    if not tables_name:
        tables_name = subjects_en

    try:
        cursor = conn.cursor()
        for table in tables_name:
            code = CODE_FOR_CREATING_TABLE.format(table)
            cursor.execute(code)
    except Exception:
        conn.rollback()
        my_logger.error(traceback.format_exc())
    else:
        conn.commit()
