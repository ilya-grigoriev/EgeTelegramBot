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
html = """<div class="WordSection1   "><p class="MsoNormal   "><span
        style='color:black'>На рисунке изображён график   функции <span
        style='position:relative;top:6.0pt'><img width="71   " height="24   "
                                                 src="http://os.fipi.ru/api/docs/byid/81887   "></span>. На оси абсцисс отмечены семь точек: <span
        style='position:relative;top:7.0pt'><img width="20   " height="27   "
                                                 src="http://os.fipi.ru/api/docs/byid/81888   "></span>, <span
        style='position:relative;   top:7.0pt'><img width="21   "
                                                    height="27   "
                                                    src="http://os.fipi.ru/api/docs/byid/81889   "></span>, <span
        style='position:relative;top:7.0pt'><img width="21   " height="27   "
                                                 src="http://os.fipi.ru/api/docs/byid/81890   "></span>, <span
        style='position:relative;   top:7.0pt'><img width="21   "
                                                    height="27   "
                                                    src="http://os.fipi.ru/api/docs/byid/81891   "></span>, <span
        style='position:relative;top:7.0pt'><img width="21   " height="27   "
                                                 src="http://os.fipi.ru/api/docs/byid/81892   "></span>, <span
        style='position:relative;   top:7.0pt'><img width="21   "
                                                    height="27   "
                                                    src="http://os.fipi.ru/api/docs/byid/81893   "></span>, <span
        style='position:relative;top:7.0pt'><img width="21   " height="27   "
                                                 src="http://os.fipi.ru/api/docs/byid/81894   "></span>. </span>В
    скольких из этих точек производная функции <span
            style='color:black;position:relative;top:6.0pt'><img width="41   "
                                                                 height="24   "
                                                                 src="http://os.fipi.ru/api/docs/byid/81895   "></span> отрицательна?
</p>
    <p class="MsoNormal   " align="center   " style='text-align:center'>
    <span style='color:black'><img width="293   " height="189   "
                                   src="http://os.fipi.ru/api/docs/byid/81896   "
                                   alt="Adobe
                                   Systems   "></span></p>
</div>"""


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


def main() -> None:
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
