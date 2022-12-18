def convert_image_to_bytes(*, file_name: str) -> bytes:
    converted_image = None
    with open(file_name, "rb") as image:
        to_bytes = image.read()
        converted_image = to_bytes
    image.close()
    return converted_image


if __name__ == '__main__':
    pass
