import tempfile

import html2image
from parse_data.format.format_html import format_html_code


def convert_html_code_to_image(*, html_code: str, name_fale: str) -> None:
    image = html2image.Html2Image()
    html_code = format_html_code(html_code=html_code)
    image.screenshot(html_str=html_code, save_as=f'tmp/{name_fale}.jpg')
