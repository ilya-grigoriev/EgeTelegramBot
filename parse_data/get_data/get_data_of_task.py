"""This module help to get data of task for subtopic."""
import re
from typing import Tuple

from bs4 import BeautifulSoup
from parse_data.typing_for_parsing import DataTaskOfSubtopic


def get_data_of_task_for_subtopic(*, html: str) -> Tuple[str, DataTaskOfSubtopic]:
    """
    Get data of task for subtopic from html code.

    Parameters
    ----------
    html : str
        Html code.

    Returns
    -------
    Tuple[str, DataTaskOfSubtopic]
        Html code task and data of task is converted to dataclass.
    """
    soup = BeautifulSoup(html, "html.parser")
    task_html = soup.find("div", attrs={"class": "nobreak"})
    task_desc_html = task_html.find("div", attrs={"id": re.compile(r"body\d+")})
    task_desc_html = re.sub("'", '"', str(task_desc_html))
    text_for_task_html = ""
    searching = re.search(r'id="text\d+"', str(task_html))
    if searching:
        text_for_task_html = task_html.find("div", attrs={"id": re.compile(r"text\d+")})
    data_task_for_subtopic = DataTaskOfSubtopic(
        task_desc_html=str(task_desc_html), text_for_task_html=str(text_for_task_html)
    )
    return str(task_html), data_task_for_subtopic
