import aiosqlite
from parse_data.format_data import format_data_from_db


async def select_task(*, subject: str) -> tuple[str, str] | None:
    async with aiosqlite.connect('db/tasks_for_subjects.db') as db:
        cursor = await db.execute(f"""SELECT * FROM {subject}
                                      LIMIT 1 
                                      OFFSET ABS(RANDOM()) % MAX((
                                      SELECT COUNT(*) 
                                      FROM {subject}), 1);""")
        task = await cursor.fetchone()
    return format_data_from_db(task), task[-2]
