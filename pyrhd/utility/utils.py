import os
from typing import Union

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from termcolor import cprint

from cprint.cprint import aprint


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
    # If the given url is actually the 'Response' of the get method
    if type(url) == requests.models.Response:
        plain_text = url.text
    # If the given url the URL in 'string' data type
    elif type(url) == str:
        plain_text = requests.get(url).text
    # return the selected elements through Beautifulsoup and CSS selector
    return BeautifulSoup(plain_text, "html.parser").select(selector)


def makedir(path: str, verbose: bool = False) -> None:
    """Checks whether the given path/directory is present or not,
    if not present, creates one

    Args:
        path (str): Path of the directory to be created
        verbose (bool, optional): Verbose. Defaults to False.
    """
    if not os.path.exists(path):
        os.mkdir(path)
        if verbose:
            aprint(f"✅  Directory created : '{path}'", "green")
    elif verbose:
        aprint(f"⚠️   Directory existed : '{path}'", "cyan")


def makedirs(path: str, verbose: bool = False) -> None:
    """Calls os.makedirs(path[, exist_ok=True])
        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, don't raise an OSError. This is recursive.

    Args:
        path (str): Path of the directory to be created
        verbose (bool, optional): Verbose. Defaults to False.
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        if verbose:
            aprint(f"✅  Directory created recursively: '{path}'", "green")
    elif verbose:
        aprint(f"⚠️   Directory existed : '{path}'", "cyan")


def cleanPathName(text: str) -> str:
    """Clean the path name according ot the Windows 10 file system rule

    Args:
        text (str): path

    Returns:
        str: cleaned path with no illegal character
    """
    excluded = ["\\", "/", "<", ">", "|", '"', "?", "*", ":"]
    return "".join(i for i in text if i not in excluded)
