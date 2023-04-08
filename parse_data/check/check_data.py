"""Module is designed for checking data."""
import aiohttp
from parse_data import exceptions_for_parsing
from parse_data.check.check_data_object import (
    check_arg_data_from_db,
    check_arg_data_issue,
    check_arg_data_subtopic,
    check_arg_task,
)
from parse_data.check.check_html import check_arg_html
from parse_data.check.check_integer_args import (
    check_arg_id_task,
    check_arg_max_skip,
    check_arg_number_issue,
    check_arg_number_subtopic,
    check_arg_number_task,
)
from parse_data.check.check_path import (
    check_arg_file_name,
    check_arg_path_image,
    check_arg_path_pdf,
)
from parse_data.check.check_session import check_arg_session
from parse_data.check.check_subject_name import check_arg_subject_name
from parse_data.check.check_urls import check_arg_template_url, check_arg_url
from parse_data.config_for_parsing import list_types
from parse_data.typing_for_parsing import DataFromDB, Subtopic, typing_task


def check_args(**kwargs):
    """Check arguments in function."""
    if "html" in kwargs:
        html = kwargs["html"]
        check_arg_html(html=html)

    if "template_url" in kwargs:
        template_url = kwargs["template_url"]
        check_arg_template_url(template_url=template_url)

    if "session" in kwargs:
        session: aiohttp.ClientSession = kwargs["session"]  # type: ignore
        check_arg_session(session=session)

    if "n_issue" in kwargs:
        n_issue = kwargs["n_issue"]
        check_arg_number_issue(n_issue=n_issue)

    if "is_detailed" in kwargs:
        is_detailed = kwargs["is_detailed"]
        if not isinstance(is_detailed, bool):
            raise exceptions_for_parsing.WrongIsDetailed

    if "file_name" in kwargs:
        file_name = kwargs["file_name"]
        check_arg_file_name(file_name=file_name)

    if "data_subtopic" in kwargs:
        data_subtopic: Subtopic = kwargs["data_subtopic"]  # type: ignore
        check_arg_data_subtopic(data_subtopic=data_subtopic)

    if "subject_name_en" in kwargs:
        subject_name_en = kwargs["subject_name_en"]
        check_arg_subject_name(subject_name=subject_name_en)

    if "n_subtopic" in kwargs:
        n_subtopic = kwargs["n_subtopic"]
        check_arg_number_subtopic(n_subtopic=n_subtopic)

    if "type_html" in kwargs:
        type_html = kwargs["type_html"]
        if type_html not in list_types:
            raise exceptions_for_parsing.WrongTypeHtml

    if "data_from_db" in kwargs:
        data_from_db: DataFromDB = kwargs["data_from_db"]  # type: ignore
        check_arg_data_from_db(data_from_db=data_from_db)

    if "id_task" in kwargs:
        id_task = kwargs["id_task"]
        check_arg_id_task(id_task=id_task)

    if "path_pdf" in kwargs:
        path_pdf = kwargs["path_pdf"]
        check_arg_path_pdf(path_pdf=path_pdf)

    if "path_image" in kwargs:
        path_image = kwargs["path_image"]
        check_arg_path_image(path_image=path_image)

    if "url" in kwargs:
        url = kwargs["url"]
        check_arg_url(url=url)

    if "max_skip" in kwargs:
        max_skip = kwargs["max_skip"]
        check_arg_max_skip(max_skip=max_skip)

    if "task" in kwargs:
        task: typing_task = kwargs["task"]  # type: ignore
        check_arg_task(task=task)

    if "data_issues" in kwargs:
        data_issues = kwargs["data_issues"]
        for issue in data_issues:
            check_arg_data_issue(issue=issue)

    if "n_task" in kwargs:
        n_task = kwargs["n_task"]
        check_arg_number_task(n_task=n_task)
