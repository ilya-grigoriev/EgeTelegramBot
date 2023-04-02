"""Module help to convert task."""
from typing import Optional, Sequence

import aiohttp
from parse_data.check.check_data import check_args
from parse_data.format.format_html import format_html_code
from parse_data.get_data.get_data_from_html import get_tasks_html_from_html
from parse_data.typing_for_parsing import DataTaskOfSubtopic
from tenacity import RetryError


async def get_tasks_from_html(
    *,
    html: str,
    template_url: str,
    session: aiohttp.ClientSession,
    n_issue: int,
    is_detailed: bool,
) -> Sequence[Optional[DataTaskOfSubtopic]]:
    """
    Convert tasks to dataclass subtopic's tasks.

    Parameters
    ----------
    html : str
        Html code.
    template_url : str
        Template url for formatting internal links.
    session : aiohttp.ClientSession
        Aiohttp client session.
    n_issue : int
        Number issue.
    is_detailed : bool
        Is the task with detailed answer?

    Returns
    -------
    Sequence[Optional[DataTaskOfSubtopic]]
        List of dataclass subtopic's tasks.
    """
    check_args(
        html=html,
        template_url=template_url,
        session=session,
        n_issue=n_issue,
        is_detailed=is_detailed,
    )

    tasks = get_tasks_html_from_html(html=html, n_issue=n_issue)
    formatted_tasks = []

    for task in tasks:
        try:
            formatted_task = await format_html_code(
                html_code=task,
                template_url=template_url,
                session=session,
                is_detailed=is_detailed,
            )
        except RetryError:
            formatted_task = None
        formatted_tasks.append(formatted_task)
    return formatted_tasks
