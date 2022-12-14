import os
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from keyboards.subjects import keyboard_subjects
from work_with_db.select_data import select_task
from config_for_parsing import translation_for_db


async def get_task(*, message: types.Message, state: FSMContext,
                   after_subject_selection: bool, bot: Bot) -> None:
    if after_subject_selection:
        subject = translation_for_db.get(message.text)
        await state.update_data({'subject': subject})
    else:
        data = await state.get_data()
        subject = data.get('subject')

    response = await select_task(subject=subject)
    if response and response[3]:
        task, id_task, correct_answer, file_path = response
        await state.update_data({'correct_answer': correct_answer})

        await message.answer(text=task,
                             reply_markup=types.ReplyKeyboardRemove())

        await bot.send_document(message.chat.id, open(file_path, 'rb'))
        os.remove(file_path)

        await message.answer(text='Введите ответ:')
    else:
        await message.answer(text='Произошла ошибка. Повторите попытку позже.')
        await message.answer(text='Выберите другой предмет:',
                             reply_markup=keyboard_subjects)
        await state.finish()
