"""Module is designed for initializing Telegram bot."""
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StatesGroup, State
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from keyboards.get_data_for_keyboard.get_data_for_telegram_subjects import (
    get_subjects_data,
)
from work_with_db.check_data.check_existing_db import check_db

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
check_db()
scheduler = AsyncIOScheduler()
subjects_data_for_keyboard = get_subjects_data()


class Response(StatesGroup):
    """Aiogram State for user interaction."""

    issue = State()
    subtopic = State()
    task = State()
    back_or_get = State()
    check_message = State()
