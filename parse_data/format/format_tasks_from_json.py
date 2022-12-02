from parse_data.typing_for_parsing import DataForDB


def format_tasks(tasks: list[dict]) -> list[DataForDB]:
    data = []
    for task in tasks:
        level_name = task.get('levelName', '').strip()

        number_task = task.get('numberInGroup', '')
        number_task = number_task if number_task else -1

        correct_answer = task.get('answer', '').strip()

        html_code = task.get('html').strip()

        task_data = DataForDB(level_name=level_name, number_task=number_task,
                              img=html_code, correct_answer=correct_answer)

        data.append(task_data)
    return data
