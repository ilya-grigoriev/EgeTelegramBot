"""This modules is designed for button report."""
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BTN_REPORT = KeyboardButton("Сообщить об ошибке")
keyboard_get_task = ReplyKeyboardMarkup([[BTN_REPORT]])
