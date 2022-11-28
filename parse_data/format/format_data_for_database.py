from parse_data.typing_for_parsing import DataForDB


def format_data_for_db(*, subject_id: int, task: DataForDB) -> str:
    answers = task.answers
    if isinstance(answers, list):
        answers = '\n'.join(task.answers)
    if subject_id != 2:
        total_request = f"('{task.level_name}', {task.number_task}, '{task.task_title}', '{task.task_text}', '{task.text}', '{answers}', '{task.correct_answer}')"
    else:
        total_request = f"('{task.level_name}', {task.number_task}, '{task.task_title}', '{task.task_text}', '{task.correct_answer}', '{task.img}')"
    return total_request
