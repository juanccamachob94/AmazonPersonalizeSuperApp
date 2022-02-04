from urllib.request import urlopen

import json

class JSONReader:
    @classmethod
    def perform(cls, url):
        return json.loads(urlopen(url).read())
