from parse_data.convert.convert_html import convert_html_code_to_image
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.typing_for_parsing import DataForDB


def get_data_from_json(*, task: dict) -> DataForDB | None:
    if task.get('answer') and task.get('id'):
        id = task.get('id')

        level_name = task.get('levelName', '').strip()

        number_task = task.get('numberInGroup', '')
        number_task = number_task if number_task else -1

        correct_answer = task.get('answer', '')

        html_code = task.get('html').strip().replace('\n', ' ').replace('\r',
                                                                        ' ')
        html_code = delete_excess_data_in_tag(html_code)

        task_data = DataForDB(level_name=level_name, html=html_code,
                              number_task=number_task, id_task=id,
                              correct_answer=correct_answer)

        return task_data
