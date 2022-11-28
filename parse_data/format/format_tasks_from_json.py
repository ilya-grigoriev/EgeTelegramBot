from bs4 import BeautifulSoup

from parse_data.format.format_description_answers import \
    format_desc_and_answers_for_task
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.typing_for_parsing import DataForDB
from parse_data.get_data.get_img_from_tag import get_img_url_from_tag


def format_tasks(tasks: list[dict], subject_id: int) -> list[DataForDB]:
    data = []
    for n, task in enumerate(tasks, start=1):
        if n == 265:
            pass
        level_name = task.get('levelName', '').strip()

        number_task = task.get('numberInGroup', '')
        number_task = number_task if number_task else -1

        task_title = task.get('taskTitle', '').strip()

        text = task.get('docHtml', '')
        if text:
            text = delete_excess_data_in_tag(
                BeautifulSoup(text, 'html.parser').text.strip())
        else:
            text = ''

        correct_answer = task.get('answer', '').strip()

        img = get_img_url_from_tag(task.get('taskTextWord'))

        if img:
            img = '\n'.join(img)
            task_text = delete_excess_data_in_tag(task.get('taskTextWord'))
        else:
            task_text = delete_excess_data_in_tag(
                task.get('taskText', '').strip())
        task_text = BeautifulSoup(task_text, 'html.parser').text.strip()

        desk_for_task = format_desc_and_answers_for_task(task.get('html', ''))
        answers = None

        if desk_for_task:
            answers = desk_for_task.get('answers')
            task_text = desk_for_task.get(
                'task_text') or delete_excess_data_in_tag(task_text)

            task_data = DataForDB(level_name=level_name,
                                  number_task=number_task,
                                  task_title=task_title, task_text=task_text,
                                  text=text, answers=answers,
                                  correct_answer=correct_answer)

            data.append(task_data)
        elif subject_id == 2 and correct_answer:
            task_data = DataForDB(level_name=level_name,
                                  number_task=number_task,
                                  task_title=task_title, task_text=task_text,
                                  correct_answer=correct_answer, img=img)

            data.append(task_data)
    return data
