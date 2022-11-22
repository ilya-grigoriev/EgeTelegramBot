import aiosqlite
from config import translation
import sqlite3
from format_data import format_data_from_db


def insert_data(subject: str, data: str) -> None:
    subject = translation.get(subject)
    con = sqlite3.connect('tasks_for_subjects.db')
    cur = con.cursor()
    total_request = f"""INSERT OR IGNORE INTO {subject}
                        (level_name, number_task, task_title, task_text, 
                        text, answers, correct_answer, img) VALUES {data}"""
    cur.execute(total_request)
    con.commit()
    con.close()


async def select_data(subject: str) -> str | None:
    trans_subject = translation.get(subject)
    async with aiosqlite.connect('tasks_for_subjects.db') as db:
        cursor = await db.execute(f"""SELECT * FROM {trans_subject}
                                      LIMIT 1 
                                      OFFSET ABS(RANDOM()) % MAX((
                                      SELECT COUNT(*) 
                                      FROM {trans_subject}), 1);""")
        task = await cursor.fetchone()
    return format_data_from_db(task)
