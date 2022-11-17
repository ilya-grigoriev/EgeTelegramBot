from bs4 import BeautifulSoup


def format_choosing_answers(answers: list[str]) -> list[str]:
    formatted_answers = []
    for count, answer in enumerate(answers, start=1):
        formatted_answers.append(f'{count}) {answer}')
    return formatted_answers


def format_desc_for_task(text: str) -> dict:
    data = dict()
    soup = BeautifulSoup(text, 'html.parser')
    text_task = soup.find('div', attrs={'name': 'text'}).text
    data['text_task'] = text_task.strip('\n')
    answers = [answer.text.strip() for answer in
               soup.find_all('div', attrs={'class': 'answer'})]
    data['answers'] = format_choosing_answers(answers)
    return data


def format_tasks(tasks: list[dict]) -> list[list[str, dict]]:
    data = []
    for task in tasks:
        level_name = task.get('levelName', '').strip()
        task_title = task.get('taskTitle', '').strip()
        correct_answer = task.get('answer', '').strip()
        desc_for_task = format_desc_for_task(task.get('html', '').strip())
        data.append([level_name, task_title, desc_for_task, correct_answer])
    return data
