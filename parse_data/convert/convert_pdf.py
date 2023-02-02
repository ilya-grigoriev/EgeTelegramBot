"""This module help to converting pdf to other data."""
import os
import traceback

from pdf2image import convert_from_path

from logger_for_project import my_logger
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes
from parse_data.typing_for_parsing import typing_converted_images_to_bytes
from parse_data.format.format_image import crop_image
from parse_data.config_for_parsing import PATH_DIR


def convert_pdf_to_images(
    *, path_pdf_file: str, path_image: str
) -> typing_converted_images_to_bytes:
    """Converting pdf to images.

    Parameters
    ----------
    path_pdf_file: str
        Path existing pdf file.
    path_image: str
        Path existing image.
    Returns
    -------
    type_converted_images_to_bytes: Optional[List[bytes]]
        List of images converted to bytes.
    """

    path_for_poppler = rf"{PATH_DIR}\poppler-0.68.0\bin"
    images = convert_from_path(pdf_path=path_pdf_file, poppler_path=path_for_poppler)
    converted_images = []

    try:
        my_logger.info("Saving images...")
        for image in images:
            image.save(fp=path_image)

            my_logger.info("Start converting image to bytes...")
            converted_image = convert_image_to_bytes(file_name=path_image)
            my_logger.success("Converting image is finished")

            my_logger.info("Start cropping image...")
            image_without_empty_space = crop_image(image_to_bytes=converted_image)
            my_logger.success("Cropping image is finished")

            converted_images.append(image_without_empty_space)
        my_logger.success("Images saved")
    except Exception:  # pylint: disable=broad-except
        my_logger.error(traceback.format_exc())
    finally:
        if os.path.isfile(path_image):
            os.remove(path_image)

    return converted_images
