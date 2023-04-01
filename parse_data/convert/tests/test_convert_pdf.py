import pytest
from hypothesis import given
from hypothesis import strategies as st
from parse_data.convert.convert_pdf import convert_pdf_to_images
from parse_data.exceptions_for_parsing import FilePathIsNotStr


@given(x=st.integers(), y=st.integers())
def test_integer(x: int, y: int):
    with pytest.raises(FilePathIsNotStr):
        convert_pdf_to_images(path_pdf_file=x, path_image=y)  # type: ignore


@given(pdf_file=st.text(), image_file=st.text())
def test_not_file_path(pdf_file: str, image_file: str):
    with pytest.raises(FileNotFoundError):
        convert_pdf_to_images(path_pdf_file=pdf_file, path_image=image_file)


def test_converting():
    package_path = "\\".join(__file__.split("\\")[:-1])
    pdf_path = f"{package_path}\\sample.pdf"
    image_path = f"{package_path}\\empty_image.jpg"
    with open(image_path, "w"):
        pass
    convert_pdf_to_images(path_pdf_file=pdf_path, path_image=image_path)
