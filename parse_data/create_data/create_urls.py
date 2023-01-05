import asyncio
import copy
from typing import List, Dict, Tuple

from parse_data.typing_for_parsing import DataTask


def create_urls_for_subject(*, subject_name_en: str,
                            data):
    formatted_data = []
    for task in data_subject:
        formatted_dict = copy.deepcopy(task.dict())
        task = task.dict()
        if 'subtopics' in task:
            subtopics = task.get('subtopics')
            for ind, subtopic in enumerate(subtopics):
                id = subtopic.get('id')
                total_url = f'https://{subject_name_en}-ege.sdamgia.ru/test?theme={id}'
                cur_subtopic_dict = formatted_dict.get('subtopics')[ind]
                cur_subtopic_dict.update({'url': total_url})
                formatted_dict['subtopics'][ind] = cur_subtopic_dict
            formatted_data.append(formatted_dict)
    return formatted_data


async def create_urls_for_request(*, url: str, max_skip: int):
    urls_with_data = []
    skip = 5
    max_amount = max_skip
    if url:
        while max_amount >= 5:
            max_amount -= 5
            urls_with_data.append(
                (url, {'ajax': '1', 'skip': skip, 'max_skip': max_skip}))
            skip += 5
        urls_with_data.append(
            (url, {'ajax': '1', 'skip': max_skip, 'max_skip': max_skip}))
        urls_with_data.append((url, dict()))
    return urls_with_data


if __name__ == '__main__':
    print(asyncio.run(create_urls_for_request(url='a', max_skip=116)))
