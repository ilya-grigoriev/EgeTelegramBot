"""This module help to converting data to dataclass"""
from logger_for_project import my_logger
from parse_data.create_data.create_urls import create_urls_for_request
from parse_data.typing_for_parsing import DataSubtopic, Subtopic
from parse_data.get_data.get_data_of_tasks import \
    get_data_of_tasks_for_subtopic


async def convert_subtopic_to_dataclass(*, data_subtopic: Subtopic,
                                        subject_name_en: str,
                                        n_issue: int,
                                        n_subtopic: int,
                                        is_detailed: str) -> DataSubtopic:
    """Function for converting pydantic model to dataclass.

    Parameters
    ----------
    data_subtopic : Subtopic
        Pydantic model with subtopic data.
    subject_name_en: str
        The name of subject in English.
    n_issue: int
        The serial number of the issue.
    n_subtopic: int
        The serial number of the subtopic.
    is_detailed: bool
        Check issue for non-text answer.
    """
    url = f'https://{subject_name_en}-ege.sdamgia.ru/test?theme={data_subtopic.id}'
    urls = await create_urls_for_request(url=url,
                                         max_skip=data_subtopic.amount)

    my_logger.info(f'Sending requests for {url}')
    formatted_tasks = await get_data_of_tasks_for_subtopic(urls=urls,
                                                           n_issue=n_issue,
                                                           is_detailed=is_detailed)
    my_logger.success('Sending requests is completed')

    if formatted_tasks:
        result_data = DataSubtopic(number_subtopic=data_subtopic.id,
                                   title=data_subtopic.title,
                                   tasks=formatted_tasks,
                                   ind_subtopic=n_subtopic)
        return result_data
    return None
