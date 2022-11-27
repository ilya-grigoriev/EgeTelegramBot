import re
from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass(init=True)
class DataFromDB:
    id: int
    level_name: str
    number_task: int
    task_title: str
    text: str
    task_text: str
    answers: str
    correct_answer: str
    img: str


@dataclass
class DataForDB:
    level_name: str
    number_task: int
    task_title: str
    task_text: str
    text: str
    answers: str
    correct_answer: str
    img: str


def format_answers_options(answers: list[str]) -> list[str]:
    formatted_answers = []
    for count, answer in enumerate(answers, start=1):
        formatted_answers.append(f'{count}) {answer}')
    return formatted_answers


def delete_excess_data_in_tag(tag: str) -> str:
    tag = re.sub('<math>[\w\W]+</math>', '', tag)
    tag = re.sub('MathType[A-Za-z\d@+=]+', '', tag)
    tag = re.sub('\s{2,}', ' ', tag)
    return tag


def format_desc_and_answers_for_task(text: str) -> dict | None:
    data = dict()
    soup = BeautifulSoup(text, 'html.parser')
    list_answers = soup.find_all('div', attrs={'class': 'answer'})
    if list_answers:
        task_text = soup.find('div', attrs={'name': 'text'}).text
        data['task_text'] = task_text.strip().strip('\n')
        answers_options = [
            delete_excess_data_in_tag(answer.text.strip().strip('\n')) for
            answer in list_answers]
        data['answers'] = format_answers_options(answers_options)
        return data
    return None


def format_tasks(tasks: list[dict]) -> list[DataForDB]:
    data = []
    for task in tasks:
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

        img = task.get('img', '').strip()

        task_text = task.get('taskText', '').strip()
        task_text = BeautifulSoup(task_text, 'html.parser').text.strip()

        desk_for_task = format_desc_and_answers_for_task(task.get('html', ''))

        if desk_for_task:
            answers = desk_for_task.get('answers')
            task_text = desk_for_task.get(
                'task_text') or delete_excess_data_in_tag(task_text)

            task_data = DataForDB(level_name, number_task,
                                  task_title, task_text,
                                  text, answers, correct_answer, img)

            data.append(task_data)
    return data


def format_data_for_db(*, task: DataForDB) -> str:
    answers = task.answers
    if isinstance(answers, list):
        answers = '\n'.join(task.answers)
    total_request = f"('{task.level_name}', {task.number_task}, '{task.task_title}', '{task.task_text}', '{task.text}', '{answers}', '{task.correct_answer}', '{task.img}')"
    return total_request


def format_data_from_db(data: tuple[str] | None) -> str:
    total_text = ''
    if data is not None:
        data = DataFromDB(*data)
        total_text += f"Уровень: {data.level_name}\n"
        if data.number_task != -1:
            total_text += f"Номер задания: {data.number_task}\n"
        total_text += f"{data.task_title}\n"
        if data.text:
            total_text += f"Текст задания:\n"
            total_text += f"{data.text}\n"
        total_text += f"Задание:\n"
        total_text += f"{data.task_text}\n"
        total_text += f"Варианты ответов:\n"
        total_text += f"{data.answers}"
    return total_text
