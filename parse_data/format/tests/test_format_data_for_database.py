import pytest
from hypothesis import given
from hypothesis import strategies as st
from parse_data.format.format_data_for_database import format_data_for_db
from parse_data.typing_for_parsing import DataTaskOfSubtopic


@given(
    number_task=st.integers(),
    is_detailed=st.booleans(),
    number_subtopic=st.integers(),
)
def test_incorrect_data_for_format_data_for_db(
    number_task, is_detailed, number_subtopic
):
    task = DataTaskOfSubtopic(
        id_task=1,
        task_desc_html="",
        text_for_task_html="",
        file_urls_for_task="",
        solution_html="",
        answer="",
    )
    if number_task <= 0 or number_subtopic <= 0:
        with pytest.raises(Exception):
            format_data_for_db(
                task=task,
                number_task=number_task,
                is_detailed=is_detailed,
                number_subtopic=number_subtopic,
            )
