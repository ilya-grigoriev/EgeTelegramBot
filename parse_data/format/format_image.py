"""This module help to format image."""
import io

from typing import IO
from PIL import Image, ImageDraw, ImageOps


def crop_image(*, image_to_bytes: bytes) -> IO[bytes]:
    """
    Remove empty space in the image.

    Parameters
    ----------
    image_to_bytes: bytes
        Image is converted to bytes.

    Returns
    -------
    IO[bytes]
        Image without empty space converted to bytes.
    """

    image = Image.open(io.BytesIO(image_to_bytes))
    image = image.convert("RGB")
    ImageDraw.floodfill(image, xy=(0, 0), value=(255, 255, 255), thresh=10)

    bbox = ImageOps.invert(image).getbbox()
    trimmed = image.crop(bbox)

    res = ImageOps.expand(trimmed, border=10, fill=(255, 255, 255))
    res = ImageOps.expand(res, border=5, fill=(0, 0, 0))
    res = ImageOps.expand(res, border=5, fill=(255, 255, 255))

    buf = io.BytesIO()
    res.save(buf, format="PNG")
    buf.seek(0)
    return buf
