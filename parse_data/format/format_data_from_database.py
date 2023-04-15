"""Module help to format data from database."""
import traceback

import aiogram
from logger_for_project import my_logger
from parse_data.convert.convert_html import convert_html_code_to_bytes
from parse_data.typing_for_parsing import DataFromDB


async def format_data_for_tg_and_send_photo(
    *, data: DataFromDB, bot: aiogram.Bot, chat_id: str, subject_name_en: str
) -> None:
    """Format data for Telegram and sending converted images to bytes.

    Parameters
    ----------
    data : DataFromDB
        Dataclass DataFromDB.
    bot : aiogram.Bot
        Telegram bot from aiogram.
    chat_id : int
        Telegram chat id.
    subject_name_en : str
        The name of the subject in English.
    """
    template_url = f"https://{subject_name_en}-ege.sdamgia.ru"

    try:
        task_images = await convert_html_code_to_bytes(
            html_code=data.task_desc_html,
            type_html="task",
            data=data,
            template_url=template_url,
        )

        await bot.send_message(chat_id=chat_id, text="Условия задания:")
        if task_images:
            for task_image in task_images:
                await bot.send_photo(chat_id=chat_id, photo=task_image)

        text_for_task_images = await convert_html_code_to_bytes(
            html_code=data.text_for_task_html,
            type_html="text_for_task",
            data=data,
            template_url=template_url,
        )

        if text_for_task_images:
            await bot.send_message(chat_id=chat_id, text="Текст задания:")
            for text_for_task_image in text_for_task_images:
                await bot.send_photo(chat_id=chat_id, photo=text_for_task_image)

        answer_images = await convert_html_code_to_bytes(
            html_code=data.answer,
            type_html="answer",
            data=data,
            template_url=template_url,
        )

        if answer_images:
            await bot.send_message(chat_id=chat_id, text="Ответ на задание:")
            for answer_image in answer_images:
                await bot.send_photo(chat_id=chat_id, photo=answer_image)
        else:
            solution_images = await convert_html_code_to_bytes(
                html_code=data.solution_html,
                type_html="solution",
                data=data,
                template_url=template_url,
            )

            if solution_images:
                await bot.send_message(
                    chat_id=chat_id, text="Пояснение к задаче:"
                )
                for solution_image in solution_images:
                    await bot.send_photo(chat_id=chat_id, photo=solution_image)

            if data.file_urls_for_task:
                await bot.send_message(
                    chat_id=chat_id, text="Ссылки с файлами из задания:"
                )
                file_urls = data.file_urls_for_task.split(", ")
                await bot.send_message(
                    chat_id=chat_id, text="\n".join(file_urls)
                )
    except Exception:  # pylint: disable=broad-except
        my_logger.error(traceback.format_exc())
