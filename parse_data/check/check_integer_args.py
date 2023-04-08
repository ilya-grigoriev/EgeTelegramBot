"""Module is desinged for checking integer arguments."""
from parse_data import exceptions_for_parsing


def check_arg_max_skip(max_skip: int):
    """
    Check argument of max skip.

    Parameters
    ----------
    max_skip : int
    """
    try:
        if max_skip < 0:
            raise exceptions_for_parsing.WrongMaxSkip
    except TypeError:
        raise exceptions_for_parsing.WrongMaxSkip


def check_arg_id_task(id_task: int):
    """
    Check argument of id task.

    Parameters
    ----------
    id_task : int
    """
    try:
        if id_task < 0:
            raise exceptions_for_parsing.WrongIdTask
    except TypeError:
        raise exceptions_for_parsing.WrongIdTask


def check_arg_number_issue(n_issue: int):
    """
    Check argument of number issue.

    Parameters
    ----------
    n_issue : int
    """
    try:
        if n_issue <= 0:
            raise exceptions_for_parsing.WrongNumberIssue
    except TypeError:
        raise exceptions_for_parsing.WrongNumberIssue


def check_arg_number_subtopic(n_subtopic: int):
    """
    Check argument of number subtopic.

    Parameters
    ----------
    n_subtopic : int
    """
    try:
        if n_subtopic <= 0:
            raise exceptions_for_parsing.WrongNumberSubtopic
    except TypeError:
        raise exceptions_for_parsing.WrongNumberSubtopic


def check_arg_number_task(n_task: int):
    """
    Check argument of number subtopic.

    Parameters
    ----------
    n_subtopic : int
    """
    try:
        if n_task <= 0:
            raise exceptions_for_parsing.WrongNumberTask
    except TypeError:
        raise exceptions_for_parsing.WrongNumberTask
