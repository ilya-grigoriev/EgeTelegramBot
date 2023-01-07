import os


def get_path_for_file(*, path_dir_file: str) -> str:
    par_dir = os.path.dirname(f"{os.path.dirname(__file__)}")
    ind_last_backslash = par_dir.rindex("\\")
    par_dir = par_dir[:ind_last_backslash]
    path = os.path.join(par_dir, rf"{path_dir_file}")
    return path


if __name__ == "__main__":
    print(get_path_for_file(path_dir_file=r"db\tasks_for_subjects.db"))
