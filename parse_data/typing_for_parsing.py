from dataclasses import dataclass


@dataclass
class DataForDB:
    id: int = -1
    level_name: str = ''
    number_task: int = -1
    img: str = ''
    correct_answer: str = ''
