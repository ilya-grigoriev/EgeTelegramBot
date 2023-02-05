"""This module help to get data of keyboard for subtopics."""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.btn_back import BTN_BACK
from keyboards.btn_random_task import BTN_RANDOM_TASK
from parse_data.typing_for_parsing import DataTask


def get_keyboard_for_subtopic(
    *, issue_data: DataTask, num_issue: str
) -> ReplyKeyboardMarkup:
    """
    Getting keyboards for subtopics.

    Parameters
    ----------
    issue_data : DataTask
        Pydantic model with data of issue.
    num_issue : int
        Number issue.

    Returns
    -------
    ReplyKeyboardMarkup
        Keyboard for subtopics.
    """
    if not issue_data.subtopics:
        return "No subtopics"

    subtopic_buttons = [
        [KeyboardButton(f"{num_issue}{ind_subtopic}. {subtopic.title}")]
        for ind_subtopic, subtopic in enumerate(issue_data.subtopics, start=1)
    ]
    total_keyboard = [*subtopic_buttons, [BTN_RANDOM_TASK], [BTN_BACK]]
    keyboard_subtopics = ReplyKeyboardMarkup(total_keyboard)
    return keyboard_subtopics
