import traceback
from typing import List

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
    *, subject_name_en: str, values_for_inserting: List[str]
) -> None:
    try:
        conn = await asyncpg.connect(
            user=USER_DB,
            password=PASSWORD_DB,
            port=PORT_DB,
            database="subjects",
            host=HOST_DB,
        )
        tr = conn.transaction()
    except Exception as e:
        my_logger.error(traceback.format_exc())
    else:
        my_logger.info("Insert values in database")
        try:
            await tr.start()
            for task in values_for_inserting:
                request = code_for_insert_data_in_table.format(subject_name_en, task)
                await conn.execute(request)
        except Exception as e:
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
