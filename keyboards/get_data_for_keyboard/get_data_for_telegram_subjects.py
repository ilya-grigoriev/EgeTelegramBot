"""Module help to getting data for subjects."""
from typing import List

from parse_data.config_for_parsing import subjects_en
from parse_data.get_data.get_data_of_subject import get_json_of_data_subject
from parse_data.typing_for_parsing import DataTask, DataSubjectForTG


def get_subjects_data() -> List[DataSubjectForTG]:
    """Get data of subjects.

    Returns
    -------
    List[DataSubjectForTG]
        List of TypedDict with data of subject for Telegram.
    """
    data_for_tg = []
    for subject in subjects_en:
        issues = get_json_of_data_subject(subject_name_en=subject)

        if issues:
            converted_data = [DataTask(**issue) for issue in issues]
            formatted_data = [
                issue
                for issue in converted_data
                if issue.subtopics and issue.issue != 0
            ]

            subject_dict = {"title": subject, "issues": formatted_data}
            data_for_tg.append(DataSubjectForTG(**subject_dict))  # type: ignore
    return data_for_tg


if __name__ == "__main__":
    print(get_subjects_data())
