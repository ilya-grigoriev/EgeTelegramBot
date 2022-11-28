import re


def get_img_url_from_tag(tag: str):
    pattern = r'\/api\/docs\/byid\/\d+'
    finding = re.findall(pattern, tag)
    return finding if finding else ''


if __name__ == '__main__':
    # print(get_img_url_from_tag(
    #     "<!DOCTYPE html>\r\n<html test=\"\">\r\n<head>\r\n <title tasktype=\"InputTextMany\">&#x412;&#x432;&#x435;&#x434;&#x438;&#x442;&#x435; &#x43E;&#x442;&#x432;&#x435;&#x442; &#x432; &#x43F;&#x43E;&#x43B;&#x435; &#x432;&#x432;&#x43E;&#x434;&#x430;</title>\r\n <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n <meta charset=\"utf-8\">\r\n <link href=\"/Content/KimTemplate/kimTmp.css\" rel=\"stylesheet\">\r\n <link href=\"/Content/KimTemplate/kimTmpInputTextMany.css\" r…ыла наибольшей за указанный период.</p> <p class=\"MsoNormal\" align=\"center\"><script language='javascript'> ShowPictureQ('docs/7180F95137BF9FEF48092553403ECAB5/questions/C62C7B3FE63586F946F9845820A43203/xs3qstsrcC62C7B3FE63586F946F9845820A43203_1_1326808337.png');</script><span></span></p> \r\n <div style=\"margin-top: 10px;\">\r\n <input id=\"answer_1\" class=\"answer\" number=\"1\" type=\"text\" placeholder=\"Введите ответ\">\r\n </div>\r\n </div>\r\n</body>\r\n</html>"))
    print(get_img_url_from_tag('a'))
