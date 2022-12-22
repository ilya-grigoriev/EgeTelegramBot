import traceback

from parse_data.get_data.get_path import get_path_for_file
import sqlite3
from parse_data.config_for_parsing import translation_from_rus
from loguru import logger
from work_with_db.config_for_db import file_path

def insert_tasks(*, subject: str, data: str) -> None:
    subject_name = translation_from_rus.get(subject)
    con = sqlite3.connect(database=file_path)
    cur = con.cursor()
    try:
        request = f"INSERT OR IGNORE INTO {subject_name} (id_task, " \
                  f"level_name, number_task, html, correct_answer) VALUES {data}"
        cur.execute(request)
        con.commit()
    except Exception as e:
        print(request)
        logger.error(traceback.format_exc())
    finally:
        con.close()


if __name__ == '__main__':
    pass
