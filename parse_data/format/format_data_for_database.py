import re

from parse_data.typing_for_parsing import DataTaskOfSubtopic


def format_data_for_db(*, task: DataTaskOfSubtopic, number_task: int,
                       is_detailed: bool, number_subtopic: int) -> str:
    task.task_desc_html = re.sub("'", '"', task.task_desc_html)
    task.text_for_task_html = re.sub("'", '"', task.text_for_task_html)
    task.solution_html = re.sub("'", '"', task.solution_html)

    if number_subtopic != -1:
        task_section = f'{number_task}/{number_subtopic}'
    else:
        task_section = number_task
    total_request = f"('{task_section}', {task.id_task}, {str(is_detailed).lower()}, '{task.task_desc_html}', '{task.text_for_task_html}', '{task.solution_html}', '{task.answer}')"
    return total_request
