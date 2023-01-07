from PIL import Image


def crop_image(*, file_path: str) -> None:
    image = Image.open(file_path)
    image = image.convert("RGB")
    pixels = image.load()
    w, h = image.size
    access = True
    hor_x = 0
    vert_y = 0

    for x in range(w - 1, -1, -1):
        if access:
            for y in range(h):
                if pixels[x, y] != (245, 245, 245, 255):
                    hor_x = x
                    access = False
                    break
        else:
            access = True
            break

    for y in range(h - 1, -1, -1):
        if access:
            for x in range(w):
                if pixels[x, y] != (245, 245, 245, 255):
                    vert_y = y
                    access = False
                    break
        else:
            break
    image.crop((0, 0, hor_x, vert_y + 10)).save(file_path)


if __name__ == "__main__":
    crop_image(file_path=r"C:\Users\ilia0\PycharmProjects\EgeTelegramBot\4076.jpg")
