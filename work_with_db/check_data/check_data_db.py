"""This module help to check database."""
import asyncio
import random
import time
import traceback

import aiohttp.client_exceptions
import psycopg2.errors
from logger_for_project import my_logger
from parse_data.config_for_parsing import subjects_en
from parse_data.format.parse_data_and_update_database import parse_data_and_update_db


def check_data_of_tables(*, conn) -> None:
    """
    Check tables of database.

    Parameters
    ----------
    conn: psycopg2.connection
        Connection to PostgreSQL.
    """

    try:
        cursor = conn.cursor()
        for subject in subjects_en:
            my_logger.info(f"Selecting data. Subject: {subject}")
            cursor.execute(f"SELECT count(task_section) FROM {subject}")
            my_logger.success(f"Selecting data is finished. Subject: {subject}")
            if cursor.fetchone()[0] == 0:
                my_logger.info(f"Parsing for {subject}...")
                count_time = 5
                while True:
                    if count_time > 10:
                        break
                    try:
                        my_logger.info(f"Starting parsing data for {subject}")
                        asyncio.run(parse_data_and_update_db(subject_name_en=subject))
                        my_logger.success(f"Parsing data for {subject} is finished")
                    except aiohttp.client_exceptions.ClientError:
                        my_logger.error(traceback.format_exc())
                        my_logger.info(f"Repeat parsing data for {subject}...")

                        time.sleep(random.randint(3, count_time))
                        count_time += 2
                    else:
                        break
                my_logger.success(f"End parsing for {subject}")
            time.sleep(3)
    except psycopg2.errors.InFailedSqlTransaction:  # pylint: disable=no-member
        conn.rollback()
    except Exception:
        my_logger.error(traceback.format_exc())
