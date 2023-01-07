from aiogram.types import ReplyKeyboardMarkup
from keyboards.btn_get_task import BTN_GET_TASK
from keyboards.btn_back_home import BTN_BACK_HOME
from keyboards.btn_report import BTN_REPORT

buttons = [
    [BTN_GET_TASK],
    [BTN_BACK_HOME],
    [BTN_REPORT]
]
keyboard_menu = ReplyKeyboardMarkup(keyboard=buttons)
