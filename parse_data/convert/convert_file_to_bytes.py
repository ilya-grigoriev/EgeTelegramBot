"""This module help to converting file to bytes."""


def convert_image_to_bytes(*, file_name: str) -> bytes:
    """Converting image to bytes by filename.

    Parameters
    ----------
    file_name : str
        Image path.
    """

    converted_image = None
    with open(file_name, "rb") as image:
        to_bytes = image.read()
        converted_image = to_bytes
    image.close()
    return converted_image


if __name__ == "__main__":
    pass
