"""Module is designed for checking path."""
import os

from parse_data import exceptions_for_parsing


def check_arg_path_pdf(path_pdf: str):
    """
    Check argument of pdf filepath.

    Parameters
    ----------
    path_pdf : str
    """
    if not isinstance(path_pdf, str):
        raise exceptions_for_parsing.FilePathIsNotStr
    if not os.path.isfile(path_pdf):
        raise FileNotFoundError


def check_arg_path_image(path_image: str):
    """
    Check argument of image filepath.

    Parameters
    ----------
    path_image : str
    """
    if not isinstance(path_image, str):
        raise exceptions_for_parsing.FilePathIsNotStr
    if not os.path.isfile(path_image):
        raise FileNotFoundError


def check_arg_file_name(file_name: str):
    """
    Check argument of filename path.

    Parameters
    ----------
    file_name : str
    """
    if not isinstance(file_name, str):
        raise exceptions_for_parsing.FilePathIsNotStr
    if not os.path.isfile(file_name) or not file_name:
        raise FileNotFoundError
