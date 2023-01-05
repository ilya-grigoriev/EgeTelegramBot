import re
import traceback

from logger_for_project import my_logger


def delete_excess_data_in_tag(*, template_url: str, tag: str) -> str:
    tag = re.sub(r'\s{2,}', ' ', tag)
    tag = re.sub("'", '"', tag)

    sources = re.findall('src="[\w\d\-\.\/]+"', tag)
    for source in sources:
        url = source.lstrip('src="').rstrip('"')
        if url:
            total_url = f'{template_url}{url}'
            new_source = f'src="{total_url}"'
            tag = re.sub(source, new_source, tag)

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


def format_table_in_html(*, html):
    answer = []
    table_with_answer = html.find_all('tr')[-1]
    for number in table_with_answer.find_all('td'):
        answer.append(str(number.text).strip())
    return '', ''.join(answer)


def format_answer_from_tag(*, html: str):
    pattern = re.compile('Ответ:((?!<\/p>)[\w\W])*')
    tag_answer = re.search(pattern, html)
    solution_html = ''
    answer_text = ''
    if tag_answer:
        tag_answer = re.sub(r'</span>', '', tag_answer.group())
        tag_answer = re.sub(r'<p>', '', tag_answer)
        solution_html = re.sub("'", '"', html)
        if tag_answer:
            answer_text = tag_answer.split(':')
            answer_text = ' '.join(answer_text[1:])
            answer_text = answer_text.strip().strip('.')
    return solution_html, answer_text.strip()


if __name__ == '__main__':
    print(format_answer_from_tag(
        html=open('test12.html', encoding='utf-8').read()))
