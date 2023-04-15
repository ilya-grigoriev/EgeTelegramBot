"""Module is designed for checking arguments dataclass object."""
from parse_data import exceptions_for_parsing
from parse_data.typing_for_parsing import (
    DataFromDB,
    DataIssue,
    Subtopic,
    typing_task,
)


def check_arg_data_subtopic(data_subtopic: Subtopic) -> None:
    """
    Check dataclass arguments Subtopic.

    Parameters
    ----------
    data_subtopic : Subtopic
    """
    try:
        data_subtopic.json()
    except Exception:
        raise exceptions_for_parsing.WrongSubtopicDataclass


def check_arg_data_from_db(data_from_db: DataFromDB):
    """
    Check dataclass arguments DataFromDB.

    Parametrs
    ---------
        data_from_db : DataFromDB
    """
    try:
        data_from_db.task_section
    except Exception:
        raise exceptions_for_parsing.WrongDataFromDBDataclass


def check_arg_task(task: typing_task):
    """
    Check dataclass arguments DataTaskOfSubtopic.

    Parametrs
    ---------
        task : typing_task
    """
    if task:
        try:
            task.id_task
        except Exception:
            raise exceptions_for_parsing.WrongTaskDataclass


def check_arg_data_issue(issue: DataIssue):
    """
    Check dataclass arguments DataIssue.

    Parameters
    ----------
        issue : DataIssue
    """
    if issue:
        try:
            issue.subtopics
        except Exception:
            raise exceptions_for_parsing.WrongDataIssue
