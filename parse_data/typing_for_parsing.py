from dataclasses import dataclass
from typing import TypeVar

id_task_from_db = int


@dataclass
class DataForDB:
    id_task: id_task_from_db = -1
    level_name: str = ''
    number_task: int = -1
    html: str = ''
    correct_answer: str = ''
