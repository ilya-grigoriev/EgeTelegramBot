import psycopg2

from logger_for_project import my_logger
from work_with_db.check_data.check_tables_db import check_existing_tables_db
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB
from work_with_db.check_data.check_data_db import check_data_of_tables


def check_db():
    my_logger.info("Connect with postgres db...")
    conn = psycopg2.connect(
        dbname="subjects",
        user=USER_DB,
        password=PASSWORD_DB,
        host=HOST_DB,
        port=PORT_DB,
    )
    check_existing_tables_db(conn=conn)
    check_data_of_tables(conn=conn)
    conn.close()


if __name__ == "__main__":
    check_db()
