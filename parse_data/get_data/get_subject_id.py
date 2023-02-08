"""Module help to get subject id."""
from parse_data.typing_for_parsing import (
    DataTask,
    typing_data_subjects,
    formatted_subjects,
)


def get_data_subject_from_json(
    *, data_subjects: typing_data_subjects
) -> formatted_subjects:
    """Get list of dataclass with data of tasks.

    Parameters
    ----------
    data_subjects : typing_data_subjects
        List of data of subjects.

    Returns
    -------
    formatted_data_subjects
        List of dataclass with data of subjects.
    """
    formatted_data = []
    if data_subjects:
        for task in data_subjects:
            data = DataTask(**task)
            if data.issue != 0:
                formatted_data.append(data)
            else:
                break
        return formatted_data
    return None
