import asyncio

import aiosqlite
from loguru import logger

from parse_data.format.format_data_from_database import format_data_from_db


async def select_task(*, subject: str) -> tuple[tuple[str, None], str] | None:
    try:
        async with aiosqlite.connect('../db/tasks_for_subjects.db') as db:
            cursor = await db.execute(f"""SELECT * FROM {subject}
                                          LIMIT 1 
                                          OFFSET ABS(RANDOM()) % MAX((
                                          SELECT COUNT(*) 
                                          FROM {subject}), 1);""")
            task = await cursor.fetchone()
        return format_data_from_db(subject=subject, data=task), task[-2]
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    task, a = asyncio.run(select_task(subject='math'))
    print(task[0])
    print(task[1])
