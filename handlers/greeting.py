from aiogram import types
from keyboards.subjects import keyboard_subjects


async def send_welcome(*, message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Здравствуйте, {message['from']['first_name']}!")
    await message.answer('Это неофициальный бот для подготовки к ЕГЭ')
    await message.answer('Предметы, доступные для тренировки:',
                         reply_markup=keyboard_subjects)
