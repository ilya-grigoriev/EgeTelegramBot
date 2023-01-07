from typing import Tuple, Optional
from parse_data.convert.convert_html import convert_html_code_to_image
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes
from parse_data.typing_for_parsing import DataFromDB, DataForTG
from aiogram import Bot


async def format_data_for_tg_and_send_photo(*, data: DataFromDB, bot: Bot,
                                            chat_id: str):
    task_image = await convert_html_code_to_image(
        html_code=data.task_desc_html,
        type_html='task',
        id_task=data.id_task)
    await bot.send_photo(chat_id=chat_id, photo=task_image)

    if data.text_for_task_html:
        text_for_task_image = await convert_html_code_to_image(
            html_code=data.text_for_task_html, type_html='text_for_task',
            id_task=data.id_task)
        await bot.send_photo(chat_id=chat_id, photo=text_for_task_image)

    if data.is_detailed:
        answer_image = await convert_html_code_to_image(html_code=data.answer,
                                                        type_html='answer',
                                                        id_task=data.id_task)
        await bot.send_photo(chat_id=chat_id, photo=answer_image)
    else:
        solution_image = await convert_html_code_to_image(
            html_code=data.solution_html,
            type_html='solution',
            id_task=data.id_task)
        await bot.send_photo(chat_id=chat_id, photo=solution_image)
