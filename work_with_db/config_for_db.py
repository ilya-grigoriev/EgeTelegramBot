"""Module is designed for config data."""
import os

import psycopg2

from dotenv import load_dotenv
from parse_data.config_for_parsing import PATH_DIR

load_dotenv()

CODE_FOR_CREATING_TABLE = """CREATE TABLE {} (
                            task_section       VARCHAR  NOT NULL,
                            id_task            INTEGER  NOT NULL UNIQUE,
                            is_detailed        BOOLEAN  NOT NULL,
                            task_desc_html     VARCHAR  NOT NULL,
                            file_urls_for_task VARCHAR  NOT NULL,
                            text_for_task_html VARCHAR  NOT NULL,
                            solution_html      VARCHAR  NOT NULL,
                            answer             VARCHAR  NOT NULL
);
"""
CODE_FOR_INSERTING_DATA_IN_TABLE = (
    "INSERT INTO {} (task_section, id_task, "
    "is_detailed, task_desc_html, file_urls_for_task,"
    "text_for_task_html, solution_html, answer) "
    "VALUES {} ON CONFLICT DO NOTHING"
)
CODE_FOR_GETTING_TASK = (
    "SELECT * FROM {} WHERE TASK_SECTION LIKE '{}' ORDER BY RANDOM() LIMIT 1;"
)
file_path = rf"{PATH_DIR}\db\tasks_for_subjects.db"
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
conn = psycopg2.connect(
    dbname="subjects",
    user=USER_DB,
    password=PASSWORD_DB,
    host=HOST_DB,
    port=PORT_DB,
)
