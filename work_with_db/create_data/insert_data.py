"""This module help to insert data to database."""
import traceback
from typing import List, Optional

import asyncpg
from work_with_db.config_for_db import (
    USER_DB,
    PASSWORD_DB,
    HOST_DB,
    PORT_DB,
    code_for_insert_data_in_table,
)
from logger_for_project import my_logger


async def insert_tasks(
    *, subject_name_en: str, values_for_inserting: List[Optional[str]]
) -> None:
    """
    Insert data of tasks to database.

    Parameters
    ----------
    subject_name_en: str
        Name of table for database.
    values_for_inserting: List[str]
        List of values for inserting.
    """
    try:
        conn = await asyncpg.connect(
            user=USER_DB,
            password=PASSWORD_DB,
            port=PORT_DB,
            database="subjects",
            host=HOST_DB,
        )
        tr = conn.transaction()
    except Exception:
        my_logger.error(traceback.format_exc())
    else:
        my_logger.info("Insert values in database")
        try:
            await tr.start()
            for task in values_for_inserting:
                request = code_for_insert_data_in_table.format(subject_name_en, task)
                await conn.execute(request)
        except Exception:
            print(request)
            if tr:
                await tr.rollback()
            my_logger.error(traceback.format_exc())
        else:
            await tr.commit()
            await conn.close()
            my_logger.success("Values inserted in database")


if __name__ == "__main__":
    pass
