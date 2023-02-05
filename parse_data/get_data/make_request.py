"""This module help to make requests."""
import random
import traceback
from typing import Dict, Sequence, Optional, List
import asyncio
import aiohttp

from logger_for_project import my_logger
from parse_data.config_for_parsing import headers_for_get_data_tasks
from parse_data.typing_for_parsing import (
    typing_data_of_tasks,
    DataTaskOfSubtopic,
    typing_request_data,
)
from parse_data.convert.convert_task import get_tasks_from_html


async def request_to_url(
    *, url: str, data: Dict[str, str | int], n_issue: int, is_detailed: bool
) -> typing_data_of_tasks:
    """
    Make request to url.

    Parameters
    ----------
    url : str
    data : Dict[str, str | int]
        Data payload for request.
    n_issue : int
        Number issue.
    is_detailed : bool
        Is the task with detailed answer?

    Returns
    -------
    typing_data_of_tasks
        List of dataclass with data of subtopic's tasks.
    """
    time = 3
    session = aiohttp.ClientSession()
    while True:
        if time > 6:
            await session.close()
            return []
        try:
            template_url = url.rsplit("/", maxsplit=1)[0]
            headers_for_get_data_tasks.update({"Referer": url})
            headers_for_get_data_tasks.update({"Origin": template_url})

            response = await session.post(
                url, data=data, headers=headers_for_get_data_tasks
            )
        except (
            aiohttp.client_exceptions.ClientConnectorError,
            aiohttp.client_exceptions.ClientOSError,
        ):
            await session.close()
            my_logger.error(traceback.format_exc())
            my_logger.info(f"Repeat the request to {url}")
            await asyncio.sleep(random.randint(2, time))
            session = aiohttp.ClientSession()
            time += 2
        else:
            html = await response.text()
            if data.get("skip") == data.get("max_skip") and data:
                await session.close()
            elif "prob_maindiv" in html:
                formatted_html_codes = await get_tasks_from_html(
                    html=html,
                    template_url=template_url,
                    session=session,
                    n_issue=n_issue,
                    is_detailed=is_detailed,
                )
                await asyncio.sleep(random.randint(0, 2))
                await session.close()
                return formatted_html_codes
            else:
                await session.close()
            return [None]


async def main(
    *, urls_with_data: List[typing_request_data], n_issue: int, is_detailed: bool
) -> typing_data_of_tasks:
    """
    Run requests.

    Parameters
    ----------
    urls_with_data : List[typing_request_data]
        List of urls with data payload.
    n_issue : int
        Number issue.
    is_detailed : bool
        Is the task with detailed answer?

    Returns
    -------
    typing_data_of_tasks
        List of dataclass with data of subtopic's tasks.
    """
    async_requests = [
        request_to_url(
            url=url[0], data=url[1], n_issue=n_issue, is_detailed=is_detailed
        )
        for url in urls_with_data
    ]

    my_logger.info("Starting make requests...")
    tasks: Sequence[Sequence[Optional[DataTaskOfSubtopic]]] = await asyncio.gather(
        *async_requests
    )
    my_logger.success("Tasks received")

    formatted_tasks = []
    for data in tasks:
        if data:
            for html_code in data:
                if html_code:
                    formatted_tasks.append(html_code)
    return formatted_tasks
