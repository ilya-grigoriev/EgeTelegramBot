"""This module help to format html code."""
import asyncio
import random
import traceback
from typing import Optional, Any

import aiohttp
from tenacity import retry, wait_fixed, stop_after_attempt
from logger_for_project import my_logger
from parse_data.typing_for_parsing import DataTaskOfSubtopic
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.get_data.get_answer import get_answer_task
from parse_data.get_data.get_data_of_task import get_data_of_task_for_subtopic


@retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
async def format_html_code(
    *,
    html_code: str,
    template_url: str,
    session: aiohttp.ClientSession,
    is_detailed: bool
) -> Optional[DataTaskOfSubtopic] | Any:
    """
    Parse tasks from html code and formatting them.

    Parameters
    ----------
    html_code: str
        Html code.
    template_url: str
        Template url for formatting internal links.
    session: aiohttp.ClientSession
        Aiohttp client session.
    is_detailed: bool
        Is the task with detailed answer?

    Returns
    -------
    Optional[DataTaskOfSubtopic] | Any
        Dataclass with data of subtopic's task.
    """

    my_logger.info("Format html code...")
    formatted_html = delete_excess_data_in_tag(template_url=template_url, tag=html_code)
    my_logger.success("Html code formatted")

    my_logger.info("Getting data of task...")
    task_html, data_task = get_data_of_task_for_subtopic(html=formatted_html)
    my_logger.success("Getting data is finished")

    my_logger.info("Get solution for task...")
    time = 2
    while True:
        if time > 5:
            return None
        try:
            response = await get_answer_task(
                template_url=template_url,
                html_code=task_html,
                session=session,
                is_detailed=is_detailed,
            )
        except Exception:  # pylint: disable=broad-except
            my_logger.error(traceback.format_exc())
            return None
        else:
            if not response:
                my_logger.info("Repeat request...")
                await asyncio.sleep(random.randint(0, time))
                time += 2
            else:
                break

    my_logger.success("Solution received")

    if formatted_html and response:
        file_urls, solution_html, answer_text, id_task = response
        if id_task and isinstance(answer_text, str):
            data_task.id_task = int(id_task)
            data_task.solution_html = solution_html
            data_task.answer = answer_text
            data_task.file_urls_for_task = file_urls
            return data_task
    return None
