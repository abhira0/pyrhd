import os
from typing import Union

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet


def sourceCode(url: Union[str, requests.models.Response], selector: str) -> ResultSet:
    """Returns the selected elements from html source code

    Args:
        url (Union[str, requests.models.Response]): There can be two inputs
            1. str: when the URL is given, make a request implicitly and then parse the response
            2. Response: when request is already sent by the calling function, and just need to parse the respose

        selector (str): CSS Selector to select the elements

    Returns:
        ResultSet: Selected elements from the DOM (html source code)
    """
    check4resp = type(url) == requests.models.Response
    plain_text = url.text if check4resp else requests.get(url).text
    soup_select = BeautifulSoup(plain_text, "html.parser").select(selector)
    return soup_select


def makedir(subdir_path: str) -> None:
    """Checks whether the given path/directory is present or not,
    if not present, creates one.

    Args:
        subdir_path (str): [description]
    """
    try:
        if not os.path.exists(subdir_path):
            os.mkdir(subdir_path)
    except:
        ...


def makedirs(dir_path: str) -> None:
    """Calls os.makedirs(path[, exist_ok=True])
        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, don't raise an OSError. This is recursive.

    Args:
        dir_path (str): path of the directory to be created
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
