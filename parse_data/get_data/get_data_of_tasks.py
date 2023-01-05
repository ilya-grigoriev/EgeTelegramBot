import asyncio
import copy
import time

import aiohttp

from logger_for_project import my_logger
from parse_data.typing_for_parsing import data_from_json
from typing import Any
from parse_data.create_data.create_urls import create_urls_for_request
from parse_data.get_data import make_request


async def get_data_of_tasks_for_subtopic(*, urls, n_issue: int,
                                         is_detailed: str):
    tasks = await make_request.main(urls_with_data=urls, n_issue=n_issue,
                                    is_detailed=is_detailed)
    return tasks
