import aiohttp
import pytest
from hypothesis import given, strategies as st
from parse_data.convert.convert_task import get_tasks_from_html


@pytest.mark.asyncio
@given(
    html=st.text(),
    template_url=st.text(),
    n_issue=st.integers(),
    is_detailed=st.booleans(),
)
async def test_incorrect_data(
    html: str, template_url: str, n_issue: int, is_detailed: bool
):
    with pytest.raises(Exception):
        async with aiohttp.ClientSession() as session:
            await get_tasks_from_html(
                html=html,
                template_url=template_url,
                session=session,
                n_issue=n_issue,
                is_detailed=is_detailed,
            )


@pytest.mark.asyncio
async def test_correct_data():
    async with aiohttp.ClientSession() as session:
        await get_tasks_from_html(
            html="<p>a</p>",
            template_url="https://test-ege.sdamgia.ru",
            session=session,
            n_issue=1,
            is_detailed=True,
        )
