from parse_data.format.parse_data_and_update_database import \
    parse_data_and_update_db


def parse_tasks():
    parse_data_and_update_db(subject_name='Математика профильная',
                             n_tasks=1000)
    parse_data_and_update_db(subject_name='Русский язык',
                             n_tasks=1000)


if __name__ == '__main__':
    # parse_data_and_update_db(subject_name='Русский язык',
    #                          n_tasks=100)
    parse_data_and_update_db(subject_name='Математика профильная',
                             n_tasks=100)
