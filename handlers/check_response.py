"""Module is designed to checking response."""
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.menu import keyboard_menu


async def check_answer_from_user(
    *, message: types.Message, state: FSMContext
) -> None:
    """Check answer from user's message.

    Parameters
    ----------
    message : types.Message
    state : FSMContext
    """
    data = await state.get_data()
    correct_answer = data.get("correct_answer")

    if message.text.strip() == str(correct_answer):
        await message.answer("Правильный ответ!", reply_markup=keyboard_menu)
    else:
        await message.answer("Неправильно")
        await message.answer(
            f"Правильный ответ: {correct_answer}", reply_markup=keyboard_menu
        )
