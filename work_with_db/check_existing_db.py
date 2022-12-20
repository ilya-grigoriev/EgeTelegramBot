import os
from parse_data.config_for_parsing import path_dir


def check_db() -> bool:
    file_path = rf'{path_dir}\db\tasks_for_subjects.db'
    return os.path.isfile(file_path)


if __name__ == '__main__':
    print(check_db())
