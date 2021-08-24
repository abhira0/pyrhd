import os
import threading
from typing import Callable, List, Tuple, Union

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from pyrhd.utility.cprint import aprint


class Utils:
    class requests:
        @staticmethod
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
            # If the given url the URL in 'string' format
            if type(url) == str:
                url = requests.get(url)
            plain_text = url.text
            if url.status_code != 200:
                return []
            # return the selected elements through Beautifulsoup and CSS selector
            return BeautifulSoup(plain_text, "html.parser").select(selector)

    class os:
        @staticmethod
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

        @staticmethod
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

        @staticmethod
        def cleanPathName(text: str) -> str:
            """Clean the path name according ot the Windows 10 file system rule

            Args:
                text (str): path

            Returns:
                str: cleaned path with no illegal character
            """
            excluded = ["\\", "/", "<", ">", "|", '"', "?", "*", ":"]
            return "".join(i for i in text if i not in excluded)

        @staticmethod
        def getCFD(f) -> str:
            """Get the absolute "Current File Directory" path

            Args:
                f (str): file absolute path

            Returns:
                str: Absolute path of the parent directory
            """
            return os.path.dirname(f)

    class threading:
        @staticmethod
        def joinThreads(thr: List[threading.Thread]) -> None:
            """Join all the threads present in the parameter list

            Args:
                thr (List[threading.Thread]): List of all the threads which are to be joined
            """
            [i.join() for i in thr]

        def createThread(
            target: Callable, args: Union[List, Tuple], thr_list: list
        ) -> threading.Thread:
            """Create a thread, append the thread to a given list
            for further use and finally start the thread.

            Args:
                target (function): target method /function to thread
                args (Union[List, Tuple]): list of arguments to be passed (must be in order)
                thr_list (list): List of threads

            Returns:
                threading.Thread: Newly created thread is returned after starting it
            """
            # Thread arguments must be a encapsulated in a tuple
            if type(args) != tuple:
                args = tuple(args)
            # Create a thread using threading module
            thread = threading.Thread(target=target, args=args)
            thr_list.append(thread)  # Appending to thread's list
            thread.start()  # Starting the thread
            return thread  # Return created thread
