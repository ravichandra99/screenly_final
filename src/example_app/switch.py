import requests
from requests.structures import CaseInsensitiveDict
import threading
import os
import dot
# from screenly_ose import Screenly


def switch_asset(_id,dev):
    url = os.getenv("IVIS_SCREENLY_API1")+"{}".format(_id)+os.getenv("IVIS_SCREENLY_API2")+"{}".format(dev) #url = os.getenv("SCREENLY_CONTROL_API")+"asset&{}".format(_id)
    print(url)
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    resp = requests.get(url, headers=headers)
    return resp.status_code


class TestThreading(object):
    def __init__(self,_id,dev, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=(_id,dev,))
        thread.daemon = True
        thread.start()

    def run(self,_id,dev):
            switch_asset(_id,dev)


