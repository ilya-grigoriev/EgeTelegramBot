import requests

from config import headers


def get_content_from_site(url: str, mode='get') -> (
        requests.Response | None, str | None):
    response = None
    status_code = None
    if mode == 'get':
        response: requests.Response = requests.get(url, headers=headers)
        status_code = response.status_code
    return response.content, status_code
