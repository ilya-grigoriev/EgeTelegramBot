"""Module is designed for checking network session."""
import aiohttp
from parse_data import exceptions_for_parsing


def check_arg_session(session: aiohttp.ClientSession):
    """
    Check arguments of Aiohttp session.

    Parameters
    ----------
    session : aiohttp.ClientSession
    """
    try:
        if not isinstance(session, aiohttp.ClientSession):
            raise exceptions_for_parsing.WrongClientSession
        if session.closed:
            raise exceptions_for_parsing.SessionClosed
    except Exception:
        raise exceptions_for_parsing.WrongClientSession
