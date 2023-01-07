import asyncio
import random
import re
import traceback

from bs4 import BeautifulSoup
import aiohttp

from logger_for_project import my_logger
from parse_data.config_for_parsing import headers_for_request
from parse_data.format.format_data_in_tag import (
    format_table_in_html,
    format_answer_from_tag,
    delete_excess_data_in_tag,
)


async def get_answer_task(
    *,
    template_url: str,
    html_code: str,
    session: aiohttp.ClientSession,
    is_detailed: str,
) -> str:
    bs = BeautifulSoup(html_code, "html.parser")
    num_and_id_task = bs.find("span", attrs={"class": "prob_nums"}).text
    num_task, id_task = map(lambda x: x.strip(), num_and_id_task.split("№"))
    total_url = f"{template_url}/problem?id={id_task}"

    while True:
        try:
            response = await session.get(total_url, headers=headers_for_request)
        except Exception as e:
            my_logger.error(traceback.format_exc())
        except aiohttp.client_exceptions.ClientOSError or asyncio.TimeoutError:
            my_logger.error(traceback.format_exc())
            my_logger.info(f"Repeat request to {total_url}...")
            await asyncio.sleep(random.randint(0, 2))
        else:
            break

    if response.status != 200:
        return None
    html = await response.text()

    bs = BeautifulSoup(html, "html.parser")
    solution_html = bs.find("div", attrs={"id": f"sol{id_task}"})

    if solution_html:
        have_table = solution_html.find("table")
        answer_text = ""

        pattern = re.compile("Ответ:((?!<\/p>)[\w\W])*")
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
                    answer_text_v2 = ":".join(answer_text_v2.split(":")[1:]).strip()
                answer_text = answer_text_v2
        elif answer_text_v1:
            solution_html, answer_text = format_answer_from_tag(html=str(solution_html))
            if have_table:
                solution_html = ""
        elif have_table:
            try:
                solution_html, answer_text = format_table_in_html(html=solution_html)
            except Exception as e:
                my_logger.error(traceback.format_exc())
        solution_html = str(solution_html)
        return solution_html, answer_text, id_task if answer_text else None
    return None
