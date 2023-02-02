"""This module help to format data for database."""
import re
from typing import List, Optional

from parse_data.typing_for_parsing import (
    DataIssue,
    typing_task,
    formatted_data_for_db,
)
from work_with_db.create_data.insert_data import insert_tasks


def format_data_for_db(
    *,
    task: typing_task,
    number_task: int,
    is_detailed: bool,
    number_subtopic: int,
) -> Optional[str]:
    """
    Format object DataTaskOfSubtopic for database.

    Parameters
    ----------
    task: typing_task
        Dataclass with data of the subtopic's task.
    number_task: int
        Number of the task.
    is_detailed: bool
        Is the task with detailed answer?
    number_subtopic: int
        Number of the subtopic.

    Returns
    -------
    Optional[str]
        Values for request for database.
    """

    total_request = None
    if task:
        task.task_desc_html = re.sub("'", '"', task.task_desc_html)
        task.text_for_task_html = re.sub("'", '"', task.text_for_task_html)
        task.solution_html = re.sub("'", '"', task.solution_html)

        if number_subtopic != -1:
            task_section = f"{number_task}/{number_subtopic}"
        else:
            task_section = f"{number_task}/0"
        total_request = f"('{task_section}', {task.id_task}, {str(is_detailed).lower()}, '{task.task_desc_html}', '{task.file_urls_for_task}', '{task.text_for_task_html}', '{task.solution_html}', '{task.answer}')"  # pylint: disable=line-too-long
    return total_request


async def format_and_insert_tasks(
    *, issues: List[DataIssue], subject_name_en: str
) -> None:
    """
    Format list of issues and insert them to database.

    Parameters
    ----------
    issues: List[DataIssue]
        List of issues.
    subject_name_en: str
        The name of the subject in English.
    """

    if issues:
        data_for_db: formatted_data_for_db = []
        for issue in issues:
            if issue.subtopics:
                for subtopic in issue.subtopics:
                    if subtopic:
                        for task in subtopic.tasks:
                            formatted_task = format_data_for_db(
                                task=task,
                                number_task=int(issue.number_issue),
                                is_detailed=issue.is_detailed,
                                number_subtopic=subtopic.ind_subtopic,
                            )
                            data_for_db.append(formatted_task)
        await insert_tasks(
            subject_name_en=subject_name_en, values_for_inserting=data_for_db
        )
