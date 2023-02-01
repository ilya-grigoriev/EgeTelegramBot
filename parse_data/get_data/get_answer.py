"""This module help to get answer task."""
import asyncio
import random
import re
import traceback
from typing import Optional, Tuple

from bs4 import BeautifulSoup
import aiohttp

from logger_for_project import my_logger
from parse_data.config_for_parsing import headers_for_request
from parse_data.format.format_data_in_tag import (
    format_table_in_html,
    format_answer_from_tag,
    delete_excess_data_in_tag,
)
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
    template_url: str
        Template url for formatting internal links.
    html_code:
        Html code.
    session: aiohttp.ClientSession
        Aiohttp client session.
    is_detailed: bool
        Is the task with detailed answer?

    Returns
    -------
    Optional[Tuple[str, str, int]]
        Solution html code, answer html code and task id.
    """

    bs = BeautifulSoup(html_code, "html.parser")
    num_and_id_task = bs.find("span", attrs={"class": "prob_nums"}).text
    _, id_task = tuple(map(lambda x: x.strip(), num_and_id_task.split("№")))
    total_url = f"{template_url}/problem?id={id_task}"

    while True:
        try:
            response = await session.get(total_url,
                                         headers=headers_for_request)
        except Exception:
            my_logger.error(traceback.format_exc())
        except (
                aiohttp.client_exceptions.ClientOSError,
                asyncio.TimeoutError,
                aiohttp.client_exceptions.ClientConnectorError,
        ):
            my_logger.error(traceback.format_exc())
            my_logger.info(f"Repeat request to {total_url}...")
            await asyncio.sleep(random.randint(0, 2))
        else:
            break

    if response.status != 200:
        return None
    html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    solution_html = soup.find("div", attrs={"id": f"sol{id_task}"})
    file_urls = get_file_urls_from_html(html=html, template_url=template_url)

    if solution_html:
        have_table = solution_html.find("table")
        answer_text = ""

        pattern = re.compile(r"Ответ:((?!<\/p>)[\w\W])*")
        answer_text_v1 = re.search(pattern, str(solution_html))

        answer_text_v2 = bs.find("div", attrs={"class": "answer"})

        if answer_text_v2:
            if is_detailed:
                formatted_answer = delete_excess_data_in_tag(
                    template_url=template_url, tag=str(answer_text_v2)
                )
                answer_text = formatted_answer
            else:
                answer_text_v2 = answer_text_v2.text
                if have_table:
                    solution_html = ""
                if "Ответ:" in answer_text_v2:
                    answer_text_v2 = ":".join(
                        answer_text_v2.split(":")[1:]).strip()
                answer_text = answer_text_v2
        elif answer_text_v1:
            solution_html, answer_text = format_answer_from_tag(
                html=str(solution_html))
            if have_table:
                solution_html = ""
        elif have_table:
            try:
                solution_html, answer_text = format_table_in_html(
                    html=solution_html)
            except Exception:
                my_logger.error(traceback.format_exc())
        solution_html_str = str(solution_html)
        if answer_text:
            return file_urls, solution_html_str, answer_text, id_task
        return None
    return None
