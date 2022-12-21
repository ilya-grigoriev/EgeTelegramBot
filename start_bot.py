from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from os import getenv
from keyboards.subjects import keyboard_subjects
from keyboards.menu import keyboard_menu
from handlers import greeting, get_data, check_response
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from parse_data.parse_ege_tests import parse_tasks
from parse_data.config_for_parsing import subjects_ru
from work_with_db.check_existing_db import check_db

TELEGRAM_TOKEN = getenv('TOKEN')
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
check_db()


class Response(StatesGroup):
    subject = State()
    answer = State()
    back_or_get = State()


@dp.message_handler(commands=['start', 'help'], state=None)
async def send_welcome_(message: types.Message):
    await greeting.send_welcome(message=message)
    await Response.subject.set()


@dp.message_handler(state=Response.subject)
async def get_task_(message: types.Message, state: FSMContext):
    if message.text.strip() in subjects_ru:
        await state.update_data({'image_sent': False})

        await message.answer('Отправка задания...',
                             reply_markup=types.ReplyKeyboardRemove())

        await Response.next()
        await get_data.get_task(message=message, state=state,
                                after_subject_selection=True, bot=bot)
    else:
        await message.answer('Данного предмета нет в списке')
        await message.answer('Выберите предмет:',
                             reply_markup=keyboard_subjects)
        await Response.subject.set()


@dp.message_handler(state=Response.answer)
async def process_name(message: types.Message, state: FSMContext):
    data = await state.get_data()

    if not data.get('image_sent'):
        await message.answer('Задание ещё не отправлено. Подождите немного')
    else:
        await check_response.check_answer_from_user(message=message,
                                                    state=state)
        await Response.next()


@dp.message_handler(state=Response.back_or_get)
async def back_or_get(message: types.Message, state: FSMContext):
    response = message.text

    if response == 'Получить задание':
        await Response.answer.set()

        await message.answer('Отправка задания...',
                             reply_markup=types.ReplyKeyboardRemove())

        await state.update_data({'image_sent': False})
        await get_data.get_task(message=message, state=state,
                                after_subject_selection=False, bot=bot)
    elif response == 'Вернуться в главное меню':
        await Response.subject.set()
        await message.answer('Главное меню:', reply_markup=keyboard_subjects)
    else:
        await Response.back_or_get.set()
        await message.answer('Некорректный ответ', reply_markup=keyboard_menu)


def main() -> None:
    scheduler.add_job(parse_tasks, trigger='cron', hour='0')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
