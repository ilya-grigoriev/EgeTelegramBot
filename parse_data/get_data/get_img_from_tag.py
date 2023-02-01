"""This module help to get image src from html code."""
import re
from typing import Sequence, Any


def get_img_url_from_tag(tag: str) -> Sequence[Any]:
    """
    Get internal links to images from html code.

    Parameters
    ----------
    tag: str
        Html code.

    Returns
    -------
    Sequence[Any]
        List of internal links to images.
    """
    pattern = r"\/api\/docs\/byid\/\d+"
    finding = re.findall(pattern, tag)
    return finding if finding else ""


if __name__ == "__main__":
    print(get_img_url_from_tag("a"))
