import random
import traceback
from typing import Dict

from logger_for_project import my_logger
from parse_data.config_for_parsing import headers_for_get_data_tasks
import aiohttp
import asyncio
from parse_data.format.format_html import format_html_code
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.get_data.get_answer import get_answer_task
from parse_data.typing_for_parsing import DataTaskOfSubtopic
from parse_data.get_data.get_data_from_html import get_tasks_from_html


async def request_to_url(
    *, url: str, data: Dict[str, str | int], n_issue: int, is_detailed: str
):
    time = 2
    session = aiohttp.ClientSession()
    while True:
        if time > 5:
            await session.close()
            return []
        try:
            template_url = url.rsplit("/", maxsplit=1)[0]
            headers_for_get_data_tasks.update({"Referer": url})
            headers_for_get_data_tasks.update({"Origin": template_url})

            response = await session.post(
                url, data=data, headers=headers_for_get_data_tasks
            )
        except aiohttp.client_exceptions.ClientConnectorError:
            await session.close()
            my_logger.error(traceback.format_exc())
            my_logger.info(f"Repeat the request to {url}")
            await asyncio.sleep(random.randint(0, time))
            session = aiohttp.ClientSession()
            time += 2
        else:
            html = await response.text()
            if "prob_maindiv" in html:
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
            elif data["skip"] == data["max_skip"]:
                await session.close()
                return None


async def main(*, urls_with_data, n_issue: int, is_detailed: str):
    async_requests = [
        request_to_url(
            url=url[0], data=url[1], n_issue=n_issue, is_detailed=is_detailed
        )
        for url in urls_with_data
    ]

    my_logger.info("Starting make requests...")
    tasks = await asyncio.gather(*async_requests)
    my_logger.success("Tasks received")

    formatted_tasks = []
    for data in tasks:
        if data:
            for html_code in data:
                if html_code:
                    formatted_tasks.append(html_code)
    return formatted_tasks


if __name__ == "__main__":
    tasks = [
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 5}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 8}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 11}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 14}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 17}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 20}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 23}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 26}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 29}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 32}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 35}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 38}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 41}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 44}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 47}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 50}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 53}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 56}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 59}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 62}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 65}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 68}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 71}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 74}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 77}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 80}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 83}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 86}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 89}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 92}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 95}),
        ("https://math-ege.sdamgia.ru/test?theme=79", {"ajax": "1", "skip": 98}),
    ]
    print(asyncio.get_event_loop().run_until_complete(main(urls_with_data=tasks)))
