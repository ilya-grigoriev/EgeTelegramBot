import requests
from logger_for_project import my_logger
from parse_data.typing_for_parsing import data_subjects
from typing import Any
from parse_data.config_for_parsing import headers_for_get_subject_ids


def get_json_of_data_subject(*, subject_name_en: str) -> data_subjects | Any:
    url = f"https://{subject_name_en}-ege.sdamgia.ru/newapi/general"
    headers_for_get_subject_ids.update({"authority": "math-ege.sdamgia.ru"})
    response = requests.get(url, headers=headers_for_get_subject_ids)
    if response.status_code == 200:
        my_logger.info("Get subject ids from json")
        data_subject = response.json().get("constructor")
        my_logger.info("Data received")
        return data_subject
    else:
        my_logger.error(f"Connection is failed. URL: {url}")
        return None


if __name__ == "__main__":
    print(get_json_of_subject_ids(subject_name_rus="Русский язык"))
