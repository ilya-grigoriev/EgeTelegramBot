"""This module help to select data from database."""
import asyncio
import traceback
from typing import Optional

import psycopg2

from logger_for_project import my_logger
from parse_data.typing_for_parsing import DataFromDB
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB
from work_with_db.config_for_db import code_for_getting_task
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
    conn = None
    cursor = None
    task = None
    try:
        conn = psycopg2.connect(
            dbname="subjects",
            user=USER_DB,
            password=PASSWORD_DB,
            host=HOST_DB,
            port=PORT_DB,
        )
        cursor = conn.cursor()

        my_logger.info("Getting task from db...")
        request = code_for_getting_task.format(subject_name, task_section)
        cursor.execute(request)
        conn.commit()
        my_logger.success("Getting task is finished")

        task = cursor.fetchone()
    except psycopg2.errors.UndefinedTable:
        my_logger.error(traceback.format_exc())
        create_tables(conn=conn, tables_name=[subject_name])
        my_logger.info(f"Table {subject_name} created")
    except Exception:
        my_logger.error(traceback.format_exc())
    finally:
        if conn:
            cursor.close()  # type: ignore
            conn.close()
            if task:
                data = DataFromDB(*task)
                return data
        return None


if __name__ == "__main__":
    resp = asyncio.run(select_task(subject_name="math", task_section="1/%"))
    if resp:
        print(resp)
