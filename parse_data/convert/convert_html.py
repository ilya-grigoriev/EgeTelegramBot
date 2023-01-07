"""This module help to converting html"""
import asyncio
import os

from logger_for_project import my_logger
from parse_data.config_for_parsing import path_dir
from parse_data.typing_for_parsing import (
    id_task_from_db,
    converted_images_to_bytes,
    type_converted_images,
)
from parse_data.browser_for_parsing import make_pdf
from parse_data.convert.convert_pdf import convert_pdf_to_images


async def convert_html_code_to_image(
        *,
        html_code: str,
        id_task: id_task_from_db,
        type_html: str,
        is_created_pdf_files: type_converted_images = {},
) -> converted_images_to_bytes:
    """Converting html code to image.

    Parameters
    ----------
    html_code : str
        Html code in string.
    id_task: int
        Id_task column from database.
    type_html: str
        Part of the task (list of parts: 'task', 'text', 'solution', 'answer').
    is_created_pdf_files: dict
        Dictionary of already created pdf files to save work time.
    """
    formatted_html = html_code
    file_path = f"{path_dir}\\{id_task}_{type_html}"
    html_file = f"{file_path}.html"
    pdf_file = f"{file_path}.pdf"
    jpg_file = f"{file_path}.jpg"
    try:
        if pdf_file not in is_created_pdf_files:
            is_created_pdf_files[pdf_file] = None

            with open(html_file, mode="w", encoding="utf-8") as file:
                file.write(formatted_html)

            await make_pdf(file_path_for_open=html_file,
                           file_path_for_save=pdf_file)
            os.remove(html_file)

            if os.path.isfile(pdf_file):
                my_logger.info('Converting pdf to images...')
                converted_images = convert_pdf_to_images(
                    path_pdf_file=pdf_file, path_image=jpg_file)
                my_logger.success('Converting pdf is finished')

                os.remove(pdf_file)
                is_created_pdf_files[pdf_file] = converted_images
            else:
                return None
        else:
            # Checking converted image. Waiting if image is converted.
            if not is_created_pdf_files[pdf_file]:
                while True:
                    if os.path.isfile(pdf_file):
                        break
    finally:
        return is_created_pdf_files[pdf_file]


if __name__ == '__main__':
    html_code = open('tests/test.html', encoding='utf-8').read()
    asyncio.run(convert_html_code_to_image(html_code=html_code, id_task=0,
                                           type_html='text'))
