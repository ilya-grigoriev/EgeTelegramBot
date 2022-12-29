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
    pattern_for_href = r'(docs\/[\d\w]+\/[\d\w]+\/[\d\w]+\/[\d\w]+\.png)'
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
        """<!DOCTYPE html> <html test=""> <head> <title tasktype="InputTextMany">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435; &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435; &#x432;&#x432;&#x43E;&#x434;&#x430;</title> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> <meta charset="utf-8"> <link href="/Content/KimTemplate/kimTmp.css" rel="stylesheet"> <link href="/Content/KimTemplate/kimTmpInputTextMany.css" rel="stylesheet"> <link href="/Content/task-common.css" rel="stylesheet" /> <script src="/scripts/task-common.bundle.js"></script> <script src="/Scripts/tools.js"></script> <script src="/Scripts/InputTextManyTest.js"></script> <script src="/scripts/fipi-tools.js?rev=2"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({messageStyle: "none"}); </script> </head> <body bgcolor="#f5f5f5"> <input id="AllowSymbolsCode" type="hidden" value=""> <input id="AnswerMinLength" type="hidden" value="0"> <input id="TaskId" type="hidden" value="4044"> <input id="AnswerMaxLength" type="hidden" value="10000"> <div id="hint" class="hint" name="hint">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435; &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435; &#x432;&#x432;&#x43E;&#x434;&#x430;</div> <div id="text" class="text custom-scroll-no" name="text"> <p class="MsoNormal">На рисунке жирными точками показана цена унции золота на момент закрытия биржевых торгов во все рабочие дни с 11 по 27 июля 2000 года. По горизонтали указываются числа месяца, по вертикали <math> <semantics> <mo>&#x2014;</mo> </semantics> </math>&nbsp;цена унции золота в долларах США. Для наглядности жирные точки на рисунке соединены линией. Определите по рисунку, какого числа цена унции золота на момент закрытия торгов была наибольшей за указанный период.</p> <p class="MsoNormal" align="center"><script language="javascript"> ShowPictureQ("docs/7180F95137BF9FEF48092553403ECAB5/questions/C62C7B3FE63586F946F9845820A43203/xs3qstsrcC62C7B3FE63586F946F9845820A43203_1_1326808337.png");</script><span></span></p> <div style="margin-top: 10px;"> <input id="answer_1" class="answer" number="1" type="text" placeholder="Введите ответ"> </div> </div> </body> </html>"""))
