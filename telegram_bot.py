from aiogram import Dispatcher, Bot, types, executor
from loguru import logger
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    print(message)
    await message.reply(f"Здравствуйте, {message['from']['first_name']}!")
    await message.reply('Это неофициальный бот для подготовки к ЕГЭ')
    await message.reply('Разделы ')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
