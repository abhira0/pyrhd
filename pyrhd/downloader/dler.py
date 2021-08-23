import os
import shutil
from threading import BoundedSemaphore

import requests
from utility.cprint.cprint import aprint


class BaseDownloader:
    @classmethod
    def downloadAMedia(
        url: str, dir_: str, title: str, sema4: BoundedSemaphore
    ) -> bool:
        url_filename, ex10sion = url.split("/")[-1].split(".")
        ex10sion = ex10sion.split("?")[0] if "?" in ex10sion else ex10sion
        path_ = f"{dir_}\\{title or url_filename}.{ex10sion}"
        r = requests.get(url, stream=True)
        downloaded = os.path.exists(path_)
        if r.status_code == 200 and not downloaded:
            r.raw.decode_content = True
            with open(path_ + ".part", "wb") as f:
                shutil.copyfileobj(r.raw, f)
            downloaded = True
            os.rename(path_ + ".part", path_)
            aprint(f"[+] Downloaded media from ", "green", url, "magenta")
        if not downloaded:
            aprint(f"❗ {r.status_code} Error while downloading ", "red", url, "magenta")
        sema4.release()
        return downloaded
