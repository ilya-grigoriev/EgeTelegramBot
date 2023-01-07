import re
import traceback

from aiogram.utils import executor

from logger_for_project import my_logger
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.subjects import keyboard_subjects
from keyboards.menu import keyboard_menu
from handlers import greeting, get_data_for_keyboard, handlers_for_task
from parse_data.config_for_parsing import subjects_ru
from work_with_bot.init_for_bot import bot, dp, scheduler, Response
from parse_data.parse_ege_tests import parse_tasks


@dp.message_handler(commands=["start", "help"], state=None)
async def send_welcome_(message: types.Message):
    await greeting.send_welcome(message=message)
    await Response.issue.set()


@dp.message_handler(state=Response.issue)
async def get_issues(message: types.Message, state: FSMContext):
    response = message.text.strip()
    if response in subjects_ru:
        await Response.subtopic.set()
        await get_data_for_keyboard.get_data_for_issues(
            message=message, state=state, response=response
        )
    else:
        await message.answer("Данного предмета нет в списке")
        await message.answer("Выберите предмет:", reply_markup=keyboard_subjects)
        await Response.issue.set()


@dp.message_handler(state=Response.subtopic)
async def get_subtopics(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = message.text
    issues_data = data.get("issues")
    keyboard_issues = data.get("keyboard_issues")
    issue_titles = [btn[0]["text"] for btn in keyboard_issues["keyboard"]]
    is_sending = data.get("is_sending")

    if is_sending:
        await message.answer("Задание ещё не отправлено. Подождите немного")
    elif response == "❔ Получить случайное задание":
        await state.update_data({"task_section": "%/%"})

        try:
            await handlers_for_task.send_task(message=message, state=state, bot=bot)
        except Exception as e:
            await state.update_data({"is_sending": True})
            my_logger.error(traceback.format_exc())
            await message.answer("Произошла ошибка. Повторите запрос позже")

        await Response.back_or_get.set()
    elif response == "🏠 Вернуться в главное меню":
        await message.answer("Выберите предмет:", reply_markup=keyboard_subjects)
        await Response.issue.set()
    elif response in issue_titles:
        await Response.task.set()
        await get_data_for_keyboard.get_data_for_subtopics(
            message=message, state=state, response=response, issues_data=issues_data
        )
    else:
        await message.answer("Данного задания нет в списке")
        await message.answer("Выберите задание:", reply_markup=keyboard_issues)
        await Response.subtopic.set()


@dp.message_handler(state=Response.task)
async def get_task(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = message.text
    keyboard_issues = data.get("keyboard_issues")
    keyboard_subtopics = data.get("keyboard_subtopics")
    subtopic_titles = [btn[0]["text"] for btn in keyboard_subtopics["keyboard"]]
    is_sending = data.get("is_sending")

    if is_sending:
        await message.answer("Задание ещё не отправлено. Подождите немного")
    elif response == "❔ Получить случайное задание":
        num_issue = data.get("issue")
        task_section = f"{num_issue}/%"
        await state.update_data({"task_section": task_section})
        await Response.back_or_get.set()

        try:
            await handlers_for_task.send_task(message=message, state=state, bot=bot)
        except Exception as e:
            my_logger.error(traceback.format_exc())
            await message.answer("Произошла ошибка. Повторите запрос позже")
    elif response == "🔙 Вернуться обратно":
        await message.answer(
            "Выберите подраздел задания:", reply_markup=keyboard_issues
        )
        await Response.issue.set()
    elif response in subtopic_titles:
        num_issue, num_subtopic = re.findall(r"\d+\.", response)
        task_section = f'{num_issue.strip(".")}/{num_subtopic.strip(".")}'
        await state.update_data({"task_section": task_section})
        await Response.back_or_get.set()

        try:
            await handlers_for_task.send_task(message=message, state=state, bot=bot)
        except Exception as e:
            my_logger.error(traceback.format_exc())
            await message.answer("Произошла ошибка. Повторите запрос позже")
    else:
        await message.answer("Данного подраздела нет в списке")
        await message.answer("Выберите подраздел:", reply_markup=keyboard_subtopics)
        await Response.subtopic.set()


@dp.message_handler(state=Response.back_or_get)
async def back_or_get(message: types.Message, state: FSMContext):
    response = message.text
    data = await state.get_data()
    is_sending = data.get("is_sending")

    if is_sending:
        await message.answer("Задание ещё не отправлено. Подождите немного")
    elif response == "Получить задание":

        try:
            await handlers_for_task.send_task(message=message, state=state, bot=bot)
        except Exception as e:
            my_logger.error(traceback.format_exc())
            await message.answer("Произошла ошибка. Повторите запрос позже")

        await Response.back_or_get.set()
    elif response == "🏠 Вернуться в главное меню":
        await Response.issue.set()
        await message.answer("Главное меню:", reply_markup=keyboard_subjects)
    elif response == "Сообщить об ошибке":
        await Response.issue.set()
        await message.answer("Спасибо за обратную связь!")
        await message.answer("Главное меню:", reply_markup=keyboard_subjects)
        my_logger.error("Incorrect photo sending")
        my_logger.error(f'ID task: {data.get("id_task")}')
    else:
        await Response.back_or_get.set()
        await message.answer("Некорректный ответ", reply_markup=keyboard_menu)


def main():
    scheduler.add_job(parse_tasks, trigger="cron", hour="0")
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
