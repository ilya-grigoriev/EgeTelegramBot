import re
from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.subtopics import get_keyboard_for_subtopic
from parse_data.typing_for_parsing import DataTask
from parse_data.config_for_parsing import translation_from_rus
from work_with_bot.init_for_bot import subjects_data_for_keyboard
from keyboards.issues import get_keyboard_for_issue


async def get_data_for_issues(*, message: types.Message, state: FSMContext,
                              response: str):
    subject_en = translation_from_rus.get(response)
    await state.update_data({"subject": subject_en})

    for subject in subjects_data_for_keyboard:
        if subject["title"] == subject_en:
            issues = subject["issues"]
            keyboard_issues = get_keyboard_for_issue(issues_data=issues)

            await state.update_data({"issues": issues})
            await state.update_data({"keyboard_issues": keyboard_issues})

            await message.answer(
                "Выберите номер задания:", reply_markup=keyboard_issues
            )

            return None


async def get_data_for_subtopics(*, message: types.Message, state: FSMContext,
                                 response: str, issues_data: List[DataTask]):
    num_issue = re.search("\d+\.", response)
    num_issue = num_issue.group()
    await state.update_data({'issue': num_issue.strip('.')})
    response = re.sub("\d+\.", "", response).strip()
    for issue in issues_data:
        if issue.title == response:
            keyboard_subtopics = get_keyboard_for_subtopic(
                issue_data=issue, num_issue=num_issue
            )
            await state.update_data(
                {"keyboard_subtopics": keyboard_subtopics})
            await message.answer(
                "Выберите подраздел задания:",
                reply_markup=keyboard_subtopics
            )

            break
