import re


def format_html_code(*, html_code: str) -> str:
    sources = re.findall('\/api\/docs\/byid\/\d+', html_code)
    for source in sources:
        html_code = re.sub(source, f'http://os.fipi.ru{source}', html_code)
    return html_code


if __name__ == '__main__':
    print(format_html_code(
        html_code="""<div class="WordSection1"><p class="MsoNormal" style='margin-bottom:6.0pt'>На рисунке жирными точкамипоказана цена унции золота на момент закрытия биржевых торгов во все рабочиедни с 11 по 27 июля 2000 года. По горизонтали указываются числа месяца, повертикали — цена унции золота в долларах США. Для наглядности жирные точки нарисунке соединены линией. Определите по рисунку, какого числа цена унции золотана момент закрытия торгов была наибольшей за указанный период.</p><p class="MsoNormal" align="center" style='text-align:center'><img width="385" height="318" src="/api/docs/byid/78133" alt="Adobe Systems"></p></div>"""))
