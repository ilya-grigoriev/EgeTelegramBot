"""Module is designed for checking html code."""
import re

from parse_data import exceptions_for_parsing


def check_arg_html(html: str):
    """
    Check html code.

    Parametrs
    ---------
        html : str
    """
    try:
        pattern = r"<\w+>[\w\d:;\.,\+\*\w\-А-Яа-яё]+<\/\w+>"
        searching = re.search(pattern, html)
        if searching:
            searching.group()
    except Exception:
        raise exceptions_for_parsing.WrongHtmlCode
