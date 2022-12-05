import re


def get_urls_from_html_code(*, html_code: str) -> list[str]:
    urls = re.findall('http:\/\/os.fipi.ru\/api\/docs\/byid\/\d+', html_code)
    return urls