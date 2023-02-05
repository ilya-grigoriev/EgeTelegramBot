"""This module help to parse data and insert them to database."""
import asyncio
import time

from logger_for_project import my_logger
from parse_data.format.format_data_for_database import format_and_insert_tasks
from parse_data.get_data.get_data_of_subject import get_json_of_data_subject
from parse_data.get_data.get_subject_id import get_data_subject_from_json
from parse_data.convert.convert_data import convert_subtopic_to_dataclass
from parse_data.typing_for_parsing import DataIssue


async def parse_data_and_update_db(*, subject_name_en: str) -> None:
    """
    Parse data from https://ege.sdamgia.ru/ and insert them to database.

    Parameters
    ----------
    subject_name_en: str
        The name of the subject in English.
    """
    my_logger.info("Getting json of subject data...")
    data_subjects = get_json_of_data_subject(subject_name_en=subject_name_en)
    my_logger.success("Getting json of subject data is finished")

    my_logger.info("Getting subject data from json...")
    formatted_data = get_data_subject_from_json(data_subjects=data_subjects)
    my_logger.success("Getting subject data is finished")
    if formatted_data:
        for ind_issue, num_issue in enumerate(formatted_data, start=1):
            is_detailed = False
            if num_issue.type_issue == "detailed":
                is_detailed = True

            async_subtopics = [
                convert_subtopic_to_dataclass(
                    data_subtopic=subtopic,
                    subject_name_en=subject_name_en,
                    n_issue=ind_issue,
                    n_subtopic=ind_subtopic,
                    is_detailed=is_detailed,
                )
                for ind_subtopic, subtopic in enumerate(num_issue.subtopics, start=1)
            ]
            my_logger.info("Start converting subtopic in dataclass...")
            formatted_subtopics = await asyncio.gather(*async_subtopics)
            my_logger.success("Converting subtopic is finished")

            data_issue = DataIssue(
                number_issue=int(num_issue.issue),
                title=num_issue.title,
                is_detailed=is_detailed,
                subtopics=formatted_subtopics,
            )

            my_logger.info("Inserting data in db...")
            await format_and_insert_tasks(
                issues=[data_issue], subject_name_en=subject_name_en
            )
            my_logger.success("Inserting data is finished")

            time.sleep(3)
        my_logger.info("Tasks formatted")


if __name__ == "__main__":
    asyncio.run(parse_data_and_update_db(subject_name_en="phys"))
