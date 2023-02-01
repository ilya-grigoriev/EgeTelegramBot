"""This module help to check tables of database."""
import psycopg2.errors

from parse_data.config_for_parsing import subjects_en
from work_with_db.create_data.create_db_or_tables import create_tables
import traceback
from logger_for_project import my_logger


def check_existing_tables_db(*, conn) -> None:
    """
    Check existing tables of database.

    Parameters
    ----------
    conn: psycopg2.connection
        Connection to PostgreSQL.
    """
    cursor = conn.cursor()
    for subject in subjects_en:
        try:
            cursor.execute(f"SELECT count(task_section) FROM {subject}")
            conn.commit()
        except psycopg2.errors.UndefinedTable:
            conn.rollback()
            my_logger.error(traceback.format_exc())
            create_tables(conn=conn, tables_name=[subject])
            my_logger.info(f"Table {subject} created")
        except Exception:
            my_logger.error(traceback.format_exc())
    cursor.close()


if __name__ == "__main__":
    pass
