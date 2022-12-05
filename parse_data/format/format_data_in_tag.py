import re


def delete_excess_data_in_tag(tag: str) -> str:
    tag = re.sub('<math>[\w\W]+</math>', '', tag)
    tag = re.sub('MathType[A-Za-z\d@+=]+', '', tag)
    tag = re.sub('\s{2,}', ' ', tag)
    # tag = re.sub('<img((?!<)[\w\W])+', '[]', tag)
    # tag = re.sub("style='[\d\w;.:\s-]+'", '', tag)
    tag = re.sub("'", "\"", tag)
    sources = re.findall('\/api\/docs\/byid\/\d+', tag)
    for source in sources:
        tag = re.sub(source, f'http://os.fipi.ru{source}', tag)
    return tag
