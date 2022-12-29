from typing import Tuple, Optional
from parse_data.convert.convert_html import convert_html_code_to_image
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes
from parse_data.typing_for_parsing import DataForDB, DataForTG


async def format_data_from_db(*, data: Optional[DataForDB]) -> Optional[
    DataForTG]:
    if data:
        total_text = ''
        file_path = ''
        total_text += f"Уровень: {data.level_name}\n"
        if data.number_task != -1:
            total_text += f"Номер задания: {data.number_task}\n"
        converted_image = await convert_html_code_to_image(html_code=data.html,
                                                           id_task=data.id_task)

        if converted_image:
            return DataForTG(total_text, data.id_task, data.correct_answer,
                             file_path, converted_image)
        else:
            return None
    return None
