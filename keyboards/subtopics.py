from keyboards.btn_back import BTN_BACK
from keyboards.btn_random_task import BTN_RANDOM_TASK
from parse_data.get_data.get_data_of_subject import get_json_of_data_subject
from parse_data.config_for_parsing import subjects_en
from parse_data.typing_for_parsing import DataTask
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard_for_subtopic(
    *, issue_data: DataTask, num_issue: str
) -> ReplyKeyboardMarkup:
    subtopic_buttons = [
        [KeyboardButton(f"{num_issue}{ind_subtopic}. {subtopic.title}")]
        for ind_subtopic, subtopic in enumerate(issue_data.subtopics, start=1)
    ]
    total_keyboard = [*subtopic_buttons, [BTN_RANDOM_TASK], [BTN_BACK]]
    keyboard_subtopics = ReplyKeyboardMarkup(total_keyboard)
    return keyboard_subtopics
