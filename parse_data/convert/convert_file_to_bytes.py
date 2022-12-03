import io
from PIL import Image


def convert_image_to_bytes(*, file_name: str) -> io.BytesIO:
    converted_image = io.BytesIO()
    image = Image.open(file_name)
    image = image.convert('RGB')
    image.save(converted_image, "JPEG")
    converted_image.seek(0)
    # converted_image = io.BytesIO(converted_image.read())
    return converted_image.read()


if __name__ == '__main__':
    image = convert_image_to_bytes(
        file_name=r'C:\Users\ilia0\PycharmProjects\EgeTelegramBot\test\image_for_test.jpg')
    image = Image.open(image)
    image.show()
