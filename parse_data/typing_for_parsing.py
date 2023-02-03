"""This module is designed to create type-hints."""
import dataclasses
from typing import Optional, Dict, List, Any, TypedDict, NewType, IO, Tuple, Sequence
from pydantic import BaseModel, Field, root_validator

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


@dataclasses.dataclass
class DataTaskOfSubtopic:
    """Dataclass for formatting data of subtopic's task."""

    id_task: int = -1
    task_desc_html: str = ""
    text_for_task_html: str = ""
    file_urls_for_task: str = ""
    solution_html: str = ""
    answer: str = ""


typing_task = Optional[DataTaskOfSubtopic]  # pylint: disable=invalid-name
typing_data_of_tasks = Sequence[typing_task]  # pylint: disable=invalid-name


@dataclasses.dataclass
class DataSubtopic:
    """Dataclass for formatting of subtopic."""

    number_subtopic: int = -1
    title: str = ""
    ind_subtopic: int = -1
    tasks: typing_data_of_tasks = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class DataIssue:
    """Dataclass for formatting data of issue."""

    number_issue: int = -1
    title: str = ""
    is_detailed: bool = False
    subtopics: List[DataSubtopic] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class DataForTG:
    """Dataclass for formatting data for Telegram."""

    text: str
    id: int  # pylint: disable=invalid-name
    correct_answer: str
    file_path: str
    converted_image: typing_converted_images


@dataclasses.dataclass(frozen=True)
class DataFromDB:  # pylint: disable=too-many-instance-attributes
    """Dataclass for formatting data from database."""

    task_section: str
    id_task: int
    is_detailed: bool
    task_desc_html: str
    file_urls_for_task: str
    text_for_task_html: str
    solution_html: str
    answer: str


class Subtopic(BaseModel):  # pylint: disable=too-few-public-methods
    """Pydantic model for formatting data of subtopics."""

    id: int = Field(alias="id")
    title: str = Field(alias="title")
    amount: int = Field(alias="amount")


typing_subtopics = List[Optional[Subtopic]]


@dataclasses.dataclass
class DataSubtopicForTG:
    """Dataclass for formatting data of subtopic for Telegram."""

    n_subtopic: str
    title: str


class DataTaskDict(TypedDict):
    """Typed dict for formatting data of task from dict."""

    issue: int
    title: str
    type_issue: str
    subtopics: typing_subtopics


class DataFromJson(TypedDict):
    """Typed dict for formatting data of task from json."""

    id_issue: Optional[str]
    issue: int | str
    title: str
    type_issue: str
    subtopics: Any
    amount: int


class DataTask(BaseModel):  # pylint: disable=too-few-public-methods
    """Pydantic model for formatting data of task."""

    id_issue: Optional[str] = Field(alias="id")
    issue: int | str = Field(alias="issue")
    title: str = Field(alias="title")
    type_issue: str = Field(alias="type")
    subtopics: Any = Field(alias="subtopics")
    amount: int = Field(alias="amount")

    @root_validator
    def check_subtopics(cls, val: DataFromJson) -> DataTaskDict:
        """
        Parameters.

        ----------
        val: DataFromJson
            Pydantic model with all variables for formatting data.

        Returns
        -------
        DataTaskDict
            Typed dict with data of task.
        """
        id_issue = val.get("id_issue")
        issue = val.get("issue")
        title = val.get("title")
        type_issue = val.get("type_issue")
        subtopics = val.get("subtopics")
        amount = val.get("amount")

        if isinstance(issue, str):
            issue = int(issue) if issue.isdigit() else 0
        else:
            issue = issue if isinstance(issue, int) else 0

        formatted_subtopics: typing_subtopics = []
        if not isinstance(subtopics, list):
            data_issue = Subtopic(**{"id": id_issue, "title": "", "amount": amount})
            formatted_subtopics.append(data_issue)
        elif isinstance(subtopics, list):
            for subtopic in subtopics:
                data_subtopic = Subtopic(**subtopic)
                formatted_subtopics.append(data_subtopic)

        result = DataTaskDict(
            issue=issue,
            title=title if title else "",
            type_issue=type_issue if type_issue else "",
            subtopics=formatted_subtopics,
        )
        return result


formatted_subjects = Optional[List[DataTask]]  # pylint: disable=invalid-name


class DataSubjectForTG(TypedDict):
    """
    TypedDict of data subject for Telegram.

    Parameters
    ----------
    title: str
        Title of subject.
    issues: List[DataTask]
        List of dataclass of tasks.
    """

    title: str
    issues: List[DataTask]
