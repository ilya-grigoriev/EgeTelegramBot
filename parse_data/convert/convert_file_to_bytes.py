import io
from PIL import Image


def convert_image_to_bytes(*, file_name: str) -> io.BytesIO:
    # converted_image = io.BytesIO()
    #
    # image = Image.open(file_name)
    # image = image.convert('RGBA')
    # #
    # image.save(converted_image, "PNG")
    # converted_image.seek(0)
    # converted_image = io.BytesIO(converted_image.read())
    img = Image.open(file_name)
    bytes_io = io.BytesIO()
    img.save(bytes_io, format='PNG')
    converted_image = bytes_io.getvalue()
    return io.BytesIO(converted_image)


if __name__ == '__main__':
    image = convert_image_to_bytes(
        file_name=r'C:\Users\ilia0\PycharmProjects\EgeTelegramBot\test\image_for_test.jpg')
    image = Image.open(image)
    image.show()
