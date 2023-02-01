from aiogram import types


async def send_welcome(*, message: types.Message, keyboard: types.ReplyKeyboardMarkup):
    """This handler will be called when user sends `/start` command."""
    await message.reply(f"Здравствуйте, {message['from']['first_name']}!")
    await message.answer("Это неофициальный бот для подготовки к ЕГЭ")

    if keyboard:
        await message.answer(
            "Предметы, доступные для тренировки:", reply_markup=keyboard
        )
    else:
        await message.answer("На данный момент нет доступных предметов.")
        await message.answer("Попробуйте повторить попытку позже")
