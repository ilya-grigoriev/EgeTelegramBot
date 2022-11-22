import re

from bs4 import BeautifulSoup


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


def format_desc_and_answers_for_task(text: str) -> dict:
    data = dict()
    soup = BeautifulSoup(text, 'html.parser')
    list_answers = soup.find_all('div', attrs={'class': 'answer'})
    if not list_answers:
        answers = soup.find('div', attrs={'name': 'text'}).text.replace('\n',
                                                                        '')
        data['answers'] = answers
    else:
        task_text = soup.find('div', attrs={'name': 'text'}).text
        data['task_text'] = task_text.strip().strip('\n')
        answers_options = [
            delete_excess_data_in_tag(answer.text.strip().strip('\n')) for
            answer in list_answers]
        data['answers'] = format_answers_options(answers_options)
    return data


def format_tasks(tasks: list[dict]) -> list[dict]:
    data = []
    i = 0
    for task in tasks:
        dict_task = dict()

        level_name = task.get('levelName', '').strip()
        dict_task['level_name'] = level_name

        number_task = task.get('numberInGroup')
        dict_task['number_task'] = number_task

        task_title = task.get('taskTitle', '').strip()
        dict_task['task_title'] = task_title

        text = task.get('docHtml')
        if text:
            text = delete_excess_data_in_tag(
                BeautifulSoup(text, 'html.parser').text.strip())
        else:
            text = ''
        dict_task['text'] = text

        correct_answer = task.get('answer', '').strip()
        dict_task['correct_answer'] = correct_answer

        task_text = task.get('taskText', '').strip()
        task_text = BeautifulSoup(task_text, 'html.parser').text.strip()
        if i == 9:
            pass
        desk_for_task = format_desc_and_answers_for_task(task.get('html', ''))
        desk_for_task['task_text'] = desk_for_task.get(
            'task_text') or delete_excess_data_in_tag(task_text)
        dict_task['desc_for_task'] = desk_for_task

        i += 1
        data.append(dict_task)
    return data


def format_data_for_db(task: dict[str, dict[str]]) -> str:
    level_name = task.get('level_name', '')
    number_task = task.get('number_task')
    number_task = number_task if number_task else -1
    task_title = task.get('task_title', '')
    text = task.get('text')
    desc_for_task = task.get('desc_for_task', '')
    correct_answer = task.get('correct_answer', '')
    task_text = ''
    answers = ''
    if desc_for_task:
        task_text = desc_for_task.get('task_text', '')
        answers = desc_for_task.get('answers')
        if isinstance(answers, list):
            answers = '\n'.join(desc_for_task.get('answers', ''))
    total_request = f"('{level_name}', {number_task}, '{task_title}', '{task_text}', '{text}', '{answers}', '{correct_answer}')"
    return total_request

# def format_data_from_db(data: tuple[str]) -> list[str]:
