from parse_data.typing_for_parsing import id_task_from_db


async def convert_html_code_to_image(*, html_code: str,
                                     id_task: id_task_from_db) -> str: ...
