from bs4 import BeautifulSoup


def format_choosing_answers(answers: list[str]) -> list[str]:
    formatted_answers = []
    for count, answer in enumerate(answers, start=1):
        formatted_answers.append(f'{count}) {answer}')
    return formatted_answers


def format_desc_for_task(text: str) -> dict:
    data = dict()
    soup = BeautifulSoup(text, 'html.parser')
    task_text = soup.find('div', attrs={'name': 'text'}).text
    data['task_text'] = task_text.strip().strip('\n')
    answers = [answer.text.strip() for answer in
               soup.find_all('div', attrs={'class': 'answer'})]
    data['answers'] = format_choosing_answers(answers)
    return data


def format_tasks(tasks: list[dict]) -> list[dict]:
    data = []
    for task in tasks:
        dict_task = dict()

        level_name = task.get('levelName', '').strip()
        dict_task['level_name'] = level_name

        task_title = task.get('taskTitle', '').strip()
        dict_task['task_title'] = task_title

        correct_answer = task.get('answer', '').strip()
        dict_task['correct_answer'] = correct_answer

        desc_for_task = format_desc_for_task(task.get('html', '').strip())
        dict_task['desc_for_task'] = desc_for_task

        data.append(dict_task)
    return data


def format_data_for_db(task: dict[str, dict[str]]) -> str:
    level_name = task.get('level_name', '')
    task_title = task.get('task_title', '')
    desc_for_task = task.get('desc_for_task', '')
    correct_answer = task.get('correct_answer', '')
    task_text = ''
    answers = ''
    if desc_for_task:
        task_text = desc_for_task.get('task_text', '')
        answers = '\n'.join(desc_for_task.get('answers', ''))
    total_request = f"('{level_name}', '{task_title}', '{task_text}', '{answers}', '{correct_answer}')"
    return total_request
