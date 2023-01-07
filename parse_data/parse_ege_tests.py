from parse_data.format.parse_data_and_update_database import \
    parse_data_and_update_db


def parse_tasks():
    parse_data_and_update_db(subject_name_en='rus')
    parse_data_and_update_db(subject_name_en='math')
