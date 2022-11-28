from parse_data.typing_for_parsing import DataForDB


def format_data_from_db(*, subject: str, data: tuple[str] | None) -> tuple[
    str, None]:
    total_text = ''
    if data is not None:
        data = DataForDB(*data)
        total_text += f"Уровень: {data.level_name}\n"
        if data.number_task != -1:
            total_text += f"Номер задания: {data.number_task}\n"
        total_text += f"{data.task_title}\n"
        if data.text:
            total_text += f"Текст задания:\n"
            total_text += f"{data.text}\n"
        total_text += f"Задание:\n"
        total_text += f"{data.task_text}\n"
        if subject != 'math':
            total_text += f"Варианты ответов:\n"
            total_text += f"{data.answers}"
        elif subject == 'math' and data.img:
            total_text += 'Приложенные картинки нужно подставить в квадратные скобки (каждой картинке соответствует своя пара квадратных скобок)'

    return total_text, data.img if subject == 'math' else total_text
