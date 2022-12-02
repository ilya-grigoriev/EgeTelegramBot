import asyncio
import os
import traceback
import aiosqlite
from loguru import logger

from parse_data.format.format_data_from_database import format_data_from_db


async def select_task(*, subject: str) -> tuple[str, None] | None:
    try:
        par_dir = os.path.dirname(f'{os.path.dirname(__file__)}')
        path = os.path.join(par_dir, r'db\tasks_for_subjects.db')
        async with aiosqlite.connect(path) as db:
            cursor = await db.execute(f"""SELECT * FROM {subject}
                                          LIMIT 1 
                                          OFFSET ABS(RANDOM()) % MAX((
                                          SELECT COUNT(*) 
                                          FROM {subject}), 1);""")
            task = await cursor.fetchone()
        return format_data_from_db(subject=subject, data=task)
    except Exception as e:
        logger.error(traceback.format_exc())


if __name__ == '__main__':
    resp = asyncio.run(select_task(subject='math'))
    if resp:
        task, a = resp
        print(task[0])
        print(task[1])
