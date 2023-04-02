"""Module help to converting html."""
import os
import traceback

import aiocache
from aiocache.serializers import PickleSerializer
from logger_for_project import my_logger
from parse_data.browser_for_parsing import make_pdf
from parse_data.check.check_data import check_args
from parse_data.config_for_parsing import PATH_DIR
from parse_data.convert.convert_pdf import convert_pdf_to_images
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.typing_for_parsing import DataFromDB, typing_converted_images_to_bytes


@aiocache.cached(serializer=PickleSerializer())
async def convert_html_code_to_image(
    *, html_code: str, id_task: int, type_html: str
) -> typing_converted_images_to_bytes:
    """
    Convert html code to image.

    Parameters
    ----------
    html_code : str
        Html code in string.
    id_task : int
        Id_task column from database.
    type_html : str
        Part of the task (list of parts: 'task', 'text', 'solution', 'answer').

    Returns
    -------
    converted_images_to_bytes : Optional[List[bytes]]
        List of images converted to bytes.
    """
    check_args(html=html_code, id_task=id_task, type_html=type_html)

    formatted_html = html_code
    file_path = f"{PATH_DIR}\\{id_task}_{type_html}"
    html_file = f"{file_path}.html"
    pdf_file = f"{file_path}.pdf"
    jpg_file = f"{file_path}.jpg"
    count = 0

    while True:
        try:
            if count == 3:
                break

            with open(html_file, mode="w", encoding="utf-8") as file:
                file.write(formatted_html)

            await make_pdf(file_path_for_open=html_file, file_path_for_save=pdf_file)

            os.remove(html_file)
        except Exception:
            my_logger.error(traceback.format_exc())
            my_logger.error(f"Html file: {html_file}. Pdf file: {pdf_file}.")
            count += 1
        else:
            break

    try:
        if os.path.isfile(pdf_file):
            my_logger.info("Converting pdf to images...")
            converted_images = convert_pdf_to_images(
                path_pdf_file=pdf_file, path_image=jpg_file
            )
            my_logger.success("Converting pdf is finished")

            os.remove(pdf_file)

            return converted_images
    except Exception:
        my_logger.error(traceback.format_exc())
    return None


async def convert_html_code_to_bytes(
    *, html_code: str, type_html: str, data: DataFromDB, template_url: str
) -> typing_converted_images_to_bytes:
    """
    Convert html code to list of images is converted to bytes.

    Parameters
    ----------
    html_code : str
        Html code.
    type_html : str
        Part of the task (list of parts: 'task', 'text', 'solution', 'answer').
    data : DataFromDB
        Dataclass with data from database.
    template_url : str
        Template url for formatting internal links.

    Returns
    -------
    Optional[List[IO[bytes]]]
        List of images is converted to bytes.
    """
    check_args(
        html=html_code,
        type_html=type_html,
        data_from_db=data,
        template_url=template_url,
    )

    if type_html == "answer":
        converted_text_to_html = f"<p>Ответ: {data.answer}</p>"
    else:
        converted_text_to_html = html_code

    formatted_html = delete_excess_data_in_tag(
        template_url=template_url, tag=converted_text_to_html
    )
    images = await convert_html_code_to_image(
        html_code=formatted_html,
        type_html=type_html,
        id_task=data.id_task,
    )
    return images  # type: ignore
