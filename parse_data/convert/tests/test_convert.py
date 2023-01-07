from parse_data.convert import convert_data, convert_file_to_bytes, \
    convert_html
import pytest


def test_convert_html():
    html_code = open('test.html', encoding='utf-8').read()
    convert_html.convert_html_code_to_image(html_code=html_code, id_task=0,
                                            type_html='text')


if __name__ == '__main__':
    test_convert_html()
