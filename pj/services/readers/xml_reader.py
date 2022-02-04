import requests
import xmltodict

# TODO: Create and use a reader of JSON url to select the data of another source
class XMLReader:
    CONTAINERS = [] # hierarchically ordered

    @classmethod
    def perform(cls, url):
        """
            return the <sitemap> collection; each item is a OrderedDict instance
            with the keys locm and lastmod of xml file.
        """
        # XML Content Oredered Dict object <class 'collections.OrderedDict'>
        content = xmltodict.parse(requests.get(url).content)
        for container in cls.CONTAINERS:
            content = content.get(container, content)
        if isinstance(content, list):
            return content
        elif not content:
            return []
        return [content]
