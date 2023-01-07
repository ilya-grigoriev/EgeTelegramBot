from typing import Union

from parse_data.format.format_image import crop_image as crop_image

async def format_data_from_db(
    *, data: Union[tuple[str], None]
) -> tuple[str, int, str, str]: ...
