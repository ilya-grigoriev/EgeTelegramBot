from parse_data.typing_for_parsing import DataForDB


def format_data_for_db(*, task: DataForDB) -> str:
    total_request = f'(\"{task.id_task}\", \"{task.level_name}\", {task.number_task}, \"{task.html}\", \"{task.correct_answer}\")'
    return total_request
