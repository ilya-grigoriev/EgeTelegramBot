import asyncio

import psycopg2

from work_with_db.check_data.check_data_db import check_data_of_tables
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB


def parse_tasks():
    conn = psycopg2.connect(
        dbname="subjects",
        user=USER_DB,
        password=PASSWORD_DB,
        host=HOST_DB,
        port=PORT_DB,
    )
    asyncio.run(check_data_of_tables(conn=conn))
