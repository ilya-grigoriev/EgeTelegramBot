"""This module help to check existing database."""
from logger_for_project import my_logger
from work_with_db.check_data.check_tables_db import check_existing_tables_db
from work_with_db.config_for_db import conn
from work_with_db.check_data.check_data_db import check_data_of_tables


def check_db() -> None:
    """Check PostgreSQL database (data from environment of Python)."""
    my_logger.info("Connect with postgres db...")
    check_existing_tables_db(conn=conn)
    check_data_of_tables(conn=conn)
    conn.close()


if __name__ == "__main__":
    check_db()
