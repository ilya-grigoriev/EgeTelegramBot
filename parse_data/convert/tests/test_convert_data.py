import pytest
from hypothesis import given
from hypothesis import strategies as st
from parse_data.convert.convert_data import convert_subtopic_to_dataclass
from parse_data.typing_for_parsing import Subtopic


@given(
    data_subtopic=st.dictionaries(st.text(), st.text()),
    subject_name_en=st.text(),
    n_issue=st.integers(),
    n_subtopic=st.integers(),
    is_detailed=st.booleans(),
)
@pytest.mark.asyncio
async def test_incorrect_data(
    data_subtopic: Subtopic,
    subject_name_en: str,
    n_issue: int,
    n_subtopic: int,
    is_detailed: bool,
):
    with pytest.raises(Exception):
        await convert_subtopic_to_dataclass(
            data_subtopic=data_subtopic,
            subject_name_en=subject_name_en,
            n_issue=n_issue,
            n_subtopic=n_subtopic,
            is_detailed=is_detailed,
        )


@pytest.mark.asyncio
async def test_correct_data():
    subtopic = Subtopic(**{"id": 2, "title": "No", "amount": 2})
    await convert_subtopic_to_dataclass(
        data_subtopic=subtopic,
        subject_name_en="rus",
        n_issue=1,
        n_subtopic=1,
        is_detailed=True,
    )
