"""This module help to converting html"""
import os

from parse_data.config_for_parsing import path_dir
from parse_data.typing_for_parsing import (
    id_task_from_db,
    converted_image_to_bytes,
    converted_images,
)
from parse_data.browser_for_parsing import make_screenshot
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes


async def convert_html_code_to_image(
        *,
        html_code: str,
        id_task: id_task_from_db,
        type_html: str,
        is_created_images: converted_images = {},
) -> converted_image_to_bytes:
    """Converting html code to image.

    Parameters
    ----------
    html_code : str
        Html code in string.
    id_task: int
        Id_task column from database.
    type_html: str
        Part of the task (list of parts: 'task', 'text', 'solution', 'answer').
    is_created_images: dict
        Dictionary of already created images to save work time.
    """
    formatted_html = html_code
    file_path = f"{path_dir}\\{id_task}_{type_html}"
    html_file = f"{file_path}.html"
    jpg_file = f"{file_path}.jpg"
    try:
        if jpg_file not in is_created_images:
            is_created_images[jpg_file] = None
            with open(html_file, mode="w", encoding="utf-8") as file:
                file.write(formatted_html)

            await make_screenshot(
                file_path_for_open=html_file, file_path_for_save=jpg_file
            )
            os.remove(html_file)

            if os.path.isfile(jpg_file):
                converted_image = convert_image_to_bytes(file_name=jpg_file)
                os.remove(jpg_file)
                is_created_images[jpg_file] = converted_image
            else:
                return None
        else:
            # Checking converted image. Waiting if image is converted.
            if not is_created_images[jpg_file]:
                while True:
                    if os.path.isfile(jpg_file):
                        break
    finally:
        return is_created_images[jpg_file]
