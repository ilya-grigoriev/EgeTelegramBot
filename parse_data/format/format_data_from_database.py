from typing import Tuple
from parse_data.convert.convert_html import convert_html_code_to_image

from parse_data.typing_for_parsing import DataForDB


def format_data_from_db(*, data: tuple[str] | None) -> tuple[str, int, str]:
    total_text = ''
    if data is not None:
        data = DataForDB(*data)
        total_text += f"Уровень: {data.level_name}\n"
        if data.number_task != -1:
            total_text += f"Номер задания: {data.number_task}\n"
        convert_html_code_to_image(html_code=data.html, id_task=data.id_task)

    return total_text, data.id_task, data.correct_answer
