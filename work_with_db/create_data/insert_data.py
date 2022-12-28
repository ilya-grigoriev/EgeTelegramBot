import traceback
from typing import List

import asyncpg
from parse_data.config_for_parsing import translation_from_rus
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB, \
    code_for_insert_data_in_table
from loguru import logger


async def insert_tasks(*, subject: str,
                       values_for_inserting: List[str]) -> None:
    subject_name = translation_from_rus.get(subject)
    conn = await asyncpg.connect(user=USER_DB, password=PASSWORD_DB,
                                 port=PORT_DB, database='subjects',
                                 host=HOST_DB)
    tr = None
    try:
        tr = conn.transaction()
        await tr.start()
        for task in values_for_inserting:
            request = code_for_insert_data_in_table.format(subject_name,
                                                           task)
            await conn.execute(request)
    except Exception as e:
        if tr:
            await tr.rollback()
        logger.error(traceback.format_exc())
    else:
        await tr.commit()
        await conn.close()


if __name__ == '__main__':
    pass
