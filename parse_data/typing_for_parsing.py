from dataclasses import dataclass


@dataclass
class DataForDB:
    id_task: int = -1
    level_name: str = ''
    number_task: int = -1
    html: str = ''
    correct_answer: str = ''
