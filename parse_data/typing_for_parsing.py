from dataclasses import dataclass


@dataclass
class DataForDB:
    id: int = -1
    level_name: str = ''
    number_task: int = -1
    task_title: str | None = ''
    text: str | None = ''
    task_text: str | None = ''
    answers: str | None = ''
    correct_answer: str = ''
    img: str | None = None
