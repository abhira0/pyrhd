import os
import shutil
import time
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
        cls, url: str, dir_: str, title: str = None, sema4: BoundedSemaphore = None
    ) -> bool:
        filename, f10sion = os.path.splitext(title or "")
        url_filename, ex10sion = url.split("/")[-1].split(".")
        ex10sion = ex10sion.split("?")[0] if "?" in ex10sion else ex10sion
        path_ = f"{dir_}\\{filename or url_filename}.{ex10sion or f10sion or ''}"

        downloaded = os.path.exists(path_)
        if downloaded:
            aprint(f"⚠️ Existing media ", "green", url, "magenta")
            sema4.release()
            return True

        # TODO: Add resume functionality for partially downloaded files
        # for now, program just deletes partially downloaded
        # files and tries to download from the beginning
        if os.path.exists(path_ + ".part"):
            os.remove(path_ + ".part")

        try:
            r = requests.get(url, stream=True)
        except Exception as e:
            aprint(e, "red")

        if r and r.status_code == 200:
            r.raw.decode_content = True
            with open(path_ + ".part", "wb") as f:
                shutil.copyfileobj(r.raw, f)
            aprint(f"✅ Downloaded media from ", "green", url, "magenta")
            time.sleep(0.5)
            try:
                os.rename(path_ + ".part", path_)
            except Exception as e:
                aprint(e, "red")
            downloaded = True

        if not downloaded:
            msg = f"❎ {r.status_code if r else ''} Error while downloading "
            aprint(msg, "red", url, "magenta")
        if sema4:
            sema4.release()
        return downloaded
