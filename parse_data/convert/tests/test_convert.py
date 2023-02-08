# flake8: noqa
import asyncio

from parse_data.convert import convert_html
import pytest


def test_convert_html():
    html_code = open("test.html", encoding="utf-8").read()
    asyncio.run(
        convert_html.convert_html_code_to_image(
            html_code=html_code, id_task=0, type_html="text"
        )
    )


def test_convert_pdf_to_formatted_image():
    html_code = open("test.html", encoding="utf-8").read()
    asyncio.run(
        convert_html.convert_html_code_to_image(
            html_code=html_code, id_task=0, type_html="text"
        )
    )


@pytest.mark.asyncio
async def test_async_converting():
    html_code = open("test.html", encoding="utf-8").read()
    cor = convert_html.convert_html_code_to_image(
        html_code=html_code, id_task=0, type_html="text"
    )
    cor_2 = convert_html.convert_html_code_to_image(
        html_code=html_code, id_task=1, type_html="solution"
    )
    result = await asyncio.gather(
        cor,
        cor_2,
        cor,
        cor_2,
        cor,
        cor_2,
        cor,
        cor_2,
        cor,
        cor,
        cor_2,
        cor,
        cor_2,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor_2,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor,
        cor_2,
    )
    print(result)
