"""Module help to get json of data subject."""
import traceback

from typing import Any
import requests
from logger_for_project import my_logger
from parse_data.typing_for_parsing import typing_data_subjects
from parse_data.config_for_parsing import headers_for_get_subject_ids


def get_json_of_data_subject(
    *, subject_name_en: str
) -> typing_data_subjects | Any:
    """Get json of data subject.

    Parameters
    ----------
    subject_name_en : str
        The name of the subject in English.

    Returns
    -------
    data_subjects
        Json of data subjects.
    """
    url = f"https://{subject_name_en}-ege.sdamgia.ru/newapi/general"
    headers_for_get_subject_ids.update(
        {"authority": f"{subject_name_en}-ege.sdamgia.ru"}
    )

    try:  # pylint: disable=no-else-return
        response = requests.get(
            url, headers=headers_for_get_subject_ids, timeout=5
        )
    except requests.exceptions.ReadTimeout:
        my_logger.error(traceback.format_exc())
        return None
    else:
        if response.status_code == 200:
            my_logger.info("Get subject ids from json")
            data_subject = response.json().get("constructor")
            my_logger.info("Data received")
            return data_subject
        my_logger.error(f"Connection is failed. URL: {url}")
        return None
