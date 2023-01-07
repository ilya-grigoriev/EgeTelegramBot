from typing import List

from parse_data.format.format_data_for_database import format_data_for_db
from parse_data.typing_for_parsing import DataIssue
from work_with_db.create_data.insert_data import insert_tasks


async def format_and_insert_tasks(*, issues: List[DataIssue],
                                  subject_name_en: str) -> None:
    if issues:
        data_for_db = []
        for issue in issues:
            if issue.subtopics:
                for subtopic in issue.subtopics:
                    if subtopic:
                        for task in subtopic.tasks:
                            formatted_task = format_data_for_db(task=task,
                                                                number_task=issue.number_issue,
                                                                is_detailed=issue.is_detailed,
                                                                number_subtopic=subtopic.ind_subtopic)
                            data_for_db.append(formatted_task)
        await insert_tasks(subject_name_en=subject_name_en,
                           values_for_inserting=data_for_db)
