from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types, Bot, dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TELEGRAM_TOKEN: str
bot: Bot
storage: MemoryStorage
dp: dispatcher
scheduler: AsyncIOScheduler


class Response(StatesGroup):
    subject: State
    answer: State
    back_or_get: State


async def send_welcome_(message: types.Message): ...


async def get_task_(message: types.Message, state: FSMContext): ...


async def process_name(message: types.Message, state: FSMContext): ...


async def back_or_get(message: types.Message, state: FSMContext): ...


def main() -> None: ...
