# flake8: noqa
from hypothesis import given, strategies as st
from parse_data.convert import convert_html
import pytest

from parse_data.typing_for_parsing import DataFromDB


@given(html_code=st.text(), id_task=st.integers(), type_html=st.text())
@pytest.mark.asyncio
async def test_incorrect_data_convert_html(
    html_code: str, id_task: int, type_html: str
):
    with pytest.raises(Exception):
        await convert_html.convert_html_code_to_image(
            html_code=html_code, id_task=id_task, type_html=type_html
        )


@pytest.mark.asyncio
async def test_convert_html():
    package_path = "\\".join(__file__.split("\\")[:-1])
    html_path = f"{package_path}\\test.html"
    html_code = open(html_path, encoding="utf-8").read()
    await convert_html.convert_html_code_to_image(
        html_code=html_code, id_task=0, type_html="text"
    )


@pytest.mark.asyncio
async def test_convert_pdf_to_formatted_image():
    package_path = "\\".join(__file__.split("\\")[:-1])
    html_path = f"{package_path}\\test.html"
    html_code = open(html_path, encoding="utf-8").read()
    await convert_html.convert_html_code_to_image(
        html_code=html_code, id_task=0, type_html="text"
    )


@given(
    html_code=st.text(),
    type_html=st.text(),
    data=st.dictionaries(st.text(), st.text()),
    template_url=st.text(),
)
@pytest.mark.asyncio
async def test_incorrect_data_convert_html_code_to_bytes(
    html_code: str, type_html: str, data: DataFromDB, template_url: str
):
    with pytest.raises(Exception):
        await convert_html.convert_html_code_to_bytes(
            html_code=html_code,
            type_html=type_html,
            data=data,
            template_url=template_url,
        )


@pytest.mark.asyncio
async def test_correct_data_convert_html_code_to_bytes():
    data = DataFromDB(
        task_section="1",
        id_task=1,
        is_detailed=True,
        task_desc_html="a",
        file_urls_for_task="a",
        text_for_task_html="a",
        solution_html="a",
        answer="a",
    )
    template_url = "https://a-ege.sdamgia.ru"
    await convert_html.convert_html_code_to_bytes(
        html_code="<p>a</p>",
        type_html="task",
        data=data,
        template_url=template_url,
    )
