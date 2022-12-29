from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from keyboards.subjects import keyboard_subjects
from work_with_db.get_data.select_data import select_task
from parse_data.config_for_parsing import translation_from_rus
from keyboards.btn_report import BTN_REPORT


async def get_task(*, message: types.Message, state: FSMContext,
                   after_subject_selection: bool, bot: Bot) -> None:
    if after_subject_selection:
        subject = translation_from_rus.get(message.text)
        await state.update_data({'subject': subject})
    else:
        data = await state.get_data()
        subject = data.get('subject')

    response = await select_task(subject=subject)
    if response:
        task_text, id_task, correct_answer, file_path, \
            converted_image = response.text, response.id, \
            response.correct_answer, response.file_path, \
            response.converted_image
        await state.update_data({'correct_answer': correct_answer})
        await state.update_data({'cur_id_task': id_task})

        await message.answer(text=task_text,
                             reply_markup=types.ReplyKeyboardMarkup(
                                 [[BTN_REPORT]]))

        await bot.send_photo(message.chat.id, converted_image)
        await state.update_data({'image_sent': True})

        await message.answer(text='Введите ответ:')
    else:
        await message.answer(text='Произошла ошибка. Повторите попытку позже.')
        await message.answer(text='Выберите другой предмет:',
                             reply_markup=keyboard_subjects)
        await state.finish()
