from loguru import logger


def get_subject_id_from_json(*, subjects: list[dict], subject_name: str) -> int | None:
    current_subject_id = None
    for subject in subjects:
        if subject['name'] == subject_name:
            current_subject_id = subject['id']
            logger.info('Set id for subject')
            break
    return current_subject_id