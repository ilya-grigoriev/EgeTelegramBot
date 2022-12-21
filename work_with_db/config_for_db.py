from parse_data.config_for_parsing import path_dir

code_for_creating_tables = """CREATE TABLE {} (
    id             INTEGER PRIMARY KEY AUTOINCREMENT
                           NOT NULL
                           UNIQUE,
    id_task        INTEGER NOT NULL
                           UNIQUE,
    level_name     TEXT    NOT NULL,
    number_task    INTEGER NOT NULL,
    html           TEXT    NOT NULL,
    correct_answer TEXT    NOT NULL
);
"""

file_path = rf'{path_dir}\db\tasks_for_subjects.db'
