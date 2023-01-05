import re

from bs4 import BeautifulSoup
from parse_data.typing_for_parsing import DataTaskOfSubtopic


def get_data_of_task_for_subtopic(*, html: str):
    bs = BeautifulSoup(html, 'html.parser')
    task_html = bs.find('div', attrs={'class': 'nobreak'})
    task_desc_html = task_html.find('div', attrs={'id': re.compile('body\d+')})
    task_desc_html = re.sub("'", '"', str(task_desc_html))
    text_for_task_html = ''
    searching = re.search('id="text\d+"', str(task_html))
    if searching:
        text_for_task_html = task_html.find('div', attrs={
            'id': re.compile('text\d+')})
    return str(task_html), DataTaskOfSubtopic(
        task_desc_html=str(task_desc_html),
        text_for_task_html=str(text_for_task_html))
