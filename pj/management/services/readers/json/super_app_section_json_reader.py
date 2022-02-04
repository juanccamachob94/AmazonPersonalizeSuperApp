from pj.services.readers.json_reader import JSONReader

class SuperAppSectionJSONReader(JSONReader):
    @classmethod
    def perform(cls, url):
        return super(cls, cls).perform(url)['rss']['noticias']
