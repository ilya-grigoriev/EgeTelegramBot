import os

from parse_data.config_for_parsing import path_dir

code_for_creating_table = """CREATE TABLE {} (
                            task_section       VARCHAR  NOT NULL,
                            id_task            INTEGER  NOT NULL UNIQUE,
                            is_detailed        BOOLEAN  NOT NULL,
                            task_desc_html     VARCHAR  NOT NULL,
                            text_for_task_html VARCHAR  NOT NULL,
                            solution_html      VARCHAR  NOT NULL,
                            answer             VARCHAR  NOT NULL
);
"""
code_for_insert_data_in_table = (
    "INSERT INTO {} (task_section, id_task, "
    "is_detailed, task_desc_html, "
    "text_for_task_html, solution_html, answer) "
    "VALUES {} ON CONFLICT DO NOTHING"
)
code_for_getting_task = (
    "SELECT * FROM {} WHERE TASK_SECTION LIKE '{}' " "ORDER BY RANDOM() LIMIT 1;"
)
file_path = rf"{path_dir}\db\tasks_for_subjects.db"
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
