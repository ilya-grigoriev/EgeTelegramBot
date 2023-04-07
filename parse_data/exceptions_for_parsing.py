"""Module is designed for Python exceptions."""


class FilePathIsNotStr(Exception):
    """Raise when filepath is not string."""


class WrongHtmlCode(Exception):
    """Raise when html code is incorrect."""


class WrongTemplateUrl(Exception):
    """Raise when template url is incorrect."""


class WrongClientSession(Exception):
    """Raise when client session is incorrect."""


class WrongNumberIssue(Exception):
    """Raise when number issue is incorrect."""


class WrongIsDetailed(Exception):
    """Raise when is_detailed is incorrect."""


class SessionClosed(Exception):
    """Raised when client session is closed."""


class WrongSubtopicDataclass(Exception):
    """Raised when subtopic dataclass is incorrect."""


class WrongSubjectNameEnglish(Exception):
    """Raised when subject name english is not in list of subjects."""


class WrongNumberSubtopic(Exception):
    """Raise when number subtopic is incorrect."""


class WrongTypeHtml(Exception):
    """Raise when type html is not in list of types html."""


class WrongDataFromDBDataclass(Exception):
    """Raise when data_from_db is not WrongDataFromDBDataclass."""


class WrongIdTask(Exception):
    """Raise when id task is incorrect."""


class WrongUrl(Exception):
    """Raise when url is incorrect."""


class WrongMaxSkip(Exception):
    """Raise when max skip is incorrect."""


class WrongTaskDataclass(Exception):
    """Raise when task is not DataTaskOfSubtopic dataclass."""


class WrongDataIssue(Exception):
    """Raise when issues is not DataIssue dataclass."""
