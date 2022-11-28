import sqlite3
from config_for_parsing import translation_for_db
from loguru import logger


def insert_tasks(*, subject: str, data: str) -> None:
    subject_name = translation_for_db.get(subject)
    con = sqlite3.connect(database='../db/tasks_for_subjects.db')
    cur = con.cursor()
    try:
        if subject != 'Математика профильная':
            total_request = f"""INSERT OR IGNORE INTO {subject_name}
                                (level_name, number_task, task_title, task_text, 
                                text, answers, correct_answer) VALUES {data}"""
        else:
            total_request = f"""INSERT OR IGNORE INTO {subject_name}
                                (level_name, number_task, task_title, task_text, 
                                correct_answer, img) VALUES {data}"""
        cur.execute(total_request)
        con.commit()
    except Exception as e:
        logger.error(e)
    finally:
        con.close()
