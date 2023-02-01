from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from work_with_db.get_data.select_data import select_task
from parse_data.format.format_data_from_database import (
    format_data_for_tg_and_send_photo,
)


async def get_random_task(*, message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    task_section = data.get("task_section")
    subject_name = data.get("subject")

    data_from_db = await select_task(
        subject_name=subject_name, task_section=task_section
    )

    if data_from_db:
        await state.update_data({"id_task": data_from_db.id_task})
        subject_name = data.get("subject")
        await format_data_for_tg_and_send_photo(
            data=data_from_db,
            bot=bot,
            chat_id=message.chat.id,
            subject_name_en=subject_name,
        )
