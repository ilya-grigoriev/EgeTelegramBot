from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.btn_back_home import BTN_BACK_HOME
from keyboards.btn_random_task import BTN_RANDOM_TASK

from parse_data.typing_for_parsing import DataTask


def get_keyboard_for_issue(*,
                           issue_data: List[DataTask]) -> ReplyKeyboardMarkup:
    issue_titles = [[KeyboardButton(f'{ind_issue}. {issue.title}')] for
                    ind_issue, issue in enumerate(issue_data, start=1)]
    total_keyboard = [*issue_titles, [BTN_RANDOM_TASK], [BTN_BACK_HOME]]
    keyboard_issues = ReplyKeyboardMarkup(total_keyboard)

    return keyboard_issues
