from typing import Tuple

from parse_data.typing_for_parsing import DataForDB


def format_data_from_db(*, data: tuple[str] | None) -> tuple[str, str, str]:
    total_text = ''
    if data is not None:
        data = DataForDB(*data)
        total_text += f"Уровень: {data.level_name}\n"
        if data.number_task != -1:
            total_text += f"Номер задания: {data.number_task}\n"

    return total_text, data.html, data.correct_answer
