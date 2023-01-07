from parse_data.convert.convert_html import convert_html_code_to_image
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.typing_for_parsing import DataFromDB
from aiogram import Bot


async def format_data_for_tg_and_send_photo(
    *, data: DataFromDB, bot: Bot, chat_id: str, subject_name_en: str
):
    template_url = f"https://{subject_name_en}-ege.sdamgia.ru"

    formatted_task_desc_html = delete_excess_data_in_tag(
        template_url=template_url, tag=data.task_desc_html
    )

    task_images = await convert_html_code_to_image(
        html_code=formatted_task_desc_html, type_html="task", id_task=data.id_task
    )

    await bot.send_message(chat_id=chat_id, text="Условия задания:")
    for task_image in task_images:
        await bot.send_photo(chat_id=chat_id, photo=task_image)

    if data.text_for_task_html:
        formatted_text_for_task_html = delete_excess_data_in_tag(
            template_url=template_url, tag=data.text_for_task_html
        )

        text_for_task_images = await convert_html_code_to_image(
            html_code=formatted_text_for_task_html,
            type_html="text_for_task",
            id_task=data.id_task,
        )

        await bot.send_message(chat_id=chat_id, text="Текст задания:")
        for text_for_task_image in text_for_task_images:
            await bot.send_photo(chat_id=chat_id, photo=text_for_task_image)

    if not data.solution_html:
        converted_answer_text_to_html = f"<p>Ответ: {data.answer}</p>"
        answer_images = await convert_html_code_to_image(
            html_code=converted_answer_text_to_html,
            type_html="answer",
            id_task=data.id_task,
        )

        await bot.send_message(chat_id=chat_id, text="Ответ на задание:")
        for answer_image in answer_images:
            await bot.send_photo(chat_id=chat_id, photo=answer_image)
    else:
        formatted_solution_html = delete_excess_data_in_tag(
            template_url=template_url, tag=data.solution_html
        )

        solution_images = await convert_html_code_to_image(
            html_code=formatted_solution_html,
            type_html="solution",
            id_task=data.id_task,
        )

        await bot.send_message(chat_id=chat_id, text="Пояснение к задаче:")
        for solution_image in solution_images:
            await bot.send_photo(chat_id=chat_id, photo=solution_image)
