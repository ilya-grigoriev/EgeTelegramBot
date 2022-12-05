import io
import os
import html2image
from PIL import Image

from parse_data.format.format_html import format_html_code
from parse_data.get_data.get_urls import get_urls_from_html_code


def convert_html_code_to_image(*, html_code: str, id_task: int) -> None:
    image = html2image.Html2Image()
    file_name = f'{id_task}.png'
    # html_file_name = f'{file_name}.html'
    # with open(html_file_name, 'w') as file:
    #     file.write(html_code)

    # html_code = format_html_code(html_code=html_code)
    image.screenshot(html_str=html_code, save_as=file_name)
    # converted_image = convert_image_to_bytes(file_name=file_name)
    # return converted_image


if __name__ == '__main__':
    convert_html_code_to_image(html_code="""<div class="WordSection1"><p class="MsoNormal"><span style="color:black">На рисунке жирными точками показана цена палладия, установленная Центробанком РФ во все рабочие дни с 1 по 27 октября 2010 года. <br> По горизонтали указаны числа месяца, по вертикали — цена палладия <br> в рублях за грамм. Для наглядности жирные точки на рисунке соединены линией. Определите по рисунку, какого числа цена палладия впервые поднялась выше 575 рублей за грамм.</span>
</p>
    <p class="MsoNormal" align="center" style="text-align:center"><span
            style="color:black"><img width="523" height="269"
                                     src="http://os.fipi.ru/api/docs/byid/82210"
                                     alt="Adobe Systems"></span></p></div>""",
                               file_name='test24.png')
