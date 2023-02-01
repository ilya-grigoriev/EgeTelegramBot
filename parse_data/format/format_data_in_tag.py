"""This module help to format data in html code."""
import re
from typing import Tuple


def delete_excess_data_in_tag(*, template_url: str, tag: str) -> str:
    """
    Delete excess data from html code.

    Parameters
    ----------
    template_url: str
        Template url for formatting internal links.
    tag: str
        Html code.

    Returns
    -------
    str
        Formatting html code.
    """

    tag = re.sub(r"\s{2,}", " ", tag)
    tag = re.sub("'", '"', tag)

    sources = re.findall(r'src="[\w\d\-\.\/\?=]+"', tag)
    for source in sources:
        url = source.lstrip('src="').rstrip('"')
        if url:
            total_url = f"{template_url}{url}"
            new_source = f'src="{total_url}"'
            source = re.sub(r"\?", "\\?", source)
            source = re.sub(r"\.", "\\.", source)
            tag = re.sub(source, new_source, tag)

    tag = re.sub(r'<body (class="[\w\-\s]+")', '<body bgcolor="#f5f5f5"', tag)

    tag = re.sub(r"<input[\w\s\dА-Яа-яЁё=\"_\\]+>", "", tag)

    pattern = (
        r'<script language="javascript"> ShowPictureQ\([\w\d\/_\.\"]+\);<\/script>'
    )
    sources = re.findall(pattern, tag)
    pattern_for_href = (
        r"(docs\/[\d\w]+\/[\d\w]+\/[\d\w]+\/[\d\w]+\.(png|jpg|gif|jpeg|webp|svg))"
    )
    for source in sources:
        result_search = re.search(pattern_for_href, source)
        if result_search:
            href = result_search.group()
            source = re.sub(r"/", r"\/", source)
            source = re.sub(r"\(", r"\(", source)
            source = re.sub(r"\)", r"\)", source)
            source = re.sub(r"\.", r"\.", source)
            image = f'<img src="http://os.fipi.ru/{href}">'
            tag = re.sub(source, image, tag)

    tag = re.sub("'", '"', tag)

    return tag


def format_table_in_html(*, html) -> Tuple[str, str]:
    """
    Format tag table in html code.

    Parameters
    ----------
    html: str
        Html code.

    Returns
    -------
    Tuple[str, str]
        Solution text without information and answer text.
    """

    answer = []
    table_with_answer = html.find_all("tr")[-1]
    for number in table_with_answer.find_all("td"):
        answer.append(str(number.text).strip())
    return "", "".join(answer)


def format_answer_from_tag(*, html: str) -> Tuple[str, str]:
    """
    Format answer from html code.

    Parameters
    ----------
    html: str
        Html code.

    Returns
    -------
    Tuple[str, str]
        Solution text and answer text.
    """
    pattern = re.compile(r"Ответ:((?!<\/p>)[\w\W])*")
    tag_answer = re.search(pattern, html)
    solution_html = ""
    answer_text = ""
    if tag_answer:
        result_search = tag_answer.group()
        formatted_result = re.sub(r"</span>", "", result_search)
        formatted_result = re.sub(r"<p>", "", formatted_result)
        solution_html = re.sub("'", '"', html)
        if formatted_result:
            _, *answer = formatted_result.split(":")
            answer_text = " ".join(answer)
            answer_text = answer_text.strip().strip(".")
    return solution_html, answer_text.strip()
