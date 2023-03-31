"""Module is designed for checking subject name."""
from parse_data import exceptions_for_parsing
from parse_data.config_for_parsing import subjects_en


def check_arg_subject_name(subject_name: str):
    """
    Check argument of subject name.

    Parameters
    ----------
    subject_name : str
    """
    if subject_name not in subjects_en:
        message = 'Variable "subject_name_en" not in list of subjects.'
        raise exceptions_for_parsing.WrongSubjectNameEnglish(message)
