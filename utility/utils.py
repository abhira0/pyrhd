import os
from bs4.element import ResultSet
from typing import Union
import requests
from bs4 import BeautifulSoup


class UTILS:
    def sourceCode(
        url: Union[str, requests.models.Response], selector: str
    ) -> ResultSet:
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
        """Checks whether the given path/directory is present or not, if not present it creates one."""
        try:
            if not os.path.exists(subdir_path):
                os.mkdir(subdir_path)
        except:
            ...

    def makedirs(subdir_path: str) -> None:
        """Checks whether the given path/directory is present or not, if not present it creates one. Works recursively"""
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path, exist_ok=True)
