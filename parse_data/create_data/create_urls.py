"""Module help to create urls."""
import asyncio

from parse_data.check.check_data import check_args
from parse_data.typing_for_parsing import (
    typing_data_payload,
    typing_url,
    typing_urls_with_data,
)


async def create_urls_for_request(
    *, url: typing_url, max_skip: int
) -> typing_urls_with_data:
    """Create urls to https://ege.sdamgia.ru/ for request.

    Parameters
    ----------
    url : typing_url
        Link to the website.
    max_skip : int
        Value for data payload of request.

    Returns
    -------
    type_urls_with_data
        List of urls with data payload for request.
    """
    check_args(url=url, max_skip=max_skip)

    urls_with_data = []
    skip = 5
    max_amount = max_skip
    if url:
        while max_amount >= 5:
            max_amount -= 5
            data_payload: typing_data_payload = {
                "ajax": "1",
                "skip": skip,
                "max_skip": max_skip,
            }
            urls_with_data.append((url, data_payload))
            skip += 5
        final_data_payload: typing_data_payload = {
            "ajax": "1",
            "skip": max_skip,
            "max_skip": max_skip,
        }
        urls_with_data.append((url, final_data_payload))
        urls_with_data.append((url, {}))  # for first call website
    return urls_with_data


if __name__ == "__main__":
    print(asyncio.run(create_urls_for_request(url="a", max_skip=116)))
