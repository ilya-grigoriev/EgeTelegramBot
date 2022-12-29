import asyncio
import traceback
from parse_data.typing_for_parsing import DataForDB, DataForTG
from typing import Optional, List
import psycopg2
from loguru import logger
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB
from parse_data.format.format_data_from_database import format_data_from_db
from work_with_db.create_data.create_db_or_tables import create_tables
from work_with_db.config_for_db import code_for_get_task


async def select_tasks(*, subject: str) -> Optional[List[DataForTG]]:
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(dbname='subjects', user=USER_DB,
                                password=PASSWORD_DB, host=HOST_DB,
                                port=PORT_DB)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {subject}")
        conn.commit()
        tasks = cursor.fetchall()
        formatted_tasks = []
        for task in tasks:
            if task:
                data = DataForDB(*task)
                formatted_data = await format_data_from_db(data=data)
                formatted_tasks.append(formatted_data)
        return formatted_tasks
    except psycopg2.errors.UndefinedTable:
        logger.error(traceback.format_exc())
        create_tables(conn=conn, tables_name=[subject])
        logger.info(f'Table {subject} created')
    except Exception as e:
        logger.error(traceback.format_exc())
    finally:
        if conn:
            cursor.close()
            conn.close()


async def select_task(*, subject: str) -> Optional[DataForTG]:
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(dbname='subjects', user=USER_DB,
                                password=PASSWORD_DB, host=HOST_DB,
                                port=PORT_DB)
        cursor = conn.cursor()
        cursor.execute(code_for_get_task.format(subject))
        conn.commit()
        task = cursor.fetchone()
        if task:
            data = DataForDB(*task)
            formatted_data = await format_data_from_db(data=data)
            return formatted_data
        return None
    except psycopg2.errors.UndefinedTable:
        logger.error(traceback.format_exc())
        create_tables(conn=conn, tables_name=[subject])
        logger.info(f'Table {subject} created')
    except Exception as e:
        logger.error(traceback.format_exc())
    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    resp = asyncio.run(select_task(subject='math'))
    if resp:
        print(resp)
