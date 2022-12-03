import os
import html2image
from parse_data.format.format_html import format_html_code
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes


def convert_html_code_to_image(*, html_code: str, file_name: str) -> bytes:
    image = html2image.Html2Image()
    html_code = format_html_code(html_code=html_code)
    file_name = f'{file_name}.jpg'
    image.screenshot(html_str=html_code, save_as=file_name)
    converted_image = convert_image_to_bytes(file_name=file_name)
    os.remove(file_name)
    return converted_image
