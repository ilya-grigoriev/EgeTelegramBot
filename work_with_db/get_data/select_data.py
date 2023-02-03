"""This module help to select data from database."""
import asyncio
import traceback
from typing import Optional

from psycopg2 import errors
from logger_for_project import my_logger
from parse_data.typing_for_parsing import DataFromDB
from work_with_db.config_for_db import conn
from work_with_db.config_for_db import CODE_FOR_GETTING_TASK
from work_with_db.create_data.create_db_or_tables import create_tables


async def select_task(*, subject_name: str, task_section: str) -> Optional[DataFromDB]:
    """
    Select data of task from database.

    Parameters
    ----------
    subject_name: str
        Name of table.
    task_section: str
        Task section (example, '1/5').

    Returns
    -------
    Optional[DataFromDb]
        Dataclass with data from database.
    """
    try:
        with conn:
            with conn.cursor() as cursor:
                my_logger.info("Getting task from db...")
                request = CODE_FOR_GETTING_TASK.format(subject_name, task_section)
                cursor.execute(request)
                conn.commit()
                my_logger.success("Getting task is finished")

                task = cursor.fetchone()
        if task:
            data = DataFromDB(*task)
            return data
    except errors.UndefinedTable:  # pylint: disable=no-member
        my_logger.error(traceback.format_exc())
        create_tables(conn=conn, tables_name=[subject_name])
        my_logger.info(f"Table {subject_name} created")
    except Exception:
        my_logger.error(traceback.format_exc())
    return None


if __name__ == "__main__":
    resp = asyncio.run(select_task(subject_name="math", task_section="1/%"))
    if resp:
        print(resp)
