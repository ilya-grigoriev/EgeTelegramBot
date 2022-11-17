import aiosqlite
from config import translation
import sqlite3


# from format_data import format_data_from_db


def insert_data(subject: str, data: str) -> None:
    subject = translation.get(subject)
    con = sqlite3.connect('tasks_for_subjects.db')
    cur = con.cursor()
    total_request = f"""INSERT OR IGNORE INTO {subject}
                    VALUES {data}"""
    cur.execute(total_request)
    con.commit()
    con.close()


async def get_count_tasks(subject: str) -> list[str]:


async def select_data(subject: str, n_tasks: int) -> list[str]:
    trans_subject = translation.get(subject)
    async with aiosqlite.connect('tasks_for_subjects.db') as db:
        cursor = await db.execute(f"""SELECT * FROM {trans_subject}
                                    LIMIT {n_tasks}""")
        data = await cursor.fetchall()
    return format_data_from_db(data)
