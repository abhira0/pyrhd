import json
import os
import threading
import time

SAVING_INTERVAL = 10


class BaseHarvester:
    def __init__(self, ultimatum_path) -> None:
        self.ultimatum_path = ultimatum_path
        self.ultimatum = {}
        self.getFileData()
        self.life_saver_thr = threading.Thread(target=self.lifeSaver, daemon=True)
        self.life_saver_thr.start()

    def getFileData(self):
        try:
            if os.path.exists(self.ultimatum_path):
                with open(self.ultimatum_path, "r") as f:
                    buffer = f.read()
                    for i in range(3):
                        last = "}" * i
                        try:
                            content = buffer + last
                            self.ultimatum = json.loads(content)
                            break
                        except:
                            ...
            else:
                raise Exception
        except:
            p = os.path.dirname(self.ultimatum_path)
            os.makedirs(p, exist_ok=True)
            self.ultimatum = {}
        self.saveUltimatum()

    def saveUltimatum(self):
        with open(self.ultimatum_path, "w") as f:
            # use copy() to avoid "RuntimeError: dictionary changed size during iteration"
            json.dump(self.ultimatum.copy(), f)

    def lifeSaver(self):
        while True:
            time.sleep(SAVING_INTERVAL)
            self.saveUltimatum()
