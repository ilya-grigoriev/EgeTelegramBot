import os

from PIL import Image
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from keyboards.menu import keyboard_menu
from work_with_db.select_data import select_task
from config_for_parsing import translation_for_db
from parse_data.convert.convert_file_to_bytes import convert_image_to_bytes


async def get_task(*, message: types.Message, state: FSMContext,
                   after_subject_selection: bool, bot: Bot) -> None:
    if after_subject_selection:
        subject = translation_for_db.get(message.text)
        await state.update_data({'subject': subject})
    else:
        data = await state.get_data()
        subject = data.get('subject')

    task, id_task, correct_answer = await select_task(subject=subject)
    file_name = f'{id_task}.png'
    await state.update_data({'correct_answer': correct_answer})

    if task:
        await message.answer(text=task,
                             reply_markup=types.ReplyKeyboardRemove())

        await bot.send_photo(message.chat.id, open(file_name, 'rb'))
        os.remove(file_name)

        await message.answer(text='Введите ответ:')
    else:
        await message.answer(text='В базе данных на данный момент нет задач')
        await message.answer(text='Выберите другой предмет:',
                             reply_markup=keyboard_menu)
