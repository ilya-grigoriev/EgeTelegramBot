import re


def delete_excess_data_in_tag(tag: str) -> str:
    tag = re.sub(
        r'<annotation[\s\d\w=\'-]+>((?!<)[\s\d\w=\'-@])+<\/annotation>', '',
        tag)
    tag = re.sub(r'\s{2,}', ' ', tag)
    tag = re.sub('<div[\w\s\d;=\"&#>]*</div>', ' ', tag)
    tag = re.sub("'", '"', tag)

    sources = re.findall(r'\/api\/docs\/byid\/\d+', tag)
    for source in sources:
        tag = re.sub(source, f'http://os.fipi.ru{source}', tag)

    tag = re.sub(r'<body (class="[\w\-\s]+")', '<body bgcolor="#f5f5f5"', tag)

    tag = re.sub(r'<input[\w\s\dА-Яа-яЁё=\"_\\]+>', '', tag)

    pattern = r'<script language="javascript"> ShowPictureQ\([\w\d\/_\.\"]+\);<\/script>'
    sources = re.findall(pattern, tag)
    pattern_for_href = r'(docs\/[\d\w]+\/[\d\w]+\/[\d\w]+\/[\d\w]+\.(png|jpg|gif|jpeg|webp|svg))'
    for source in sources:
        result_search = re.search(pattern_for_href, source)
        if result_search:
            href = result_search.group()
            source = re.sub(r'/', r'\/', source)
            source = re.sub(r'\(', r'\(', source)
            source = re.sub(r'\)', r'\)', source)
            source = re.sub(r'\.', r'\.', source)
            image = f'<img src="http://os.fipi.ru/{href}">'
            tag = re.sub(source, image, tag)

    tag = re.sub("'", '"', tag)

    return tag


if __name__ == '__main__':
    print(delete_excess_data_in_tag(
        """<!DOCTYPE html> <html test=""> <head> <title tasktype="InputTextMany">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435; &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435; &#x432;&#x432;&#x43E;&#x434;&#x430;</title> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> <meta charset="utf-8"> <link href="/Content/KimTemplate/kimTmp.css" rel="stylesheet"> <link href="/Content/KimTemplate/kimTmpInputTextMany.css" rel="stylesheet"> <link href="/Content/task-common.css" rel="stylesheet" /> <script src="/scripts/task-common.bundle.js"></script> <script src="/Scripts/tools.js"></script> <script src="/Scripts/InputTextManyTest.js"></script> <script src="/scripts/fipi-tools.js?rev=2"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({messageStyle: "none"}); </script> </head> <body bgcolor="#f5f5f5"> <input id="AllowSymbolsCode" type="hidden" value=""> <input id="AnswerMinLength" type="hidden" value="0"> <input id="TaskId" type="hidden" value="4306"> <input id="AnswerMaxLength" type="hidden" value="10000"> <div id="hint" class="hint" name="hint">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435; &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435; &#x432;&#x432;&#x43E;&#x434;&#x430;</div> <div id="text" class="text custom-scroll-no" name="text"> <table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" align="right"> <tr > <td valign="top"> <p class="MsoNormal" ><script language="javascript"> ShowPictureQ("docs/7180F95137BF9FEF48092553403ECAB5/questions/0BF88D65CFC989F4472412FE0E90A46D/xs3qstsrc0BF88D65CFC989F4472412FE0E90A46D_1_1384268921.gif");</script></p> </td> </tr> </table> <p class="MsoNormal">На клетчатой бумаге с размером клетки <math> <semantics> <mrow> <mn>1</mn><mo>&#x00D7;</mo><mn>1</mn> </mrow> </semantics> </math>&nbsp;изображён треугольник <math> <semantics> <mrow> <mi>A</mi><mi>B</mi><mi>C</mi> </mrow> </semantics> </math>. Найдите длину его средней линии, параллельной стороне <math> <semantics> <mrow> <mi>A</mi><mi>B</mi> </mrow> </semantics> </math>.</p> <p class="MsoNormal">&nbsp;</p> <p class="MsoNormal">&nbsp;</p> <p class="MsoNormal">&nbsp;</p> <p class="MsoNormal"><span >&nbsp;</span></p> <div style="margin-top: 10px;"> <input id="answer_1" class="answer" number="1" type="text" placeholder="Введите ответ"> </div> </div> </body> </html>"""))
