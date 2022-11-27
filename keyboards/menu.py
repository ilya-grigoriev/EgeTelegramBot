from aiogram.types import ReplyKeyboardMarkup
from keyboards.btn_get_task import BTN_GET_TASK
from keyboards.btn_back_home import BTN_BACK_HOME

buttons = [
    [BTN_GET_TASK],
    [BTN_BACK_HOME]
]
keyboard_menu = ReplyKeyboardMarkup(keyboard=buttons)
