from typing import Optional, List

from parse_data.typing_for_parsing import DataSubtopic, data_task


def get_data_from_dict(*, data, number_task: int) -> List[DataSubtopic]:
    subtopic_id = data.get('id')
    tasks = data.get('tasks')
    formatted_tasks = []
    for task in tasks:
        task_data = DataSubtopic(number_task, subtopic_id, task.get('html'),
                              task.get('solution_html'), task.get('answer'))
        formatted_tasks.append(task_data)
    return formatted_tasks
