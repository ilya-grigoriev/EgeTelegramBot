from loguru import logger
from parse_data.typing_for_parsing import data_subjects, type_subject_id


def get_subject_id_from_json(*, subjects: data_subjects,
                             subject_name: str) -> type_subject_id:
    current_subject_id = -1
    if subjects:
        for subject in subjects:
            if subject.get('name') == subject_name:
                subject_id = subject.get('id')
                if isinstance(subject_id, int):
                    current_subject_id = subject.get('id')
                    logger.info('Set id for subject')
                    break
        return current_subject_id
    return current_subject_id
