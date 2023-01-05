from typing import List, Optional

from parse_data.typing_for_parsing import DataTask


def get_data_subject_from_json(*, data_subject) -> Optional[List[DataTask]]:
    formatted_data = []
    if data_subject:
        for task in data_subject:
            data = DataTask(**task)
            if data.issue != 0:
                formatted_data.append(data)
            else:
                break
        return formatted_data
    return None
