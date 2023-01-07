from aiogram import types as types
from aiogram.dispatcher import FSMContext as FSMContext

async def check_answer_from_user(
    *, message: types.Message, state: FSMContext
) -> None: ...
