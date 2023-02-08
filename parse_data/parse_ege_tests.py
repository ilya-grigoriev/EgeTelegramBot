"""Module help to parse tests from database."""
import asyncio

import psycopg2

from work_with_db.check_data.check_data_db import check_data_of_tables
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB


def parse_tasks():
    """Parse tasks from database."""
    conn = psycopg2.connect(
        dbname="subjects",
        user=USER_DB,
        password=PASSWORD_DB,
        host=HOST_DB,
        port=PORT_DB,
    )
    asyncio.run(check_data_of_tables(conn=conn))
