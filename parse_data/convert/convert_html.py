import os

from config_for_parsing import path_dir
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.typing_for_parsing import DataForDB
from parse_data.browser_for_parsing import make_screenshot


async def convert_html_code_to_image(*, html_code: str,
                                     id_task: DataForDB.id_task) -> str:
    formatted_html = delete_excess_data_in_tag(tag=html_code)

    file_path = f'{path_dir}\\{id_task}'
    html_file = f'{file_path}.html'
    jpg_file = f'{file_path}.jpg'
    with open(html_file, mode='w', encoding='utf-8') as file:
        file.write(formatted_html)

    await make_screenshot(file_path_for_open=html_file,
                          file_path_for_save=jpg_file)

    os.remove(html_file)

    return jpg_file


if __name__ == '__main__':
    #     convert_html_code_to_image(html_code="""<!DOCTYPE html>
    # <html test="">
    # <head><title tasktype="InputTextMany">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435;
    #     &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435;
    #     &#x432;&#x432;&#x43E;&#x434;&#x430;</title>
    #     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    #     <meta charset="utf-8">
    #     <link href="/Content/KimTemplate/kimTmp.css" rel="stylesheet">
    #     <link href="/Content/KimTemplate/kimTmpInputTextMany.css" rel="stylesheet">
    #     <link href="/Content/task-common.css" rel="stylesheet"/>
    #     <script src="/scripts/task-common.bundle.js"></script>
    #     <script src="/Scripts/tools.js"></script>
    #     <script src="/Scripts/InputTextManyTest.js"></script>
    #     <script src="/scripts/fipi-tools.js?rev=2"></script>
    #     <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=MML_HTMLorMML"></script>
    #     <script type="text/x-mathjax-config">
    #          MathJax.Hub.Config({messageStyle: "none"});
    #     </script>
    # </head>
    # <body bgcolor="#f5f5f5"><input id="AllowSymbolsCode"
    #                                                           type="hidden"
    #                                                           value=""> <input
    #         id="AnswerMinLength" type="hidden" value="0"> <input id="TaskId"
    #                                                              type="hidden"
    #                                                              value="4043">
    # <input id="AnswerMaxLength" type="hidden" value="10000">
    # <div id="hint" class="hint" name="hint">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435;
    #     &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435;
    #     &#x432;&#x432;&#x43E;&#x434;&#x430;
    # </div>
    # <div id="text" class="text custom-scroll-no" name="text">
    #     <div class="WordSection1"><p class="MsoNormal">Пакет молока стоит 40
    #         рублей. Пенсионерам магазин делает скидку 15%. Сколько рублей заплатит
    #         пенсионер за пакет молока?</p></div>
    #     <div style="margin-top: 10px;"><input id="answer_1" class="answer"
    #                                           number="1" type="text"
    #                                           placeholder="Введите ответ"></div>
    # </div>
    # </body>
    # </html>""",
    #                                id_task=23)
    print(convert_html_code_to_image(html_code="""<!DOCTYPE html>
<html test="">
<head>
    <title tasktype="InputTextMany">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435;
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
<body class="no-answers custom-scroll-no noselect">
<input id="AllowSymbolsCode" type="hidden" value="">
<input id="AnswerMinLength" type="hidden" value="0">
<input id="TaskId" type="hidden" value="4047">
<input id="AnswerMaxLength" type="hidden" value="10000">
<div id="hint" class="hint" name="hint">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435;
    &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435;
    &#x432;&#x432;&#x43E;&#x434;&#x430;
</div>
<div id="text" class="text custom-scroll-no" name="text">
    <p class="MsoNormal">Найдите корень уравнения
        <math>
            <semantics>
                <mrow>
                    <msqrt>
                        <mrow>
                            <mn>2</mn>
                            <mi>x</mi>
                            <mo>+</mo>
                            <mn>31</mn>
                        </mrow>
                    </msqrt>
                    <mo>=</mo>
                    <mn>9</mn>
                </mrow>
                <annotation encoding='MathType-MTEF'>
                    MathType@MTEF@5@5@+=feaaguart1ev2aqatCvAUfeBSjuyZL2yd9gzLbvyNv2CaerbuLwBLnhiov2DGi1BTfMBaeXatLxBI9gBaebbnrfifHhDYfgasaacH80rpy0dbba9q8qqaqpepac8Eeei0lXdbrFr0xc9xq=hbr=hc9asFHe9Fne9FGe9q8qqaq=dir=f0dc9q8qq0xh9Fee9Fue9vapdbaqaaeGaciGaaiaabeqaaeaabaWaaaGcbaWaaOaaaeaacaaIYaGaamiEaiabgUcaRiaaiodacaaIXaaaleqaaOGaeyypa0JaaGyoaaaa@370E@
                </annotation>
            </semantics>
        </math>
        .<span></span></p>
    <div style="margin-top: 10px;">
        <input id="answer_1" class="answer" number="1" type="text"
               placeholder="Введите ответ">
    </div>
</div>
</body>
</html>
"""))
