"""Module help to get keyboards for subjects."""
from typing import List, Optional

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from parse_data.typing_for_parsing import DataSubjectForTG
from parse_data.config_for_parsing import translation_from_eng


def get_keyboard_for_subjects(
    *, subjects: List[DataSubjectForTG]
) -> Optional[ReplyKeyboardMarkup]:
    """Get keyboard for subjects.

    Parameters
    ----------
    subjects : List[DataSubjectForTG]
        List of TypedDict with data of subject for Telegram.

    Returns
    -------
    Optional[ReplyKeyboardMarkup]
        Keyboard for subjects.
    """
    buttons = []
    for subject in subjects:
        if subject:
            subject_name_rus = translation_from_eng.get(subject["title"])
            if subject_name_rus:
                buttons.append(KeyboardButton(subject_name_rus))

    keyboard_subjects = ReplyKeyboardMarkup(keyboard=[buttons])
    return keyboard_subjects if buttons else None
