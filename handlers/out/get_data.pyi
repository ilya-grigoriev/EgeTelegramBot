from aiogram import Bot as Bot, types
from aiogram.dispatcher import FSMContext as FSMContext

async def get_task(
    *,
    message: types.Message,
    state: FSMContext,
    after_subject_selection: bool,
    bot: Bot
) -> None: ...
