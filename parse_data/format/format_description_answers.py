from bs4 import BeautifulSoup

from parse_data.format.format_answers import format_answers_options
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag


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
