"""Module help to converting file to bytes."""
from parse_data.check.check_data import check_args


def convert_image_to_bytes(*, file_name: str) -> bytes:
    """
    Convert image to bytes by filename.

    Parameters
    ----------
    file_name : str
        Image path.
    """
    check_args(file_name=file_name)

    converted_image = None
    with open(file_name, "rb") as image:
        to_bytes = image.read()
        converted_image = to_bytes
    image.close()
    return converted_image


if __name__ == "__main__":
    pass
