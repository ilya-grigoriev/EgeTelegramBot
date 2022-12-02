import glob
import os
import sqlite3
from config_for_parsing import translation_for_db
from loguru import logger


def insert_tasks(*, subject: str, data: str) -> None:
    subject_name = translation_for_db.get(subject)
    path = glob.glob('../db/tasks_for_subjects.db', recursive=True)
    con = sqlite3.connect(database=path[0])
    cur = con.cursor()
    try:
        total_request = f"""INSERT OR IGNORE INTO {subject_name}
                            (level_name, number_task, html, 
                            correct_answer) VALUES {data}"""
        cur.execute(total_request)
        con.commit()
    except Exception as e:
        logger.error(e)
    finally:
        con.close()


if __name__ == '__main__':
    insert_tasks(subject='Математика профильная', data='a')
