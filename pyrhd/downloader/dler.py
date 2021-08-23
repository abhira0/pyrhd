import os
import shutil
from threading import BoundedSemaphore, Thread

import requests
from pyrhd.harvester.hrv8r import BaseHarvester
from pyrhd.utility.cprint import aprint


class BaseDownloader(BaseHarvester):
    def __init__(self, ultimatum_path) -> None:
        self.ultimatum_path = ultimatum_path
        self.ultimatum = {}
        self.getFileData()
        self.life_saver_thr = Thread(target=self.lifeSaver, daemon=True)
        self.life_saver_thr.start()

    @classmethod
    def downloadAMedia(
        cls, url: str, dir_: str, title: str, sema4: BoundedSemaphore
    ) -> bool:
        filename, f10sion = os.path.splitext(title)
        url_filename, ex10sion = url.split("/")[-1].split(".")
        ex10sion = ex10sion.split("?")[0] if "?" in ex10sion else ex10sion
        path_ = f"{dir_}\\{filename or url_filename}.{ex10sion or f10sion or ''}"
        downloaded = os.path.exists(path_)
        if downloaded:
            aprint(f"⚠️ Existing media ", "green", url, "magenta")
            return True
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(path_ + ".part", "wb") as f:
                shutil.copyfileobj(r.raw, f)
            downloaded = True
            os.rename(path_ + ".part", path_)
            aprint(f"✅ Downloaded media from ", "green", url, "magenta")
        if not downloaded:
            msg = f"❎ {r.status_code} Error while downloading "
            aprint(msg, "red", url, "magenta")
        sema4.release()
        return downloaded
