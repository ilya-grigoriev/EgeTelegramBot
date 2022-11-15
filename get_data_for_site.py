import requests

from config import headers


def get_response_from_site(url: str, mode='get', *, cookies=None,
                           session=None) -> (
        requests.Response | None, str | None):
    response = None
    status_code = None
    if mode == 'get':
        if session:
            response = session.get(url, headers=headers,
                                   cookies=cookies)
        else:
            response: requests.Response = requests.get(url, headers=headers,
                                                       cookies=cookies)
        status_code = response.status_code
    return response, status_code
