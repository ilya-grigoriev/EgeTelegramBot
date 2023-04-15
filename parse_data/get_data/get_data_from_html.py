"""Module help to get data from html code."""
import re
from typing import List

from bs4 import BeautifulSoup


def get_tasks_html_from_html(*, html: str, n_issue: int) -> List[str]:
    """
    Get task html codes from html code.

    Parameters
    ----------
    html : str
        Html code.
    n_issue : int
        Number issue.

    Returns
    -------
    List[str]
        List of task html codes.
    """
    html = re.sub(r"\s{2,}", " ", html)
    soup = BeautifulSoup(html, "html.parser")
    tasks = soup.find_all("div", attrs={"class": "prob_maindiv"})
    formatted_tasks = [
        str(task) for task in tasks if f"Тип {n_issue} " in str(task)
    ]
    return formatted_tasks


def get_file_urls_from_html(*, html: str, template_url: str) -> str:
    """Get file urls from html code.

    Parameters
    ----------
    html : str
        Html code.
    template_url : str
        Template url for formatting internal links.

    Returns
    -------
    str
        String of formatted file urls for inserting into the database.
    """
    formatted_html = re.sub("'", '"', html)
    tags = re.findall(r'<a href="\/doc[\/\w\d\-_\.]+"', formatted_html)
    tags_2 = re.findall(r'<a href="\/get_file\?[\d\w=]+"', formatted_html)

    formatted_file_urls = []

    for tag in tags:
        url = re.search(r"\/doc[\/\w\d\-_\.]+", tag)
        if url:
            result_search = url.group()
            total_url = f"{template_url}{result_search}"
            formatted_file_urls.append(total_url)

    for tag in tags_2:
        url = re.search(r"\/get_file\?[\w\d=]+", tag)
        if url:
            result_search = url.group()
            total_url = f"{template_url}{result_search}"
            formatted_file_urls.append(total_url)
    return ", ".join(formatted_file_urls)


# if __name__ == "__main__":
#     html_code = open("tests/test.html", encoding="utf-8").read()
#     print(
#         get_file_urls_from_html(
#             html=html_code, template_url="https://inf-ege.sdamgia.ru"
#         )
#     )
