import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from work_with_db.check_data.check_existing_db import check_db
from keyboards.get_data_for_keyboard.get_data_for_subjects import get_subjects_data

TELEGRAM_TOKEN = os.getenv("TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# check_db()
scheduler = AsyncIOScheduler()
subjects_data_for_keyboard = get_subjects_data()


class Response(StatesGroup):
    issue = State()
    subtopic = State()
    task = State()
    back_or_get = State()
    check_message = State()
