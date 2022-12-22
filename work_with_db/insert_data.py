import traceback

from parse_data.get_data.get_path import get_path_for_file
import sqlite3
from parse_data.config_for_parsing import translation_from_rus
from loguru import logger


def insert_tasks(*, subject: str, data: str) -> None:
    subject_name = translation_from_rus.get(subject)
    path = get_path_for_file(path_dir_file=r'db\tasks_for_subjects.db')
    con = sqlite3.connect(database=path)
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
