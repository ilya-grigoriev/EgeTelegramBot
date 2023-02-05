"""This module help to insert data to database."""
import traceback
from typing import List, Optional

from work_with_db.config_for_db import conn, CODE_FOR_INSERTING_DATA_IN_TABLE
from logger_for_project import my_logger


class ConnectionIsNoneException(Exception):
    """Raised when Psycopg2 connection is None."""


async def insert_tasks(
    *, subject_name_en: str, values_for_inserting: List[Optional[str]]
) -> None:
    """
    Insert data of tasks to database.

    Parameters
    ----------
    subject_name_en : str
        Name of table for database.
    values_for_inserting : List[str]
        List of values for inserting.
    """
    with conn.cursor() as cursor:
        try:
            my_logger.info("Insert values in database")
            try:
                for task in values_for_inserting:
                    request = CODE_FOR_INSERTING_DATA_IN_TABLE.format(
                        subject_name_en, task
                    )
                    cursor.execute(request)
            except Exception:
                my_logger.error(traceback.format_exc())
            else:
                if conn is not None:
                    conn.commit()
                    my_logger.success("Values inserted in database")
                else:
                    raise ConnectionIsNoneException("ConnectionIsNoneException")
        except Exception:
            my_logger.error(traceback.format_exc())
