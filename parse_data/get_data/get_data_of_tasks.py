"""This module help to get data of tasks for subtopic."""
from parse_data.get_data import make_request
from parse_data.typing_for_parsing import typing_urls_with_data, typing_data_of_tasks


async def get_data_of_tasks_for_subtopic(
    *, urls: typing_urls_with_data, n_issue: int, is_detailed: bool
) -> typing_data_of_tasks:
    """
    Get data of tasks for subtopic.

    Parameters
    ----------
    urls : typing_request_data
        Request data (url, data payload).
    n_issue : int
        Number issue.
    is_detailed : bool
        Is the task with detailed answer?

    Returns
    -------
    typing_data_of_task
        List of dataclass with data of tasks.
    """
    tasks = await make_request.main(
        urls_with_data=urls, n_issue=n_issue, is_detailed=is_detailed
    )
    return tasks
