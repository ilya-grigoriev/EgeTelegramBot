import os
from work_with_db.check_tables_db import check_existing_tables_db
from work_with_db.create_db_or_tables import create_db, create_tables
from work_with_db.config_for_db import file_path
from work_with_db.check_data_db import check_data_of_tables


def check_db():
    if os.path.isfile(file_path):
        check_existing_tables_db(file_path=file_path)
        check_data_of_tables(db_file_path=file_path)
    else:
        db_file_path = create_db()
        create_tables(db_file_path=db_file_path)


if __name__ == '__main__':
    check_db()
