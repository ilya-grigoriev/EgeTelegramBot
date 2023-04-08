"""Module is designed for checking url."""
import re

from parse_data import exceptions_for_parsing


def check_arg_url(url: str):
    """
    Check argument of url.

    Parameters
    ----------
    url : str
    """
    try:
        pattern = r"http[s]?:\/\/[\w]+-ege\.sdamgia\.ru\/test\?theme=[\d]+"
        searching = re.search(pattern, url)
        searching.group()  # type: ignore
    except AttributeError:
        raise exceptions_for_parsing.WrongUrl


def check_arg_template_url(template_url: str):
    """
    Check argument of template url.

    Parameters
    ----------
    template_url : str
        By example, 'https://math-ege.sdamgia.ru'
    """
    try:
        pattern = r"https:\/\/[\w]+\-ege\.sdamgia\.ru"
        searching = re.search(pattern, template_url)
        searching.group()  # type: ignore
    except AttributeError:
        raise exceptions_for_parsing.WrongTemplateUrl
