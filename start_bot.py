from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from os import getenv
from keyboards.subjects import keyboard_subjects
from handlers import greeting, get_data, check_response

TELEGRAM_TOKEN = getenv('TOKEN')
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


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
    await get_data.get_task(message=message, state=state,
                            after_subject_selection=True)
    await Response.next()


@dp.message_handler(state=Response.answer)
async def process_name(message: types.Message, state: FSMContext):
    await check_response.check_answer_from_user(message=message,
                                                state=state)
    await Response.next()


@dp.message_handler(state=Response.back_or_get)
async def back_or_get(message: types.Message, state: FSMContext):
    response = message.text

    if response == 'Получить задание':
        await Response.answer.set()
        await get_data.get_task(message=message, state=state,
                                after_subject_selection=False)
    elif response == 'Вернуться в главное меню':
        await Response.subject.set()
        await message.answer('Главное меню:', reply_markup=keyboard_subjects)


@dp.callback_query_handler(text='back_home', state=Response.answer)
async def back_home_(callback_query: types.CallbackQuery, state: FSMContext):
    await returning.back_home(callback_query=callback_query, bot=bot)
    await state.finish()


def main() -> None:
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
