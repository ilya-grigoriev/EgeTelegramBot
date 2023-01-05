import asyncio
import re
from typing import List, Optional

import aiohttp
from bs4 import BeautifulSoup
from parse_data.format.format_html import format_html_code
from parse_data.typing_for_parsing import DataTaskOfSubtopic


def get_task_urls_from_html(*, html, n_issue: int) -> List[str]:
    html = re.sub('\s{2,}', ' ', html)
    bs = BeautifulSoup(html, 'html.parser')
    tasks = bs.find_all('div', attrs={'class': 'prob_maindiv'})
    formatted_tasks = [str(task) for task in tasks if
                       f'Тип {n_issue} ' in str(task)]
    return formatted_tasks


async def get_tasks_from_html(*, html: str, template_url: str,
                              session: aiohttp.ClientSession, n_issue: int,
                              is_detailed: str) -> List[
    Optional[DataTaskOfSubtopic]]:
    tasks = get_task_urls_from_html(html=html, n_issue=n_issue)
    formatted_tasks = []

    for task in tasks:
        formatted_task = await format_html_code(html_code=task,
                                                template_url=template_url,
                                                session=session,
                                                is_detailed=is_detailed)
        formatted_tasks.append(formatted_task)
    return formatted_tasks
