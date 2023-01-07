import asyncio
import traceback
from parse_data.typing_for_parsing import DataSubtopic, DataForTG, DataFromDB
from typing import Optional, List
import psycopg2
from logger_for_project import my_logger
from work_with_db.config_for_db import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB
from work_with_db.create_data.create_db_or_tables import create_tables
from work_with_db.config_for_db import code_for_getting_task


# async def select_tasks(*, subject: str) -> Optional[
#     List[DataForTG]]:
#     conn = None
#     cursor = None
#     try:
#         conn = psycopg2.connect(dbname='subjects', user=USER_DB,
#                                 password=PASSWORD_DB, host=HOST_DB,
#                                 port=PORT_DB)
#         cursor = conn.cursor()
#         cursor.execute(f"SELECT * FROM {subject}")
#         conn.commit()
#         tasks = cursor.fetchall()
#         formatted_tasks = []
#         for task in tasks:
#             if task:
#                 data = DataSubtopic(*task)
#                 formatted_data = await format_data_from_db(data=data)
#                 formatted_tasks.append(formatted_data)
#         return formatted_tasks
#     except psycopg2.errors.UndefinedTable:
#         my_logger.error(traceback.format_exc())
#         create_tables(conn=conn, tables_name=[subject])
#         my_logger.info(f'Table {subject} created')
#     except Exception as e:
#         my_logger.error(traceback.format_exc())
#     finally:
#         if conn:
#             cursor.close()
#             conn.close()


async def select_task(*, subject_name: str, task_section: str) -> Optional[DataFromDB]:
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            dbname="subjects",
            user=USER_DB,
            password=PASSWORD_DB,
            host=HOST_DB,
            port=PORT_DB,
        )
        cursor = conn.cursor()

        my_logger.info("Getting task from db...")
        request = code_for_getting_task.format(subject_name, task_section)
        cursor.execute(request)
        conn.commit()
        my_logger.success("Getting task is finished")

        task = cursor.fetchone()
        if task:
            data = DataFromDB(*task)
            return data
    except psycopg2.errors.UndefinedTable:
        my_logger.error(traceback.format_exc())
        create_tables(conn=conn, tables_name=[subject_name])
        my_logger.info(f"Table {subject_name} created")
    except Exception as e:
        my_logger.error(traceback.format_exc())
    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    resp = asyncio.run(select_task(subject_name="math", task_section="1/%"))
    if resp:
        print(resp)
