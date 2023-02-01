import json
from dataclasses import dataclass, field
from pydantic import BaseModel, Field, root_validator
from typing import Optional, Dict, List, Any, TypedDict, NewType, IO, Tuple, Sequence

id_task_from_db = NewType("id_task_from_db", int)
subject_id = NewType("subject_id", int)
data_task = NewType("data_task", Dict[str, Optional[str | int]])
typing_data_subjects = List[Dict[str, str]]
data_from_json = NewType("data_from_json", List[data_task])
typing_converted_images_to_bytes = Optional[List[IO[bytes]]]
converted_image = Optional[bytes]
typing_converted_images = Dict[str, typing_converted_images_to_bytes]
typing_data_payload = Dict[str, str | int]
typing_url = str
typing_urls_with_data = List[Tuple[typing_url, typing_data_payload]]
typing_request_data = Tuple[typing_url, typing_data_payload]
formatted_data_for_db = List[Optional[str]]


@dataclass
class DataTaskOfSubtopic:
    id_task: int = -1
    task_desc_html: str = ""
    text_for_task_html: str = ""
    file_urls_for_task: str = ""
    solution_html: str = ""
    answer: str = ""


typing_task = Optional[DataTaskOfSubtopic]
typing_data_of_tasks = Sequence[typing_task]


@dataclass
class DataSubtopic:
    number_subtopic: int = -1
    title: str = ""
    ind_subtopic: int = -1
    tasks: typing_data_of_tasks = field(default_factory=list)


@dataclass
class DataIssue:
    number_issue: int = -1
    title: str = ""
    is_detailed: bool = False
    subtopics: List[DataSubtopic] = field(default_factory=list)


@dataclass
class DataForTG:
    text: str
    id: int
    correct_answer: str
    file_path: str
    converted_image: typing_converted_images


@dataclass(frozen=True)
class DataFromDB:
    task_section: str
    id_task: int
    is_detailed: bool
    task_desc_html: str
    text_for_task_html: str
    solution_html: str
    answer: str


class Subtopic(BaseModel):
    id: int = Field(alias="id")
    title: str = Field(alias="title")
    amount: int = Field(alias="amount")


@dataclass
class DataSubtopicForTG:
    n_subtopic: str
    title: str


class DataTask(BaseModel):
    id_issue: Optional[str] = Field(alias="id")
    issue: int | str = Field(alias="issue")
    title: str = Field(alias="title")
    type_issue: str = Field(alias="type")
    subtopics: Any = Field(alias="subtopics")
    amount: int = Field(alias="amount")

    @root_validator
    def check_subtopics(cls, val):
        id_issue = val.get("id_issue")
        issue = val.get("issue")
        title = val.get("title")
        type_issue = val.get("type_issue")
        subtopics = val.get("subtopics")
        amount = val.get("amount")

        if isinstance(issue, str):
            issue = issue if issue.isdigit() else 0
        else:
            issue = issue if isinstance(issue, int) else 0

        formatted_subtopics = []
        if not isinstance(subtopics, list):
            data_issue = Subtopic(**{"id": id_issue, "title": "", "amount": amount})
            formatted_subtopics.append(data_issue)
        elif isinstance(subtopics, list):
            for ind_subtopic, subtopic in enumerate(subtopics, start=1):
                data_subtopic = Subtopic(**subtopic)
                formatted_subtopics.append(data_subtopic)

        result = {
            "issue": issue,
            "title": title,
            "type_issue": type_issue,
            "subtopics": formatted_subtopics,
        }
        return result


formatted_data_subjects = Optional[List[DataTask]]


class DataSubjectForTG(TypedDict):
    title: str
    issues: List[DataTask]


if __name__ == "__main__":
    file = open("test.json", encoding="utf-8")
    data = json.load(file)
    for task in data.get("constructor"):
        print(DataTask(**task).dict())
