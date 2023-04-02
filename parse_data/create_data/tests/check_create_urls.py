from hypothesis import given, strategies as st
import pytest

from parse_data.typing_for_parsing import typing_url
from parse_data.create_data.create_urls import create_urls_for_request


@given(url=st.text(), max_skip=st.integers())
@pytest.mark.asyncio
async def test_incorrect_data(url: typing_url, max_skip: int):
    with pytest.raises(Exception):
        await create_urls_for_request(url=url, max_skip=max_skip)


@pytest.mark.asyncio
async def test_correct_data():
    url = "https://a-ege.sdamgia.ru/test?theme=1"
    await create_urls_for_request(url=url, max_skip=0)
