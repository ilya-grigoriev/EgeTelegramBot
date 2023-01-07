import os
import traceback

from pdf2image import convert_from_path

from logger_for_project import my_logger
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes


def convert_pdf_to_images(*, path_pdf_file: str, path_image: str):
    images = convert_from_path(pdf_path=path_pdf_file)
    converted_images = []

    try:
        my_logger.info('Saving images...')
        for image in images:
            image.save(fp=path_image)
            converted_image = convert_image_to_bytes(file_name=path_image)
            converted_images.append(converted_image)
        my_logger.success('Images saved')
    except Exception as e:
        my_logger.error(traceback.format_exc())
    finally:
        os.remove(path_image)
        return converted_images
