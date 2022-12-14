class DataForDB:
    id_task: int
    level_name: str
    number_task: int
    html: str
    correct_answer: str
    def __init__(self, id_task, level_name, number_task, html, correct_answer) -> None: ...
