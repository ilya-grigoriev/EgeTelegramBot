from parse_data.convert.convert_html import convert_html_code_to_image
from parse_data.typing_for_parsing import DataForDB


def get_data_from_json(*, task: dict) -> DataForDB:
    id = task.get('id')

    level_name = task.get('levelName', '').strip()

    number_task = task.get('numberInGroup', '')
    number_task = number_task if number_task else -1

    correct_answer = task.get('answer', '')

    html_code = task.get('html').strip()
    converted_html_code = convert_html_code_to_image(html_code=html_code,
                                                     file_name=str(id))

    task_data = DataForDB(level_name=level_name, number_task=number_task,
                          img=converted_html_code,
                          correct_answer=correct_answer)

    return task_data
