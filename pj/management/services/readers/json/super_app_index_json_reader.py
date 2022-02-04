from pj.services.readers.json_reader import JSONReader

class SuperAppIndexJSONReader(JSONReader):
    @classmethod
    def perform(cls, url):
        return super(cls, cls).perform(url)['datos']
