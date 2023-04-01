import pytest
from hypothesis import given, strategies as st
from parse_data.exceptions_for_parsing import FilePathIsNotStr

from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes


def test_empty_file_name():
    with pytest.raises(FileNotFoundError):
        convert_image_to_bytes(file_name="")


def test_integer():
    with pytest.raises(FilePathIsNotStr):
        convert_image_to_bytes(file_name=123)


@given(s=st.text())
def test_not_file_name(s):
    with pytest.raises(FileNotFoundError):
        convert_image_to_bytes(file_name=s)


def test_image_jpg():
    package_path = "\\".join(__file__.split("\\")[:-1])
    jpg_path = f"{package_path}\\pic_for_testing.jpg"
    convert_image_to_bytes(file_name=jpg_path)


def test_image_png():
    package_path = "\\".join(__file__.split("\\")[:-1])
    png_path = f"{package_path}\\pic_for_testing.png"
    convert_image_to_bytes(file_name=png_path)
