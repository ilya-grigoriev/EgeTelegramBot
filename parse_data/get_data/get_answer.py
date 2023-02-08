"""This module help to get answer task."""
import asyncio
import random
import traceback
from typing import Optional, Tuple

from bs4 import BeautifulSoup
import aiohttp

from logger_for_project import my_logger
from parse_data.config_for_parsing import headers_for_request
from parse_data.format.format_data_in_tag import format_solution_html
from parse_data.get_data.get_data_from_html import get_file_urls_from_html


async def get_answer_task(
    *,
    template_url: str,
    html_code: str,
    session: aiohttp.ClientSession,
    is_detailed: bool,
) -> Optional[Tuple[str, str, str, int]]:
    """
    Get answer task from html code.

    Parameters
    ----------
    template_url : str
        Template url for formatting internal links.
    html_code:
        Html code.
    session : aiohttp.ClientSession
        Aiohttp client session.
    is_detailed : bool
        Is the task with detailed answer?

    Returns
    -------
    Optional[Tuple[str, str, int]]
        Solution html code, answer html code and task id.
    """

    soup = BeautifulSoup(html_code, "html.parser")
    num_and_id_task = soup.find("span", attrs={"class": "prob_nums"}).text
    _, id_task = tuple(map(lambda x: x.strip(), num_and_id_task.split("№")))
    total_url = f"{template_url}/problem?id={id_task}"

    while True:
        try:
            response = await session.get(total_url, headers=headers_for_request)
        except (
            aiohttp.client_exceptions.ClientOSError,
            asyncio.TimeoutError,
            aiohttp.client_exceptions.ClientConnectorError,
        ):
            my_logger.error(traceback.format_exc())
            my_logger.info(f"Repeat request to {total_url}...")
            await asyncio.sleep(random.randint(0, 2))
        except Exception:  # pylint: disable=broad-except
            my_logger.error(traceback.format_exc())
        else:
            break

    if response.status != 200:
        return None
    html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    solution_html = soup.find("div", attrs={"id": f"sol{id_task}"})
    file_urls = get_file_urls_from_html(html=html, template_url=template_url)
    answer_text = ""

    if solution_html:
        formatting_solution = format_solution_html(
            solution_html=solution_html,
            soup=soup,
            template_url=template_url,
            is_detailed=is_detailed,
        )
        if formatting_solution:
            solution_html, answer_text = formatting_solution
        return file_urls, solution_html, answer_text, id_task
    return None
