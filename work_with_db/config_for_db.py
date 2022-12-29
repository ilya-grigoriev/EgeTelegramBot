import os

from parse_data.config_for_parsing import path_dir

code_for_creating_table = """CREATE TABLE {} (
                            id_task        smallint NOT NULL UNIQUE,
                            level_name     VARCHAR  NOT NULL,
                            number_task    smallint NOT NULL,
                            html           VARCHAR  NOT NULL,
                            correct_answer VARCHAR  NOT NULL
);
"""
code_for_insert_data_in_table = "INSERT INTO {} (id_task, " \
                                "level_name, number_task, html, " \
                                "correct_answer) VALUES {}" \
                                " ON CONFLICT DO NOTHING"
code_for_get_task = "SELECT * FROM {} ORDER BY RANDOM() LIMIT 1;"
file_path = rf'{path_dir}\db\tasks_for_subjects.db'
USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')
HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')
