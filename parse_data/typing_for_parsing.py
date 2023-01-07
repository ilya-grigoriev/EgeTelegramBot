import json
from dataclasses import dataclass, field
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, List, Any, TypedDict

id_task_from_db = int
type_subject_id = int
data_task = Dict[str, Optional[str | int]]
data_subjects = Optional[List[Dict[str, str]]]
data_from_json = Optional[List[data_task]]
converted_images_to_bytes = List[bytes]
type_converted_images = Dict[str, Optional[bytes]]


@dataclass
class DataTaskOfSubtopic:
    id_task: int = -1
    task_desc_html: str = ""
    text_for_task_html: str = ""
    solution_html: str = ""
    answer: str = ""


DataForDB = None


@dataclass
class DataSubtopic:
    number_subtopic: int = -1
    title: str = ""
    ind_subtopic: int = -1
    tasks: List[DataTaskOfSubtopic] = field(default_factory=list)


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
    converted_image: type_converted_images


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
    issue: int | str = Field(alias="issue")
    title: str = Field(alias="title")
    type: str = Field(alias="type")
    subtopics: Any = Field(alias="subtopics")

    @validator("issue")
    def check_number_task(cls, val):
        if isinstance(val, str):
            return val if val.isdigit() else 0
        return val if isinstance(val, int) else 0

    @validator("subtopics")
    def check_subtopics(cls, val):
        formatted_subtopics = []
        if isinstance(val, list):
            for ind_subtopic, subtopic in enumerate(val, start=1):
                data_subtopic = DataSubtopicForTG(
                    n_subtopic=ind_subtopic, title=subtopic["title"]
                )
                formatted_subtopics.append(data_subtopic)
            return formatted_subtopics
        return formatted_subtopics


class DataSubjectForTG(TypedDict):
    title: str
    issues: List[DataTask]


if __name__ == "__main__":
    file = open("test.json", encoding="utf-8")
    data = json.load(file)
    for task in data.get("constructor"):
        print(DataTask(**task).dict())
