from dataclasses import dataclass
from pydantic import BaseModel, Field, validator
from typing import Optional

from parse_data.format.format_data_in_tag import delete_excess_data_in_tag

id_task_from_db = int
data_from_json = dict


@dataclass
class DataForDB:
    id_task: id_task_from_db = -1
    level_name: str = ''
    number_task: int = -1
    html: str = ''
    correct_answer: str = ''


class Task(BaseModel):
    id: Optional[int]
    level_name: str = Field(alias='levelName')
    number_task: Optional[int] = Field(alias='numberInGroup')
    answer: str
    html: str

    @validator('level_name', 'answer')
    def check_truth_str_obj(cls, val):
        return val.strip() if val else ''

    @validator('html')
    def check_and_format_html(cls, html):
        html_code = html.strip().replace('\n', ' ').replace('\r', ' ')

        html_code = delete_excess_data_in_tag(html_code)
        return html_code

    @validator('id', 'number_task')
    def check_truth_int_obj(cls, val):
        return val if val else -1
