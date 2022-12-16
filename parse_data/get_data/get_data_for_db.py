from parse_data.typing_for_parsing import DataForDB, Task, data_from_json


def get_data_from_json(*, task: data_from_json) -> DataForDB | None:
    formatted_task = Task(**task)
    if formatted_task.answer and formatted_task.id:
        task_data = DataForDB(level_name=formatted_task.level_name,
                              html=formatted_task.html,
                              number_task=formatted_task.number_task,
                              id_task=formatted_task.id,
                              correct_answer=formatted_task.answer)

        return task_data
    return None
