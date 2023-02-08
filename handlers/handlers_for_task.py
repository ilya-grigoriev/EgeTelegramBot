"""Module help to work with sending task."""
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.get_data import get_random_task
from keyboards.menu import keyboard_menu


async def send_task(*, message: types.Message, state: FSMContext, bot: Bot):
    """Get random task and send task.

    Parameters
    ----------
    message : types.Message
    state : FSMContext
    bot : Bot
    """
    await state.update_data({"is_sending": True})
    await message.answer("Идёт отправка задания...", reply_markup=ReplyKeyboardRemove())

    await get_random_task(message=message, state=state, bot=bot)
    await message.answer("Выберите действие:", reply_markup=keyboard_menu)
    await state.update_data({"is_sending": False})
