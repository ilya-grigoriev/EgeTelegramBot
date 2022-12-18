from dataclasses import dataclass
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, List

from parse_data.format.format_data_in_tag import delete_excess_data_in_tag

id_task_from_db = int
type_subject_id = int
data_task = Dict[str, Optional[str | int]]
data_subjects = Optional[List[Dict[str, str]]]
data_from_json = Optional[List[data_task]]
converted_image_to_bytes = bytes
converted_images = Dict[str, Optional[converted_image_to_bytes]]


@dataclass
class DataForDB:
    id_task: id_task_from_db = -1
    level_name: str = ''
    number_task: Optional[int] = -1
    html: str = ''
    correct_answer: str = ''


@dataclass
class DataForTG:
    text: str
    id: int
    correct_answer: str
    file_path: str
    converted_image: bytes


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
