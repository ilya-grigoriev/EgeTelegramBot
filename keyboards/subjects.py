from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

RUSSIAN = KeyboardButton('Русский язык')
MATH = KeyboardButton('Математика профильная')

buttons = [
    [RUSSIAN, MATH]
]

keyboard_subjects = ReplyKeyboardMarkup(keyboard=buttons)
