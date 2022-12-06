import io
import os
import html2image
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from PIL import Image

from parse_data.format.format_html import format_html_code
from parse_data.get_data.get_urls import get_urls_from_html_code


def convert_html_code_to_image(*, html_code: str, file_name: str) -> None:
    image = html2image.Html2Image()
    # html_file_name = f'{file_name}.html'
    # with open(html_file_name, 'w') as file:
    #     file.write(html_code)

    # html_code = format_html_code(html_code=html_code)
    formatted_html = delete_excess_data_in_tag(tag=html_code)
    image.screenshot(html_str=formatted_html, save_as=file_name)
    # converted_image = convert_image_to_bytes(file_name=file_name)
    # return converted_image


if __name__ == '__main__':
    convert_html_code_to_image(html_code="""<!DOCTYPE html>
<html test="">
<head><title tasktype="InputTextMany">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435;
    &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435;
    &#x432;&#x432;&#x43E;&#x434;&#x430;</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta charset="utf-8">
    <link href="/Content/KimTemplate/kimTmp.css" rel="stylesheet">
    <link href="/Content/KimTemplate/kimTmpInputTextMany.css" rel="stylesheet">
    <link href="/Content/task-common.css" rel="stylesheet"/>
    <script src="/scripts/task-common.bundle.js"></script>
    <script src="/Scripts/tools.js"></script>
    <script src="/Scripts/InputTextManyTest.js"></script>
    <script src="/scripts/fipi-tools.js?rev=2"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
         MathJax.Hub.Config({messageStyle: "none"});
    </script>
</head>
<body bgcolor="#f5f5f5"><input id="AllowSymbolsCode"
                                                          type="hidden"
                                                          value=""> <input
        id="AnswerMinLength" type="hidden" value="0"> <input id="TaskId"
                                                             type="hidden"
                                                             value="4043">
<input id="AnswerMaxLength" type="hidden" value="10000">
<div id="hint" class="hint" name="hint">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435;
    &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435;
    &#x432;&#x432;&#x43E;&#x434;&#x430;
</div>
<div id="text" class="text custom-scroll-no" name="text">
    <div class="WordSection1"><p class="MsoNormal">Пакет молока стоит 40
        рублей. Пенсионерам магазин делает скидку 15%. Сколько рублей заплатит
        пенсионер за пакет молока?</p></div>
    <div style="margin-top: 10px;"><input id="answer_1" class="answer"
                                          number="1" type="text"
                                          placeholder="Введите ответ"></div>
</div>
</body>
</html>""",
                               id_task=23)
